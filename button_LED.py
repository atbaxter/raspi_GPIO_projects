import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

GPIO.setup(25, GPIO.OUT)
GPIO.output(25, 0)

try:
    while True:
        GPIO.output(25, GPIO.input(23))

except KeyboardInterrupt:
    GPIO.cleanup()

    
