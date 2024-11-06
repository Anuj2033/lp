"""
THIS CODE HAS BEEN TESTED ON RASPBERRY PI 3B, 4B AND IS FULLY OPERATIONAL.

Problem Statement: Temperature and humidity sensing using DHT11.

Code from InternetOfThingsAndEmbeddedSystems (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/InternetOfThingsAndEmbeddedSystems
"""

# NOTE: PLEASE REFER DHT11 repo by notkshitij for initialization: https://git.kska.io/notkshitij/DHT11/

# This code will only work in the virtual environment
# To enable the virtual environment, change current working directory using 'cd <DIR>'
# Activate the virtual environment using 'source bin/activate'
# Run this code 'python3 IoT\ -\ Code-4.py'

# BEGINNING OF CODE
# NOTE: GPIO PIN 16 used

import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Set True if you are having trouble connecting the DHT11 sensor to Raspberry Pi. Doing so will show warnings on screen.

try:
  while True:
    # read data using pin 16
    instance = dht11.DHT11(pin = 16)
    result = instance.read()

    if result.is_valid():
      print("Temperature: %-3.1f C" % result.temperature)
      print("Humidity: %-3.1f %%" % result.humidity)
    else:
      print("Error: %d" % result.error_code)
      # Error 1 implies sensor not detected, thus no data 
      # Error 2 implies checksum error, data corrupted, i.e. GPIO connection might be lose
    time.sleep(3)
except KeyboardInterrupt:
  print("Program stopped by user.")
  GPIO.cleanup()
# END OF CODE
