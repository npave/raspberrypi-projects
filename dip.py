'''
DIP and LEDs
Raspberry Pi

In this project you turn on and turn off LEDs using a DIP switch. 

What do you need?

* Raspberry Pi
* 4 LEDs - (blue, green, red, yellow)
* DIP switch
* Keyboard
* Resistor
* Jumper wire kit

'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins= [19, 13, 21, 20]
leds = [12, 16, 23, 18]
state = {}

for pin in pins:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
for led in leds:
	GPIO.setup(led, GPIO.OUT)
	state[led] = GPIO.input(led)


def led_on_off(pin):
    led = leds[pins.index(pin)]
    print(str(led))
    GPIO.output(led, not GPIO.input(pin))

for pin in pins:
	led_on_off(pin)

GPIO.add_event_detect(19, GPIO.BOTH, callback=led_on_off, bouncetime=300)
GPIO.add_event_detect(13, GPIO.BOTH, callback=led_on_off, bouncetime=300)
GPIO.add_event_detect(21, GPIO.BOTH, callback=led_on_off, bouncetime=300)
GPIO.add_event_detect(20, GPIO.BOTH, callback=led_on_off, bouncetime=300)

raw_input()

GPIO.cleanup()