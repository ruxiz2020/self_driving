import time
from PCA9685 import PCA9685
from servo import Servo
from Motor import Motor
from Ultrasonic import Ultrasonic
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import speech_recognition as sr
from text_2_sound import text_2_sound
from audio_2_text import audio_2_text
from chat import q_n_a

PWM = Motor()
ultrasonic = Ultrasonic()
pwm = Servo()


# Transformer model for chat bot conversation
# model_name = "microsoft/DialoGPT-large"
# model_name = "microsoft/DialoGPT-medium"
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

text_2_sound("Hi dear, let us start a conversation!")




def main(model, tokenizer):

    try:
        while True:
            distance = ultrasonic.get_distance()

            if (distance < 10): # obstacle in front
                PWM.setMotorModel(0,0,0,0)   #stop
                print ("Stop moving")
                time.sleep(1)

            # listening to conversation input
            listener = sr.Recognizer()
            # Following two lines are meant to fix error about ALSA
            listener.energy_threshold = 384
            listener.dynamic_energy_threshold = True

            question = None
            while question == None:
                question = audio_2_text(listener)

            # move head around
            for i in range(50, 110, 1):
                pwm.setServoPwm('0', i)
                time.sleep(0.05)
                q_n_a(question, model, tokenizer)


            question = None
            while question == None:
                question = audio_2_text(listener)

            # move head around
            for i in range(110, 50, -1):
                pwm.setServoPwm('0', i)
                time.sleep(0.05)
                q_n_a(question, model, tokenizer)

            question = None
            while question == None:
                question = audio_2_text(listener)

            # move head around
            for i in range(80, 150, 1):
                pwm.setServoPwm('1', i)
                time.sleep(0.05)
                q_n_a(question, model, tokenizer)

            question = None
            while question == None:
                question = audio_2_text(listener)
            # move head around
            for i in range(150, 80, -1):
                pwm.setServoPwm('1', i)
                time.sleep(0.05)
                q_n_a(question, model, tokenizer)

    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print('Car is starting ...')

    main(model, tokenizer)
