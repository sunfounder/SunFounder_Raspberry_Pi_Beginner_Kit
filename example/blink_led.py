import RPi.GPIO as GPIO
import time

led_pin = 17
delay = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    GPIO.output(led_pin, GPIO.LOW)       # LED ON
    time.sleep(delay)                    # Sleep "delay" second
    GPIO.output(led_pin, GPIO.HIGH)      # LED OFF
    time.sleep(delay)                    # Sleep "delay" second
