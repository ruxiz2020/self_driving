import speech_recognition as sr
from audio_2_text import audio_2_text

from Motor import *
PWM=Motor()


def forward():
    try:
        PWM.setMotorModel(600,600,600,600)       #Forward
        print ("The car is moving forward")
        time.sleep(1)

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def stop():
    try:
        PWM.setMotorModel(0,0,0,0)                   #Stop
        print ("\nEnd of program")
        time.sleep(1)

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def command_2_mode():

        listener = sr.Recognizer()
        # Following two lines are meant to fix error about ALSA
        listener.energy_threshold = 384
        listener.dynamic_energy_threshold = True

        command = None
        while command == None:
            command = audio_2_text(listener)

        if command == 'come':
            forward()
        if command == 'stop':
            stop()
