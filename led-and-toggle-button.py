# LED and Button Toggle
# Raspberry Pi


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    light_state = GPIO.input(27) 
    if input_state == False:
		if light_state == False:
        		print('Light on')
			GPIO.output(27, GPIO.HIGH)
        		time.sleep(0.2)
		if light_state == True:
        		print('Light off')
			GPIO.output(27, GPIO.LOW)
        		time.sleep(0.2)

GPIO.cleanup()