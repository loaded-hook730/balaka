# Balaka v0.2.0

Public release focused on frontend localization and launch readiness.

## Highlights

- simple frontend localization with English and Ukrainian UI copy
- English is now the default interface locale for public-facing use
- EN / UA switch persists in the browser
- runtime metadata labels are localized in the frontend
- README updated to reflect the public release flow
- frontend default locale is covered by an API test

## Release links

- Repository: https://github.com/stremovskyy/balaka
- Release: https://github.com/stremovskyy/balaka/releases/tag/v0.2.0

## Validation

- `pytest -q`
- `python -m compileall src main.py`
- `node --check frontend/app.js`

## Suggested promo angle

Balaka stays intentionally simple:

- local-only inference
- FastAPI backend
- separate static frontend
- voice design and voice cloning
- build-free UI
- bilingual public-facing interface
