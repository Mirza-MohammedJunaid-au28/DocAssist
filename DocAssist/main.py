print('[Importing Models & Libraries - Pending] . . . ')
from flask import Flask, render_template,request,jsonify,send_file
from model import whisper,emotion,segmentation
import io
print('[Importing Models & Libraries - Done] . . . ')

app = Flask(__name__, static_folder="public", static_url_path="/public")

@app.route('/',methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/login',methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

@app.route('/home',methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template("home.html")

@app.route('/audio',methods=['POST'])
def audio():
    try:
        audio_data = request.data
        print('[Received Audio] . . .')
        audio_file = io.BytesIO(audio_data)
        audio_content = audio_file.read()
        audio_file.seek(0)
        transcription = whisper(audio_content)
        print(transcription)
        sentiment = emotion(audio_content)
        print('Conversation Sentiment : ',sentiment)
        speakers = segmentation({"uri": "audio", "audio": audio_file})
        print('Speaker Segmentation : ',speakers)
        return {'message': 'Audio received successfully'}, 200
    except Exception as e:
        print('[Error] ', str(e))
        return {'error': str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)