#!/usr/bin/env python
import serial

print("Setting up serial...")
ser = serial.Serial('/dev/ttyACM0',115200)

print("Reading...")
previous_speed = 0
previous_direction = 0

def validate_serial(input, previous_speed, previous_direction):
    print("lenght:" + str(len(input)))
    if len(input) != 2:
        return previous_speed, previous_direction 
    direction = input[0]
    speed = input[1]
    print("speed:" + speed)
    print("dir:" + direction)
   # if (speed or direction > 100) or (speed or direction < 100):
   #     return previous_speed, previous_direction

    # Store previous values
    previous_speed = speed
    previous_direction = direction
    return speed, direction

def read_serial():
    # Read serial input
    input = str(ser.readline())
    # Split speed and direction values
    input = input.split('_')
    # Validate serial input
    valid_input = validate_serial(input, previous_speed, previous_direction)
    print(valid_input)
    return valid_input

def write_serial(input):
    ser.write(input)
    
def differential_steering():
    pass

while 1:

    speed, direction = read_serial()

    print(speed)
    print(direction)


