import os
import pytest
from src.app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_local_adapter_output():
    from src.utils.asr_local import transcribe_local
    with open("tests/dummy_audio.mp3", "rb") as f:
        result = transcribe_local(f.read())
    assert "segments" in result and isinstance(result["segments"], list)
    assert "text" in result

def test_build_srt_faster_whisper(client):
    os.environ["WHISPER_PROVIDER"] = "faster-whisper"

    mock_json = {
        "text": "Hello world",
        "segments": [{
            "id": 0,
            "start": 0.0,
            "end": 1.0,
            "text": "Hello world",
            "words": [{"start": 0.0, "end": 0.5, "word": "Hello"}, {"start": 0.5, "end": 1.0, "word": "world"}]
        }]
    }

    with patch("src.utils.video_utils.transcribe_local", return_value=mock_json):
        with open("tests/dummy_audio.mp3", "rb") as audio:
            response = client.post("/build_srt_file/test_project", data={"audio": audio})
            assert response.status_code == 200
            assert response.json["status"] == "MEDIA_SRT_CREATED"
