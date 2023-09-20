from tkinter import*
import speech_recognition as sr
import pyttsx3
from datetime import datetime


root=Tk()
root.geometry("500x500")

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How can i help you...?")
    speech_recogniser= sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recogniser.listen(source)
        voice_data=''
        try:
            voice_data= speech_recogniser.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('please repeat i did not get that')
            speak("please report i did not get that")
    
    respond(voice_data)        
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Jayantika")
        print('My name is Jayantika')
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = nowstrftime("%H:%M:%S")
        speak(current_time)
        
r_audio()

root.mainloop()        