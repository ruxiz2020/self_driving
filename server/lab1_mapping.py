import time
from Led import *
from Motor import *
from Ultrasonic import *
from Line_Tracking import *
from servo import *
from ADC import *
from Buzzer import *
from Thread import *
#from threading import Thread


led = Led()
PWM = Motor()
ultrasonic = Ultrasonic()
line = Line_Tracking()
pwm = Servo()
adc = Adc()
buzzer = Buzzer()


def mapping():

    try:
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

            for i in range(2180, 60, -1):
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

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print ('Mapping is starting ...')
    import sys

    mapping()
