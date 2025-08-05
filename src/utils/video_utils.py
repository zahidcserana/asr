import logging
import os
import openai
from src.config import get_whisper_provider
from src.utils.asr_local import transcribe_local

def get_whisper_srt(project_id, audio_bytes: bytes):
    provider = get_whisper_provider()

    if provider == "openai":
        return transcribe_openai(audio_bytes)

    if provider == "faster-whisper":
        return transcribe_local(audio_bytes)

    if provider == "auto":
        try:
            return transcribe_openai(audio_bytes)
        except Exception as e:
            logging.warning(f"OpenAI failed: {e}, falling back to local.")
            return transcribe_local(audio_bytes)

    raise ValueError(f"Invalid provider: {provider}")

def transcribe_openai(audio_bytes: bytes):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    resp = openai.Audio.transcribe("whisper-1", audio_bytes, response_format="verbose_json")
    return resp
