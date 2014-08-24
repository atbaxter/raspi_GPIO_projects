### Import GPIO input map and time modules
import RPi.GPIO as GPIO
import time

##Set it up to use the GPIO board
GPIO.setmode(GPIO.BOARD)

## Use pin 18 as our output
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

## Turn on

GPIO.output(16,0)
GPIO.output(12,0)
GPIO.output(12,1)

## Wait a couple seconds
time.sleep(3)

GPIO.output(12,0)

time.sleep(1)

GPIO.output(12,1)

time.sleep(1)

GPIO.output(12,0)
GPIO.output(16,1)

time.sleep(2)


## End program
GPIO.cleanup()
