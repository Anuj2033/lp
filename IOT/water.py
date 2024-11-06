import RPi.GPIO as GPIO
import time


while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN)
    GPIO.setup(16, GPIO.OUT)
    if GPIO.input(26):
        print('Obstacle not detected')
        GPIO.output(16,1)
        time.sleep(0.10)
    else:
        print("Obstacle detected")
        GPIO.output(16,0)
        time.sleep(0.10)

       