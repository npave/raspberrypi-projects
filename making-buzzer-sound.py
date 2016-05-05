# Making a buzzer sound
# Raspberry Pi


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)

def buzz(pitch, duration):
	''' Function to control a speaker
	Args: 
	     pitch: pitch you want to hear between 200 to 2000
	     duration: time in seconds
	'''
	period = 1.0/pitch
	delay = period/2
	cycles = int(duration*pitch)
	for i in xrange(cycles):
		GPIO.output(16, True)
		time.sleep(delay)
		GPIO.output(16, False)
		time.sleep(delay)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
	print('Light on')
	buzz(220, 1)
	time.sleep(0.2)
	

GPIO.cleanup()