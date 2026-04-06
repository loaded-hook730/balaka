from __future__ import annotations

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import TypeVar
from urllib.parse import quote

from fastapi import APIRouter, File, Form, Request, Response, UploadFile
from pydantic import BaseModel, ValidationError

from balaka.schemas import AudioResult, CloneRequest, DesignRequest, TTSMetaResponse
from balaka.services import SpeechService, TTSRuntimeError


router = APIRouter(prefix="/tts", tags=["tts"])
RequestModel = TypeVar("RequestModel", bound=BaseModel)


def get_service(request: Request) -> SpeechService:
    return request.app.state.tts_service


def build_audio_response(result: AudioResult) -> Response:
    filename = quote(result.filename)
    headers = {
        "Content-Disposition": f'inline; filename="{filename}"',
        "X-TTS-Status": result.status,
        "Cache-Control": "no-store",
    }
    return Response(content=result.audio_bytes, media_type=result.media_type, headers=headers)


def persist_upload(upload: UploadFile) -> Path:
    suffix = Path(upload.filename or "reference.wav").suffix or ".wav"
    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        upload.file.seek(0)
        shutil.copyfileobj(upload.file, tmp_file)
        return Path(tmp_file.name)


def parse_request(model_cls: type[RequestModel], **payload: object) -> RequestModel:
    try:
        return model_cls(**payload)
    except ValidationError as exc:
        raise TTSRuntimeError(str(exc), status_code=422) from exc


@router.get("/meta", response_model=TTSMetaResponse)
def get_metadata(request: Request) -> TTSMetaResponse:
    return get_service(request).get_metadata()


@router.post("/design")
def synthesize_design(
    request: Request,
    text: str = Form(...),
    language: str = Form("Auto"),
    num_steps: int = Form(32),
    guidance_scale: float = Form(2.0),
    denoise: bool = Form(True),
    speed: float = Form(1.0),
    duration: float | None = Form(None),
    preprocess_prompt: bool = Form(True),
    postprocess_output: bool = Form(True),
    gender: str = Form("Auto"),
    age: str = Form("Auto"),
    pitch: str = Form("Auto"),
    style: str = Form("Auto"),
    accent: str = Form("Auto"),
    dialect: str = Form("Auto"),
) -> Response:
    payload = parse_request(
        DesignRequest,
        text=text,
        language=language,
        num_steps=num_steps,
        guidance_scale=guidance_scale,
        denoise=denoise,
        speed=speed,
        duration=duration,
        preprocess_prompt=preprocess_prompt,
        postprocess_output=postprocess_output,
        gender=gender,
        age=age,
        pitch=pitch,
        style=style,
        accent=accent,
        dialect=dialect,
    )

    result = get_service(request).synthesize_design(payload)
    return build_audio_response(result)


@router.post("/clone")
def synthesize_clone(
    request: Request,
    reference_audio: UploadFile = File(...),
    text: str = Form(...),
    reference_text: str = Form(...),
    language: str = Form("Auto"),
    num_steps: int = Form(32),
    guidance_scale: float = Form(2.0),
    denoise: bool = Form(True),
    speed: float = Form(1.0),
    duration: float | None = Form(None),
    preprocess_prompt: bool = Form(True),
    postprocess_output: bool = Form(True),
) -> Response:
    if not reference_audio.filename:
        raise TTSRuntimeError("Reference audio is required.", status_code=422)

    payload = parse_request(
        CloneRequest,
        text=text,
        language=language,
        reference_text=reference_text,
        num_steps=num_steps,
        guidance_scale=guidance_scale,
        denoise=denoise,
        speed=speed,
        duration=duration,
        preprocess_prompt=preprocess_prompt,
        postprocess_output=postprocess_output,
    )

    temp_audio_path = persist_upload(reference_audio)
    try:
        result = get_service(request).synthesize_clone(payload, temp_audio_path)
    finally:
        temp_audio_path.unlink(missing_ok=True)

    return build_audio_response(result)
