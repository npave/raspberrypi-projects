'''
Numbers in a 7-segment display
Raspberry Pi

What do you need?

* 1 x 7-segment display
* 3 x toggle button
* 2 x resistors
* wire

'''

from gpiozero import Button, LED
import time
from signal import pause

# Assigning the GPIO number to the buttons and 7-segment display

reset = 3 
plus =  10
minus = 5
leds_ids = [20, 21, 23, 15, 14, 25, 24]

# Creating a instance of a Button and LED object
leds = [LED(led) for led in leds_ids]
button_reset = Button(reset)
button_plus = Button(plus)
button_minus = Button(minus)

# Defining numbers using the a pin connection diagram of the 7-segment display
# 1 = LED ON
# 0 = LED OFF
# To draw each number you need to find which LEDs are ON and which are OFF.
# For example: zero needs g OFF and others LEDs ON. 0 = [1,1,1,1,1,1,0] 
#     a
#    ___
# f |_g_| b
# e |___| c
#     d

numbers = [[1,1,1,1,1,1,0], [0,1,1,0,0,0,0], [1,1,0,1,1,0,1], [1,1,1,1,0,0,1], 
			    [0,1,1,0,0,1,1], [1,0,1,1,0,1,1], [1,0,1,1,1,1,1],
			    [1,1,1,0,0,0,0], [1,1,1,1,1,1,1], [1,1,1,0,0,1,1]
	]

current_number = 0

def print_number(number):
	''' Draw a number in the 7-segment display. Turn on and off LEDs as need.
	Args: 
		number: number to draw
				
	'''
	for led, value in zip(leds, numbers[number]):
		if value == 0:
			led.on()
		else:
			led.off()

def update_display(button, delta):
	'''Update 7-segment display
	Args: 
		button: the button that was pressed (reset, plus, minus)
		delta: operation to apply to the current number 
	'''
	print(button)
	global current_number
	if delta == 0:
		current_number = 0
	else:
		current_number += delta
	current_number = max(0, min(len(numbers) - 1, current_number))
	print_number(current_number)

	

print_number(current_number)

button_reset.when_pressed = lambda: update_display("reset", 0)
button_plus.when_pressed = lambda: update_display("plus", 1)
button_minus.when_pressed = lambda: update_display("minus", -1)

pause()