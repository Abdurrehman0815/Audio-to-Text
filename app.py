from flask import Flask, render_template, request, jsonify
import whisper
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper Model (tiny for speed)
model = whisper.load_model("tiny")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "Missing audio file"}), 400

    audio_file = request.files["audio"]
    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    # Transcribe audio (default language: English)
    result = model.transcribe(file_path)

    os.remove(file_path)  # Delete after processing

    return jsonify({"text": result["text"]})

if __name__ == "__main__":
    app.run(debug=True)
