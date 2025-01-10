import speech_recognition as sr
from google.colab import files

# SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Upload audio file
print("Please upload a WAV audio file:")
uploaded = files.upload()  # Choose your file (e.g., 'example.wav')

# Get the uploaded file name
audio_file = list(uploaded.keys())[0]

# Load and recognize the audio
with sr.AudioFile(audio_file) as source:
    print("Processing the audio file...")
    audio_data = recognizer.record(source)  # Read the entire audio file
    try:
        # Perform speech-to-text
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio_data, language="en-US")
        print(f"Recognized Text: {text}")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results; please check your internet connection.")
