import RPi.GPIO as GPIO

leds = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

GPIO.cleanup()