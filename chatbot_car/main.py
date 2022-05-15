import time
from PCA9685 import PCA9685
from servo import Servo
from Motor import *


pwm = Servo()

def test_Servo():
    try:
        while True:
            for i in range(50, 110, 1):
                pwm.setServoPwm('0', i)
                time.sleep(0.05)
            for i in range(110, 50, -1):
                pwm.setServoPwm('0', i)
                time.sleep(0.05)
            for i in range(80, 150, 1):
                pwm.setServoPwm('1', i)
                time.sleep(0.05)
            for i in range(150, 80, -1):
                pwm.setServoPwm('1', i)
                time.sleep(0.05)
    except KeyboardInterrupt:
        pwm.setServoPwm('0', 90)
        pwm.setServoPwm('1', 90)
        print("\nEnd of program")


if __name__ == '__main__':
    test_Servo()


def main():

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

                PWM.setMotorModel(400,400,400,400) #Forward
                print ("The car is moving forward")

                if (i < 90) & (data_dist < 25): # obstacle on the left
                    PWM.setMotorModel(1200,1200,-800,-800) # turn right
                    time.sleep(1)
                    #PWM.setMotorModel(-1500,-1500,1500,1500) # turn Left
                    #print("STOPPING!")
                    #PWM.setMotorModel(0,0,0,0)
                elif (i >= 90) & (data_dist < 25): # obstacle on the left
                    PWM.setMotorModel(-800,-800,1200,1200) # turn Left
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

    print ('Car is starting ...')
    import sys

    run()
