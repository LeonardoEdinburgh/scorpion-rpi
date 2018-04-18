#!/usr/bin/env python
import serial

direction_max = 100 
direction_min = -100
speed_max	 =  100
speed_min	 = -100

previous_speed = 0
previous_direction = 0

print("Setting up serial...")
ser = serial.Serial('/dev/ttyACM0',115200)
print("Reading...")

# Validate the serial in then return the speed and direction.
# If invalid return the previous values.
def decode_input(input, previous_speed, previous_direction):
	print("length:" + str(len(input)))
	if len(input) == 2 : 
		direction = input[0]
		speed = input[1]
		print("decoded direction:" + direction)
		print("decoded speed:" + speed)
		if (speed < speed_max and direction < direction_max) :
			if( speed > speed_min and direction > direction_min) :
				previous_speed = speed
				previous_direction = direction
				return speed, direction
	# If not returned speed and direction yet then return previous
	return previous_speed, previous_direction
	
# Read serial input, decode it then return input.
def read_serial():
    input = str(ser.readline())     
    input = input.split('_')
    decoded_input = decode_input(input, previous_speed, previous_direction)
    print("decoded input: " + str(decoded_input[0] )+ str(decoded_input[1]))
    return decoded_input

def write_serial(motor_speeds):
	text = str(motor_speeds[0]) + "," + str(motor_speeds[1])
	ser.write(text)
   
def differential_steering(speed, direction):
	left_motor = speed
	right_motor = speed
	direction_percent =  abs(direction) / float(direction_max)
	print("dir perc " + str(direction_percent))
	# If turn left
	if direction < 0 : 
		left_motor -= direction_percent * abs(speed)
	# If turn right
	elif direction > 0 : 
		right_motor -= direction_percent * abs(speed)
	print("left motor: " + str(left_motor))
	print("right motor:  " + str(right_motor))
	return left_motor, right_motor

while 1:
	speed, direction = read_serial()
	motor_speeds = differential_steering(speed, direction)
	write_serial(motor_speeds)


