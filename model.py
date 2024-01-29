from transformers import pipeline
from pyannote.audio import Pipeline

#  Text to Speech
# whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-medium', device = -1)

# Emotion Recognition
""" emotion = pipeline('audio-classification',model='superb/wav2vec2-base-superb-er') """

# Speaker Segementation 
segmentation = Pipeline.from_pretrained(
  "pyannote/speaker-diarization-3.0",
  use_auth_token="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")

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")