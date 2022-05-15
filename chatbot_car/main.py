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
from explain_keyword import TextFromUrl, explain_2_me

PWM = Motor()
ultrasonic = Ultrasonic()
pwm = Servo()


servo_directions = [[50, 110, 1],
[110, 50, -1],
[80, 150, 1],
[150, 80, -1]]


def run():

    try:
        while True:
            arr_dist = []
            for i in range(60, 120, 2):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)

                #buzzer.run('0')

                data_dist=ultrasonic.get_distance()   #Get the distance value
                #print ("When servo is at "+str(i)+" degree")
                #print ("Obstacle distance is "+str(data)+" CM")
                arr_dist.append((i, data_dist))
                print(arr_dist)

                PWM.setMotorModel(600,600,600,600) #Forward
                print ("The car is moving forward")

                #if (i < 90) & (data_dist < 25): # obstacle on the left
                #    PWM.setMotorModel(1200,1200,-800,-800) # turn right
                #    time.sleep(1)
                    #PWM.setMotorModel(-1500,-1500,1500,1500) # turn Left
                    #print("STOPPING!")
                    #PWM.setMotorModel(0,0,0,0)
                #elif (i >= 90) & (data_dist < 25): # obstacle on the left
                #    PWM.setMotorModel(-800,-800,1200,1200) # turn Left
                #    time.sleep(1)
                    #PWM.setMotorModel(1500,1500,-1500,-1500) # turn right
                if (data_dist < 5): # obstacle in front
                    PWM.setMotorModel(0,0,0,0)   #Back
                    print ("The car is going backwards")
                    time.sleep(1)
                else:
                    PWM.setMotorModel(600,600,600,600) #Forward
                    print ("The car is moving forward")


    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


def main(model, tokenizer, run_model_flag = 'chat'):
    '''
    run_model_flag
        chat: chatbot for random topic chat
        explain: explain keyword by google search and read the top 1 article found
    '''

    try:
        run()
        for i in range(10):

            listener = sr.Recognizer()
            # Following two lines are meant to fix error about ALSA
            listener.energy_threshold = 384
            listener.dynamic_energy_threshold = True

            question = None
            while question == None:
                question = audio_2_text(listener)

            if run_model_flag == 'chat':
                chat_with_bot(question, model, tokenizer)

            if run_model_flag == 'explain':

                explain_2_me(question)

                with open('news.txt', 'r') as file:
                    data = file.read().replace('\n', ' ')
                print(data)

                text_2_sound(data[:2000])


    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print('Car is starting ...')

    main(model, tokenizer, 'explain')
