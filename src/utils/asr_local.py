from faster_whisper import WhisperModel

model = WhisperModel("tiny", device="cpu")

def transcribe_local(audio_bytes: bytes, language: str = None) -> dict:
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        segments, info = model.transcribe(tmp.name, language=language, word_timestamps=True)

    results = {
        "text": "",
        "segments": []
    }

    for i, segment in enumerate(segments):
        seg = {
            "id": i,
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
            "words": [{"start": w.start, "end": w.end, "word": w.word} for w in segment.words]
        }
        results["text"] += segment.text + " "
        results["segments"].append(seg)

    return results


# def transcribe_local(audio_bytes: bytes, language: str = None) -> dict:
#     return {
#         "text": "Mock transcription.",
#         "segments": [{
#             "id": 0,
#             "start": 0.0,
#             "end": 1.0,
#             "text": "Mock transcription.",
#             "words": [{"start": 0.0, "end": 1.0, "word": "Mock"}]
#         }]
#     }
