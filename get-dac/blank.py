import RPi.GPIO as GPIO

leds = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

pwm = GPIO.PWM(12, 1000)

pwm.stop()

GPIO.cleanup()