from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
def speech_to_text(file_name):
    transcript = pipeline(file_name)
    return transcript

