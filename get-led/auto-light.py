import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 23
GPIO.setup(led, GPIO.OUT)

lx = 6
GPIO.setup(lx, GPIO.IN)
state = 0

while True:
    state = GPIO.input(lx) - 1
    GPIO.output(led, state)
    
