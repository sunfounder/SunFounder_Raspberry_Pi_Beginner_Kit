import RPi.GPIO as GPIO
import time

# Setup the GPIO and stuff
def setup():
    global led_pin, button_pin, ON, OFF, PRESSED, RELEASED
    led_pin = 17
    button_pin = 18
    ON = "led_on"
    OFF = "led_off"
    PRESSED = 0
    RELEASED = 1
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT, GPIO.HIGH)
    GPIO.setup(button_pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(button_pin, GPIO.BOTH, check_button, bouncetime=20)

# LED control function
def led(status):
    if status == ON:
        GPIO.output(led_pin, GPIO.LOW)
    elif status == OFF:
        GPIO.output(led_pin, GPIO.HIGH)

# callback to check button
def check_button(channel):
    button_status = GPIO.input(button_pin)
    if button_status == PRESSED:
        led(ON)
    elif button_status == RELEASED:
        led(OFF)

# Main function
def main():
    while True:
        print "I'm so boring, doing nothing in main function."
        time.sleep(3)

# "Destroy" everything before stopping the script
def destroy():
    led(OFF)
    GPIO.cleanup()
    
if __name__ == "__main__":
    try:
        setup()
        main()
    except KeyboardInterrupt:
        destroy()
