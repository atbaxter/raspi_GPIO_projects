# import all necessary modules
import RPi.GPIO as GPIO
import time

# set to use pin values, not physical location
GPIO.setmode(GPIO.BCM)

# assign pin values
TRIG = 24
ECHO = 23
ALARM_PIE = 18
ALARM_LED = 22
GO = 17

# set up all pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(TRIG,0)

GPIO.setup(ALARM_LED, GPIO.OUT)
GPIO.setup(ALARM_LED, 0)

GPIO.setup(ALARM_PIE, GPIO.OUT)
GPIO.setup(ALARM_PIE, 0)

GPIO.setup(GO, GPIO.OUT)
GPIO.setup(GO, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)

# print a phrase marking the beginning of a program
print("Starting Measurement...")

#set up try-except so keyboard interrupt can stop program
try:

    #loop indefinitely
    while True:

        # send signal to ultrasonic sensor            
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)

        # start timing
        while GPIO.input(ECHO) == 0:
            pass
        start = time.time()

        # stop timing
        while GPIO.input(ECHO) == 1:
            pass
        stop = time.time()

        # equation to calculate distance
        d = (stop-start) * 17000

        # print distance
        print (d)

        # if-else loop to either display red or green LEDs
        if d < 100:
            GPIO.output(ALARM_LED, 1)
            GPIO.output(ALARM_PIE, 1)
            time.sleep(0.99)
            GPIO.output(ALARM_LED, 0)
            GPIO.output(ALARM_PIE, 0)
        else:
            GPIO.output(GO, 1)
            time.sleep(0.99)
            GPIO.output(GO, 0)

# CNTRL-C to end program
except KeyboardInterrupt:
    GPIO.cleanup()
