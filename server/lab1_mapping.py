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
ultrasonic = Ultrasonic()
line = Line_Tracking()
pwm = Servo()
adc = Adc()
buzzer = Buzzer()


def move_or_stop_according_to_detected_distance(distince_input, PWM):

    data=ultrasonic.get_distance()   #Get the distance value
    print ("When servo is at "+str(i)+" degree")
    print ("Obstacle distance is "+str(data)+" CM")

    if data < distince_input:
        print("STOPPING!")
        PWM.setMotorModel(0,0,0,0)
    else:
        PWM.setMotorModel(500,500,500,500) #Forward
        print ("The car is moving forward")


def mapping(distince_input):

    PWM = Motor()

    D = int(distince_input) # distince threshold for stopping

    while True:
        for i in range(40, 160, 1):
            pwm.setServoPwm('0', i)
            time.sleep(0.01)
            move_or_stop_according_to_detected_distance(D, PWM)

        for i in range(160,40,-1):
            pwm.setServoPwm('0',i)
            time.sleep(0.01)
            move_or_stop_according_to_detected_distance(D, PWM)

    #except KeyboardInterrupt:
    #    PWM.setMotorModel(0,0,0,0)
    #    print ("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print ('Mapping is starting ...')
    import sys

    try:
        dist = sys.argv[1]
        mapping(dist)
    except:
        print("Please input a distinct theshold for stopping!")
