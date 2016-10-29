import RPi.GPIO as GPIO
import time

led_pin = 17
on_delay = 0.5
off_delay = on_delay
freq = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
p = GPIO.PWM(led_pin, freq)
p.start(0)

def set_led_value(value):    # Define a function 
    p.ChangeDutyCycle(100-value)

while True:
    set_led_value(50)        # use our function to set led value to 50
    time.sleep(on_delay)
    set_led_value(10)        # use our function to set led value to 10
    time.sleep(off_delay)
