import os

os.environ["FFMPEG_PATH"] = "C:/ffmpeg"

try:
    print('[Importing Models & Libraries - Pending] . . . ')
    from model import whisper,emotion,segmentation
    print('[Whisper Imported] . . . ')
    from transformers import pipeline
    print('[Importing Models & Libraries - Complete] . . . ')
except Exception as e:
    print("Exception : ",e)

def toText(audio):
    text = whisper(audio)
    return text

def text_emotion(audio):
    sentiment = emotion(audio)
    return sentiment

def speaker_segmentation(audio):
    seg = segmentation(audio)
    return seg

audio = './convo.wav'
text = toText(audio)
sentiment = text_emotion(audio)
seg = speaker_segmentation(audio)
print('Text : ',text)
print('Sentiment : ',sentiment)
print('Speaker Segmentation : ',seg)