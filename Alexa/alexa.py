import webbrowser
import time
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr
import threading


import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as source

playsound.playsound("my name is Omar")
with sr.Microphone() as source:
    print("Listening...")

    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)

    # Listen for audio and capture it in 'audio' variable
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

