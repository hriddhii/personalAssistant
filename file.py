# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:25:13 2020
This code is Specific to Windows Only
@author: Hriddhi
"""

"""
This is My First Attempt At Making a Voice Assistant 
Let's see how far we can go
"""
import speech_recognition
import datetime
import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def weather():
    res=requests.get('https://ipinfo.io/')
    data=res.json()
    city=data['city']
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=281fb18bbaf599aca140694edf28d926&units=metric'.format(city)
    response=requests.get(url)
    data=response.json()
    temperature=data['main']['temp']
    speak("Currently it is")
    speak(temperature)
    speak("degree Celcius in")
    speak(city)

def listen():
    r = speech_recognition.Recognizer()
     with speech_recognition.Microphone() as source:
        print("Talk to me")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    else:
        speak("Good Evening")

if __name__ == '__main__':
    speak("Hello")
    wishMe()
    listen()
    command=listen().lower
    if 'weather' in command:
        weather()
