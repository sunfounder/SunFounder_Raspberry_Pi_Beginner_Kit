import RPi.GPIO as GPIO
import time

led_pin = 17
delay = 0.01                 # delay for LED breathing speed
freq = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
p = GPIO.PWM(led_pin, freq)
p.start(0)

def set_led_value(value):
    p.ChangeDutyCycle(100-value)

while True:
    for i in range(0, 101):   # Loop "i" from 0 to 100
        set_led_value(i)      # Set led value to i
        time.sleep(delay)     # delay for LED breathing speed
    
    for i in range(100, -1, -1):   # Loop "i" from 100 to 0
        set_led_value(i)      # Set led value to i
        time.sleep(delay)     # delay for LED breathing speed
