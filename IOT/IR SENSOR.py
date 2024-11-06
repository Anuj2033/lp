"""
THIS CODE HAS BEEN TESTED ON RASPBERRY PI 3B and 4B AND IS FULLY OPERATIONAL.

Problem Statement: IR Sensor

Code from InternetOfThingsAndEmbeddedSystems (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/InternetOfThingsAndEmbeddedSystems
"""

# BEGINNING OF CODE
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.IN) # For IR sensor
GPIO.setup(26,GPIO.OUT) # For LED

try: 
   while True:
      if (GPIO.input(16)):
          print("No object")
          GPIO.output(26,GPIO.LOW) # LED OFF when no object detected
      else:
          print("Object Detected")
          GPIO.output(26,GPIO.HIGH) # LED ON when object detected
except KeyboardInterrupt:
    GPIO.cleanup()
# END OF CODE
