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


def move_or_stop_according_to_detected_distance(degree, distince_input, PWM):

    data=ultrasonic.get_distance()   #Get the distance value
    print ("When servo is at "+str(degree)+" degree")
    print ("Obstacle distance is "+str(data)+" CM")

    if data < distince_input:
        print("STOPPING!")
        PWM.setMotorModel(0,0,0,0)
    else:
        PWM.setMotorModel(500,500,500,500) #Forward
        print ("The car is moving forward")

    return (degree, data)


def mapping(distince_input):

    PWM = Motor()

    D = int(distince_input) # distince threshold for stopping

    while True:
        array_distances = []
        for i in range(40, 160, 1):
            pwm.setServoPwm('0', i)
            time.sleep(0.01)
            (degree, dist) = move_or_stop_according_to_detected_distance(i, D, PWM)
            array_distances.append(degree, dist)

        for i in range(160, 40, -1):
            pwm.setServoPwm('0', i)
            time.sleep(0.01)
            (degree, dist) = move_or_stop_according_to_detected_distance(i, D, PWM)
            array_distances.append(degree, dist)
        print(array_distances)

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
        print(sys.argv[1])
        print("Please input a distinct theshold for stopping!")
