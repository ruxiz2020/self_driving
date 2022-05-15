import time
from PCA9685 import PCA9685
from servo import Servo
from Motor import Motor
from Ultrasonic import Ultrasonic
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import speech_recognition as sr
from text_2_sound import text_2_sound
from audio_2_text import audio_2_text
from chat import chat_with_bot, tokenizer, model

PWM = Motor()
ultrasonic = Ultrasonic()
pwm = Servo()


servo_directions = [[50, 110, 1],
[110, 50, -1],
[80, 150, 1],
150, 80, -1]


def main(model, tokenizer):

    try:
        while True:
            for i in range(10):

                direction = servo_directions[i % 4]
                #print(direction)

                dist=ultrasonic.get_distance()   #Get the distance value
                print(dist)

                PWM.setMotorModel(400,400,400,400) #Forward
                print ("The car is moving forward")

                if (dist < 5):
                    PWM.setMotorModel(0,0,0,0) #Stop
                    print ("The car stopped")

                text_2_sound("hmmm ")

                listener = sr.Recognizer()
                # Following two lines are meant to fix error about ALSA
                listener.energy_threshold = 384
                listener.dynamic_energy_threshold = True

                input = None
                while input == None:
                    input = audio_2_text(listener)

                if input == 'come':
                    PWM.setMotorModel(400,400,400,400) #Forward
                    print ("The car is moving forward")

                chat_with_bot(input, model, tokenizer)

                # rotate head
                print("===direction===")
                print(direction)
                for ss in range(direction[0], direction[1], direction[2]):
                    pwm.setServoPwm('0', ss)
                    time.sleep(0.05)

    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print('Car is starting ...')

    main(model, tokenizer)
