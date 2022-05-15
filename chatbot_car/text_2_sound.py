# Import the required module for text
# to speech conversion
from gtts import gTTS
#import pyttsx3


# This module is imported so that we can
# play the converted audio
import os

from pygame import mixer
import playsound
from time import sleep

def playText(sound_file):

    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    print("Finished playing sound file")
    #playsound.playsound(sound_file, False)
    mixer.music.stop()
    mixer.quit()
    #exit()


def text_2_sound(text):
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    #engine = pyttsx3.init() # object creation
    #""" RATE"""
    #rate = engine.getProperty('rate')   # getting details of current speaking rate
    #print (rate)                        #printing current voice rate
    #engine.setProperty('rate', 40)     # setting up new voice rate

    #"""VOLUME"""
    #volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    #print (volume)                          #printing current volume level
    #engine.setProperty('volume', 0.5)    # setting up volume level  between 0 and 1

    #"""VOICE"""
    #voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    #engine.setProperty('voice', voices[28].id)   #changing index, changes voices. 1 for female

    #engine.say(text)
    #engine.say('My current speaking rate is ' + str(rate))
    #engine.runAndWait()
    #engine.stop()

    #"""Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    #engine.save_to_file(text, 'read.mp3')
    #engine.runAndWait()

    # saving the converted audio in a mp3 file
    myobj.save("read.mp3")

    # Playing the converted file
    #os.system("mpg321 read.mp3")
    playText("read.mp3")
