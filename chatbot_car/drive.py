import time
from .. / server / Led import *
from .. / server / Motor import *
from .. / server / Ultrasonic import *
from .. / server / Line_Tracking import *
from .. / server / servo import *
from .. / server / ADC import *
from .. / server / Buzzer import *
from .. / server / Thread import *
#from threading import Thread


led = Led()
PWM = Motor()
ultrasonic = Ultrasonic()
line = Line_Tracking()
pwm = Servo()
adc = Adc()
buzzer = Buzzer()


def run():

    try:
        while True:
            arr_dist = []
            for i in range(60, 120, 2):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)

                # buzzer.run('0')

                data_dist = ultrasonic.get_distance()  # Get the distance value
                #print ("When servo is at "+str(i)+" degree")
                #print ("Obstacle distance is "+str(data)+" CM")
                arr_dist.append((i, data_dist))
                print(arr_dist)

                PWM.setMotorModel(600, 600, 600, 600)  # Forward
                print("The car is moving forward")

                if (i < 90) & (data_dist < 25):  # obstacle on the left
                    PWM.setMotorModel(1200, 1200, -800, -800)  # turn right
                    time.sleep(1)
                    # PWM.setMotorModel(-1500,-1500,1500,1500) # turn Left
                    # print("STOPPING!")
                    # PWM.setMotorModel(0,0,0,0)
                elif (i >= 90) & (data_dist < 25):  # obstacle on the left
                    PWM.setMotorModel(-800, -800, 1200, 1200)  # turn Left
                    time.sleep(1)
                    # PWM.setMotorModel(1500,1500,-1500,-1500) # turn right
                elif (data_dist < 10):  # obstacle in front
                    PWM.setMotorModel(0, 0, 0, 0)  # stop
                    time.sleep(20)
                else:
                    PWM.setMotorModel(600, 600, 600, 600)  # Forward
                    print("The car is moving forward")

    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nEnd of program")


# Main program logic follows:
if __name__ == '__main__':

    print('Car is starting ...')
    import sys

    run()
