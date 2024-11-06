: '
THIS CODE HAS BEEN TESTED ON RASPBERRY PI 3B, 4B AND IS FULLY OPERATIONAL.

Problem Statement: Picamera

Code from InternetOfThingsAndEmbeddedSystems (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/InternetOfThingsAndEmbeddedSystems
'

# BEGINNING OF CODE

# Run these command one by one manually in the terminal.
# Image and video file will be saved in Desktop directory of the cuurent user.

cd /home/$(whoami)/Desktop/ # Changing current working directory to Desktop
raspicam-still -o test.jpg # Image
libcamera-vid --codec h254 vid.h264

# END OF CODE

