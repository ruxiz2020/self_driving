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
            arr_dist = []
            for i in range(20, 120, 2):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)

                data_dist=ultrasonic.get_distance()   #Get the distance value
                #print ("When servo is at "+str(i)+" degree")
                #print ("Obstacle distance is "+str(data)+" CM")
                arr_dist.append((i, data_dist))
                print(arr_dist)

                if (i < 80) & (data_dist < 15): # obstacle on the left
                    PWM.setMotorModel(1000,1000,-1000,-1000) # turn right
                    time.sleep(1)
                    #PWM.setMotorModel(-1500,-1500,1500,1500) # turn Left
                    #print("STOPPING!")
                    #PWM.setMotorModel(0,0,0,0)
                elif (i >= 100) & (data_dist < 15): # obstacle on the left
                    PWM.setMotorModel(-1000,-1000,1000,1000) # turn Left
                    time.sleep(1)
                    #PWM.setMotorModel(1500,1500,-1500,-1500) # turn right
                #elif (data_dist < 5): # obstacle in front
                #    PWM.setMotorModel(-1000,-1000,-1000,-1000)   #Back
                #    print ("The car is going backwards")
                #    time.sleep(1)
                else:
                    PWM.setMotorModel(400,400,400,400) #Forward
                    print ("The car is moving forward")


    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print ('Mapping is starting ...')
    import sys

    mapping()
