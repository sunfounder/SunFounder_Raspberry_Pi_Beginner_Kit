import RPi.GPIO as GPIO
import time

r_pin = 17
g_pin = 18
b_pin = 27
freq = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(g_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
r_p = GPIO.PWM(r_pin, freq)
g_p = GPIO.PWM(g_pin, freq)
b_p = GPIO.PWM(b_pin, freq)
r_p.start(0)
g_p.start(0)
b_p.start(0)

# Add a map value function
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# map the value before output to ChangeDutyCycle
def set_color(r_value, g_value, b_value):
    r_p.ChangeDutyCycle(map_value(r_value,0,255,0,100))
    g_p.ChangeDutyCycle(map_value(g_value,0,255,0,100))
    b_p.ChangeDutyCycle(map_value(b_value,0,255,0,100))

def rgb_value(value):
    value = '%6X' % value
    value = value.replace(" ", "0")
    r_value = int(value[0:2], 16)
    g_value = int(value[2:4], 16)
    b_value = int(value[4:6], 16)
    set_color(r_value, g_value, b_value)

rgb_value(0xFFab84)
time.sleep(5)
rgb_value(0)