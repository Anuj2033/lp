# NOTE: GPIO PIN 16 used

import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False) # Set True if you are having trouble connecting the DHT11 sensor to Raspberry Pi. Doing so will show warnings on screen.
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

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
    time.sleep(3)
except KeyboardInterrupt:
  print("Program stopped by user.")
  GPIO.cleanup()
