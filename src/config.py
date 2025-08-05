import os
from dotenv import load_dotenv

def load_env_vars(env_file=".env"):
    load_dotenv(env_file)

def get_whisper_provider():
    return os.getenv("WHISPER_PROVIDER", "openai")
