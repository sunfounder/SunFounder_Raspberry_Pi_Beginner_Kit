import RPi.GPIO as GPIO

button_pin = 18           # Connect button at 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, GPIO.PUD_UP) # Set button as input and pull up

while True:
    button_status = GPIO.input(button_pin)   # Read button input and give the value to status
    if button_status == 1:                   # Check status value
        print "Button Released!"
    else:
        print "Button Pressed!"
