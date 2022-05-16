import speech_recognition as sr
import time
from audio_2_text import audio_2_text

from Ultrasonic import Ultrasonic
from Motor import Motor
PWM=Motor()
ultrasonic = Ultrasonic()

def forward(data_dist):
    global PWM
    try:
        PWM.setMotorModel(700,700,700,700)       #Forward
        print ("The car is moving forward")
        time.sleep(4)

        if data_dist < 1:
            PWM.setMotorModel(0,0,0,0)
            time.sleep(1)

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def left(data_dist):
    global PWM
    try:
        PWM.setMotorModel(-1500,-1500,2000,2000)       #Left
        print ("The car is turning left")
        time.sleep(3)

        if data_dist < 1:
            PWM.setMotorModel(0,0,0,0)
            time.sleep(1)

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def right(data_dist):
    global PWM
    try:
        PWM.setMotorModel(2000,2000,-1500,-1500)       #Right
        print ("The car is turning right")
        time.sleep(3)

        if data_dist < 1:
            PWM.setMotorModel(0,0,0,0)
            time.sleep(1)

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def stop(data_dist):
    global PWM
    try:
        PWM.setMotorModel(0,0,0,0)                   #Stop
        print ("\nEnd of program")
        time.sleep(1)

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def command_2_mode(PWM):

    for i in range(10):

        listener = sr.Recognizer()
        # Following two lines are meant to fix error about ALSA
        listener.energy_threshold = 384
        listener.dynamic_energy_threshold = True

        command = None
        while command == None:
            command = audio_2_text(listener)
        print(command)

        data_dist=ultrasonic.get_distance()   #Get the distance value
        print(data_dist)


        if command == 'come':
            forward(data_dist)
        elif command == 'left':
            left(data_dist)
        elif command == 'right':
            right(data_dist)
        elif command == 'stop':
            stop(data_dist)


if __name__=='__main__':
    command_2_mode(PWM)
