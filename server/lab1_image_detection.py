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
#from detect import *



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
            for i in range(20, 120, 2):
                pwm.setServoPwm('0', i)
                time.sleep(0.01)

                PWM.setMotorModel(400,400,400,400) #Forward
                print ("The car is moving forward")

                data_dist=ultrasonic.get_distance()   #Get the distance value
                if (data_dist < 20):
                    PWM.setMotorModel(0,0,0,0) # stop
                    time.sleep(1)
                    camera.capture('sign.jpg') # take picture
                    #detections = run_detection(model='efficientdet_lite0.tflite',
                    #                            camera_id=0,height=480,width=640,
                    #                            num_threads=4,enable_edgetpu=False) # object detection
                    #print(detections)

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
