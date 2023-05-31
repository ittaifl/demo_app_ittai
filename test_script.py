from google.cloud import speech
import os
print(os.environ['PATH'])
def analyze_audio(file_path):
    with open(file_path, 'rb') as audio_file:
        audio_content = audio_file.read()

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="en-US",
        audio_channel_count=2,
    )

    try:
        response = client.recognize(config=config, audio=audio)
        print("Google Speech-to-Text API response: ", response)

        for result in response.results:
            print("Transcript: ", result.alternatives[0].transcript)
            if "hello" in result.alternatives[0].transcript.lower():
                return True
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

# Set the environment variable
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Lenovo\Downloads\deom-for-interview-b0a1bb996236.json'

# Call the function with the path to your audio file
analyze_audio('C:\\Users\\Lenovo\\my-app\\audio1.wav')
