#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:30:02 2020

@author: Chamroukhi
"""
import speech_recognition as sr 
import playsound 
from gtts import gTTS #google text to speech
import random
import webbrowser # ouvrir naviguateur
import time
import os # supprimer les fichiers audio

class person:
    name = 'Naoufel'
    def setName(self, name):
        self.name = name

def there_exists(terms):# verifier si le terme dans la sequence de parole ou non 
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            #speak('What you say Naoufel')
            #time.sleep(1)
            a=1
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string,langue):
    tts = gTTS(text=audio_string, lang=langue) # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Julia: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    if there_exists(['hello julia','hello']):
        greetings = [f"Good morning {person_obj.name}",f"Hi {person_obj.name}",f"Hey {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet, 'en')
    
    if there_exists(['introduce yourself','who are you','introduce','yourself']):
        speak("okay ,I am Naoufel speech assistant ,He created me using, speech recognition,and google Text To Speech ,Python library. And I am here ,to help you present the article, I am very happy to be with you, in this meeting",'en')
     
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Julia",'en')
        else:
            speak("my name is Julia. what's your name?",'en')

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}",'en')
        person_obj.setName(person_name) # remember name in person object
   
        
    if there_exists(['okay you can start','you can start','you can','can start']):
        speak("ok, donc je commence, par présenter l'article, cet article , est créer , en 2016, par",'fr')
        speak("Du Guiming , Wang Xia , Wang Guangyan , Zhang Yan , Li Dan",'en')
        speak("et il est, composé de 4 page, le sujet de cet article est, reconnaissance automatique, de parole, en utilisant, un réseaux de neurones convolutif, les principeaux mots, importante sont: ",'fr')
        speak("speech recognition, convolution neural network, back propagation",'en')
        speak("Dans cet article, les auteurs utilise, le MFCC et le CNN ,pour classifier ,les mots isolées ,de sont propre base d'apprentissage, sans tombe dans le cas de sur-apprentissage.",'fr')
        speak("Maintenant je vous laisse, avec Naoufel pour le reste de présentation","fr")

    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking",'en')
        
    
    if there_exists(["thank you julia","thanks","thank you"]):
        thanks = [f"Welcome, I'm here to help you",f"Welcome, I'm here to help you"]
        thank = thanks[random.randint(0,len(thanks)-1)]
        speak(thank,'en')
        
    

    # search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google','en')

    # search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube','en')

    
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline",'en')
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond


