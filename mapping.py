import time
from control.Led import *
from control.Motor import *
from control.Ultrasonic import *
from control.Line_Tracking import *
from control.servo import *
from control.ADC import *
from control.Buzzer import *
from control.Thread import *
from control.threading import Thread


led = Led()
PWM = Motor()
ultrasonic = Ultrasonic()
line = Line_Tracking()
pwm = Servo()
adc = Adc()
buzzer = Buzzer()


def mapping():

    while True:
        for i in range(60, 180, 1):
            pwm.setServoPwm('0', i)
            time.sleep(0.01)

            data=ultrasonic.get_distance()   #Get the distance value
            print ("When servo is at "+str(i)+" degree")
            print ("Obstacle distance is "+str(data)+" CM")

            if data < 50:
                print("STOPPING!")
                PWM.setMotorModel(0,0,0,0)
            else:
                PWM.setMotorModel(500,500,500,500) #Forward
                print ("The car is moving forward")


# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys

    if sys.argv[1] == 'Mapping is starting ...':
        mapping()
