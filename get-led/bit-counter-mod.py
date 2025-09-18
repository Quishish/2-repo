import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16,12,25,17,27,23,22,24]

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

up = 9
GPIO.setup(up, GPIO.IN)

down = 10
GPIO.setup(down, GPIO.IN)

num = 0

def dec2bin (x):
    return[int(element) for element in bin(x)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if num < 0:
        num = 0
    if num > 255:
        num = 255

    if GPIO.input(up):
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(down):
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    

    if GPIO.input(up) and GPIO.input(down):
        num = 255
    
    number = dec2bin(num)
    for i in range(len(leds)):
        GPIO.output(leds[i], number[i])

        
GPIO.cleanup()