import time
from Led import *
from Motor import *
from Ultrasonic import *
from Line_Tracking import *
from servo import *
from ADC import *
from Buzzer import *
from Thread import *
from threading import Thread


led=Led()
PWM=Motor()
ultrasonic=Ultrasonic()
line=Line_Tracking()
pwm=Servo()
adc=Adc()
buzzer=Buzzer()


def rotate_Servo():
    try:
        while True:
            for i in range(60,180,1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(180,60,-1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            #for i in range(80,150,1):
            #    pwm.setServoPwm('1',i)
            #    time.sleep(0.01)
            #for i in range(150,80,-1):
            #    pwm.setServoPwm('1',i)
            #    time.sleep(0.01)
    except KeyboardInterrupt:
        pwm.setServoPwm('0',90)
        pwm.setServoPwm('1',90)
        print ("\nEnd of program")


def forward():
    try:
        PWM.setMotorModel(500,500,500,500)       #Forward
        print ("The car is moving forward")
        #time.sleep(1)
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")

def main():

    servo_action = Thread(target=rotate_Servo)
    forward_action = Thread(target=forward)

    servo_action.start()
    forward_action.start()

    data=ultrasonic.get_distance()   #Get the distance value
    print ("Obstacle distance is "+str(data)+"CM")
    if data < 100:
        stop_thread(forward_action)



# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys

    if sys.argv[1] == 'Forward':
        main()
