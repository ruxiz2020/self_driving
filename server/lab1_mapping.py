import time
from Led import *
from Motor import *
from Ultrasonic import *
from Line_Tracking import *
from servo import *
from ADC import *
from Buzzer import *
from astar_search import *
from Thread import *
#from threading import Thread
import math
import cmath


led = Led()
PWM = Motor()
ultrasonic = Ultrasonic()
line = Line_Tracking()
pwm = Servo()
adc = Adc()
buzzer = Buzzer()





def convert_angle_dist_2_coord(angle, dist):
    '''
    This function converts ultrasonic data
    into coordinates x, y
    '''
    r = angle * math.pi / 180
    y = math.sin(r) * dist
    x = math.sqrt(dist ** 2 - y ** 2)

    if angle < 90:
        x = abs(x) * -1
    return int(x), int(y)


def create_matrix_input_for_astar_algo(arr_coordinates):
    '''
    This function converts coordinates matrix into binary matrix
    as the input data of A* algorithm
    '''

    M = [[0 for col in range(11)] for row in range(11)] # matrix of size 11 * 11
    for (x, y) in arr_coordinates:
        if (x + 5 >= 0) & (x + 5 <= 10) & (y >= 0) & (y < 10): # leave the furthest line all zero
            M[y][x + 50] = 1
    return M




def mapping():

    try:
        while True:
            arr_dist = []
            for i in range(20, 120, 2):
                pwm.setServoPwm('0', i)
                #time.sleep(0.01)

                data_dist=ultrasonic.get_distance()   #Get the distance value
                #print ("When servo is at "+str(i)+" degree")
                #print ("Obstacle distance is "+str(data)+" CM")
                arr_dist.append((data_dist, i))
                #print(arr_dist)
                if len(arr_dist) > 10:
                    PWM.setMotorModel(0,0,0,0)
                    #time.sleep(1)
                    arr_coordinates = [convert_angle_dist_2_coord(x, y) for x, y in arr_dist]
                    map = create_matrix_input_for_astar_algo(arr_coordinates)


                    if sum(sum(map,[])) > 0:
                        start = [50, 0] # starting position
                        end = [50, 100] # ending position
                        cost = 1 # cost per movement
                        print(map)

                        path, directions = aster_search(map, cost, start, end)

                        print(directions)

                        for d in directions:
                            if d == 'F':
                                PWM.setMotorModel(400,400,400,400) #Forward
                                time.sleep(1)
                            if d == 'L':
                                PWM.setMotorModel(-800,-800,1000,1000) # turn Left
                                time.sleep(1)
                            if d == 'R':
                                PWM.setMotorModel(1000,1000,-800,-800) # turn right
                                time.sleep(1)

                PWM.setMotorModel(400,400,400,400) #Forward
                print ("The car is moving forward")

                if (i < 90) & (data_dist < 20): # obstacle on the left
                    PWM.setMotorModel(1000,1000,-500,-500) # turn right
                    time.sleep(1)
                    #PWM.setMotorModel(-1500,-1500,1500,1500) # turn Left
                    #print("STOPPING!")
                    #PWM.setMotorModel(0,0,0,0)
                elif (i >= 90) & (data_dist < 20): # obstacle on the left
                    PWM.setMotorModel(-500,-500,1000,1000) # turn Left
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
