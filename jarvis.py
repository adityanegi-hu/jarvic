import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
from reportlab.pdfgen import canvas

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(" WELCOME SIR, HOW CAN I HELP YOU?")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that")
            return ""
        except sr.RequestError:
            speak("Could not request results")
            return ""

while True:
    command = take_command()
    
    if "open youtube" in command:
        speak("Opening YouTube")
        pywhatkit.playonyt("youtube")
    
    elif "open google" in command:
        speak("Opening Google")
        os.system("start chrome")
    
    elif "open WhatsApp" in command:
        speak("Opening WhatsApp")
        os.system("start WhatsApp")
    
    elif "stop jarvis" in command:
        speak("Goodbye")
        break