import RPi.GPIO as GPIO
import time

button_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, GPIO.PUD_UP)

def my_callback(channel):
    button_status = GPIO.input(button_pin)   # Read button input and give the value to status
    if button_status == 1:                   # Check status value
        print "Button Released!"
    else:
        print "Button Pressed!"

# Define a edge detection
GPIO.add_event_detect(button_pin, GPIO.BOTH, my_callback, bouncetime=20)

while True:
    print "I'm so boring, nothing left to do."
    time.sleep(3)
