import speech_recognition as sr
import spacy
#from absl import app, flags, logging

import detect
r= sr.Recognizer()
mic = sr.Microphone()
data=[]
  
# python -m spacy download en_core_web_sm 
nlp = spacy.load("en_core_web_sm") 

def listen():
    text=''
    with mic as source:
        r.adjust_for_ambient_noise(source )
        audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said: " + text)
        return text

        #error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return 0

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return -1 


def tokenize():
    res=listen()
    if (res.lower() == "hey tuffy" or res.lower() == "hey duffy"):
        print("what do you want?")
        instruction = listen()
        #print(instruction)
        if (instruction != 0 or instruction != -1):
            doc = nlp(instruction)
            #print(doc)
            # Token and Tag 
            for token in doc: 
                #print(token, token.pos_) 
                if token.pos_ == "VERB":
                    action= token.text
                    if action != 1:
                        print("Action: " + action)
                
                if token.pos_ == "ADJ":
                    adj= token.text
                    if adj != 1:
                        print("Adjective: " + adj)
                    
                if token.pos_ == "NOUN":
                    obj= token.text
                    if obj != 1:
                        print("Object: " + obj)
        else:
            print("instruction not understood")
            return 0
    else:
        print("not an instruction")
        return 0

def main():
    tokenize()
