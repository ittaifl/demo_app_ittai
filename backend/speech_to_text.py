from google.cloud import speech
from pydub import AudioSegment
import io

def analyze_audio(audio_content):
    # Load audio to pydub
    audio = AudioSegment.from_file(io.BytesIO(audio_content), format="wav")
    audio = audio.set_sample_width(2)  # Set bit depth to 16 bits

    # Save the audio to a new file
    audio.export("audio_16bit.wav", format="wav")

    # Then read this new file
    with open("audio_16bit.wav", 'rb') as audio_file:
        audio_content = audio_file.read()

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="he-IL",
        audio_channel_count=2,
    )

    try:
        response = client.recognize(config=config, audio=audio)
        print("Google Speech-to-Text API response: ", response)

        for result in response.results:
            print("Transcript: ", result.alternatives[0].transcript)
            if "לחזור" in result.alternatives[0].transcript.lower():
                return True
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
