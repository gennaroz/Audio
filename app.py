from flask import Flask, request, jsonify
import openai
import tempfile

openai.api_key = "TBmBW7kVDtvmOxT41hLZXAFjSthAag62AjAp3epeUd7ATCUUy9aTSRUndTVZB5Q"

app = Flask(__name__)

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['file']
    with tempfile.NamedTemporaryFile(suffix=".wav") as temp:
        audio_file.save(temp.name)
        transcript = openai.Audio.transcribe("whisper-1", open(temp.name, "rb"))
        return jsonify({"text": transcript["text"]})

if __name__ == '__main__':
    app.run()
