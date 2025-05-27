import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import speech_recognition as sr
import time
from playsound import playsound 
from translate import Translator
import os
from gtts import gTTS
import cv2


global translation11,translation1

TTS = gTTS(text='Welcome to your Blind Email Registration   Speak Your First name')
TTS.save("voice.mp3")
os.system("voice.mp3")
try:
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print("Username is:"+text)
        translator= Translator(from_lang="English",to_lang="English")
        translation1 = translator.translate(text)
        print(translation1)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)
    TTS = gTTS(text='Speak Your last name')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print("Last Name is:"+text)
        translator= Translator(from_lang="English",to_lang="English")
        translation1 = translator.translate(text)
        print(translation1)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)
    TTS = gTTS(text='please Said User name')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print("Username is:"+text)
        translator= Translator(from_lang="English",to_lang="English")
        translation1 = translator.translate(text)
        print(translation1)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)
        
    TTS = gTTS(text='please enter your user id ...for example 1 2 3')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        # convert speech to text
        global id
        id = str(id)
    
        id = r.recognize_google(audio_data)
        print("User id is:"+id)
        translator= Translator(from_lang="English",to_lang="English")
        translation1 = translator.translate(id)
        print(translation1)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)
    TTS = gTTS(text='You want to capture your photo')     
        
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:        
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print(audio_data)
        
                  
    print("Recognizing...")
        # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    if  text == 'yes': 
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
        cap = cv2.VideoCapture(0)
            
        #id = input('enter user id')
        #global id
        
        sampleN=0;
         
        while 1:
            
              ret, img = cap.read()
            
              gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
              faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
              for (x,y,w,h) in faces:
            
                    sampleN=sampleN+1;
            
                    cv2.imwrite("Image/User."+ str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
            
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
                    cv2.waitKey(100)
            
              cv2.imshow('img',img)
            
              cv2.waitKey(1)
            
              if sampleN > 40:
            
                   break
            
        cap.release()
            #entry2.delete(0,'end')
        cv2.destroyAllWindows()
    
     
            # from subprocess import call
            # call(["python", "demo camera.py"]) 
    
        
    print("capture your photo Sucessfully:"+text)
    translator= Translator(from_lang="English",to_lang="English")
    translation1 = translator.translate(text)
    print(translation1)
    TTS = gTTS(text=translation1)
    TTS.save("voice.mp3")
    os.system("voice.mp3")
       
    time.sleep(3)   
    TTS = gTTS(text='You Want to Train Your Photo')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        
        # convert speech to text
        text = r.recognize_google(audio_data)
        #text = r.recognize_google(audio_data)
        if  text == 'yes': 
     
            from subprocess import call
            call(["python", "train.py"]) 
    
        print("Username is:"+text)
        translator= Translator(from_lang="English",to_lang="English")
        translation1 = translator.translate(text)
        print(translation1)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)
    
    TTS = gTTS(text='Registration Successfully....Registration Successfully......Welcome to Login Page')     
        
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    from subprocess import call
    call(["python", "face_login.py"]) 
    r = sr.Recognizer()


except sr.UnknownValueError: 
    TTS = gTTS(text='Google Speech Recognition could not understand audio.')
    TTS.save("voice1.mp3")
    os.system("voice1.mp3")
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    TTS = gTTS(text='Could not request results from Google Speech Recognition service; {0}".format(e)')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
