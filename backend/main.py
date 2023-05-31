from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from speech_to_text import analyze_audio
from pydub import AudioSegment
import os
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'deom-for-interview-b0a1bb996236.json'
app = FastAPI()

origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8000",  # FastAPI server (this may not be necessary)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/audio/")
async def analyze_audio_file(file: UploadFile = File(...)):
    print("Received a request to analyze audio.")
    try:
        audio_content = await file.read()
        print("Received audio content size: ", len(audio_content))
        # Write the uploaded audio file to disk
        with open('audio.webm', 'wb') as out:
            out.write(audio_content)

        # Convert the .webm file to .wav
        audio = AudioSegment.from_file('audio.webm', format="webm")
        audio.export('audio.wav', format="wav")

        # Load the .wav file and send to Google Speech-to-Text
        with open('audio.wav', 'rb') as wav_file:
            audio_content = wav_file.read()

        result = analyze_audio(audio_content)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}