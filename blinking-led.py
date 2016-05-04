# Flashing leds
# Raspberry Pi


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def light_on_off(num):
	''' Turn LED ON if it is OFF and reciprocally 
	Args:
	     num: RasPiO pin number
	'''
	light_state = GPIO.input(num)
	if light_state == False:
        		print('Light on')
			GPIO.output(num, GPIO.HIGH)
			time.sleep(0.5)
	if light_state == True:
        		print('Light off')
			GPIO.output(num, GPIO.LOW)
			time.sleep(0.5)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
	light_on_off(20)
	light_on_off(27)
	light_on_off(17)
	light_on_off(21)


GPIO.cleanup()