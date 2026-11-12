# ZodiacApp

A small Python/Tkinter desktop app: enter a birth date and it tells you which of the
twelve zodiac signs it falls under, with the date range and a short description.
Packed with PyInstaller into a single Windows executable.

## Features

- Year/month/day spin boxes instead of free-text dates, with validation
- All twelve signs with their date ranges and descriptions
- Background music loop, with a fallback that keeps the app running if the audio
  file or device is missing
- Single-file Windows build via `zodiac_app.spec`

## Run

```bash
pip install -r requirements.txt
python zodiac_app.py
```

## Build

```bash
pyinstaller zodiac_app.spec
```

The executable lands in `dist/`. The spec bundles the `Music` folder so the packaged
app still finds its audio file.

## Stack

Python 3, Tkinter, pygame, PyInstaller.

## Notes

- The UI is in Chinese.

## License

MIT
