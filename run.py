#!/usr/bin/env python
import serial

direction_max = 100 
previous_speed = 0
previous_direction = 0
left_motor = 0
right_motor = 0

def init():
	print("Setting up serial...")
	ser = serial.Serial('/dev/ttyACM0',115200)
	print("Reading...")

# Validate the serial in then return the speed and direction.
# If invalid return the previous values.
def decoded_input(input, previous_speed, previous_direction):
    print("lenght:" + str(len(input)))
    if len(input) != 2:
        return previous_speed, previous_direction 
    direction = input[0]
    speed = input[1]
    print("speed:" + speed)
    print("dir:" + direction)
   # if (speed or direction > 100) or (speed or direction < 100):
   #     return previous_speed, previous_direction

    previous_speed = speed
    previous_direction = direction
    return speed, direction
	
# Read serial input, decode it then return input.
def read_serial():
    input = str(ser.readline())     
    input = input.split('_')
    decoded_input = decoded_input(input, previous_speed, previous_direction)
    print(decoded_input)
    return decoded_input

def write_serial(input):
    ser.write(input)
    
def differential_steering(speed, direction):
    left_motor = speed
	right_motor = speed
	direction_percent = abs(direction) / direction_max
	# If turn left
	if direction < 0 : 
		left_motor -= direction_percent * abs(speed)
	# If turn right
	elif direction > 0 : 
		right_motor -= direction_percent * abs(speed)
while 1:

	init()
    speed, direction = read_serial()
	differential_steering(speed, direction)
    print(speed)
    print(direction)


