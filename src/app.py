from flask import Flask, request, jsonify
from src.config import load_env_vars
from src.utils.video_utils import get_whisper_srt

app = Flask(__name__)
load_env_vars("dev.env")

@app.route("/build_srt_file/<project_id>", methods=["POST"])
def build_srt_file(project_id):
    audio = request.files.get("audio")
    if not audio:
        return jsonify({"error": "No audio file"}), 400
    try:
        verbose_json = get_whisper_srt(project_id, audio.read())
        return jsonify({
            "message": "SRT created",
            "status": "MEDIA_SRT_CREATED",
            "data": verbose_json
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
