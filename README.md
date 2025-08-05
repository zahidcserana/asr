# ASR Project (OpenAI + Faster-Whisper Fallback)

## ASR Provider Switch

This project supports two ASR providers:

### OpenAI Whisper API (default)
- Set `WHISPER_PROVIDER=openai`
- Requires `OPENAI_API_KEY` in your `.env`.

### Local Faster-Whisper
- Install: `pip install faster-whisper==0.7.0`
- Set `WHISPER_PROVIDER=faster-whisper`
- Good for local CPU transcription.

### Auto Mode
- Set `WHISPER_PROVIDER=auto`
- Tries OpenAI first, falls back to local if API fails.

### FFmpeg Note
If running locally, install ffmpeg:
```bash
sudo apt install ffmpeg
```
[More info](https://ffmpeg.org/download.html)

## Run Instructions

```bash
pip install -r requirements.txt
cp dev.env .env
python src/app.py
python run.py
```

## Testing

```bash
pytest -q
```
