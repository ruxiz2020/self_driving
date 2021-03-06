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

from picamera import PiCamera
from time import sleep
#camera = PiCamera()
from detect import *



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
            for i in range(30, 140, 2):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)

                PWM.setMotorModel(400,400,400,400) #Forward
                print ("The car is moving forward")

                data_dist=ultrasonic.get_distance()   #Get the distance value
                if (data_dist < 20):
                    PWM.setMotorModel(0,0,0,0) # stop
                    time.sleep(0.1)
                    #camera.capture('sign.jpg') # take picture

                    # The following line is a hack to use the detection output of
                    # calling object detection from tensorflow, but it is buggy,
                    # It runs but there is lots of warning complaining about GStream (no time to fix)
                    detections = run_detection(model='efficientdet_lite0.tflite',
                                                camera_id=0,height=480,width=640,
                                                num_threads=4,enable_edgetpu=False) # object detection
                    print(detections)
                    detect_results = [d[1][0][0] for d in detections]
                    if any('stop' in item for item in detect_results): # check if any of the detection label contains stop
                        PWM.setMotorModel(0,0,0,0) # stop
                        time.sleep(1)
                        PWM.setMotorModel(1000,1000,-500,-500) # turn right
                        time.sleep(1)

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
