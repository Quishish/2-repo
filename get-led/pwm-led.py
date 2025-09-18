import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

led = 23
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
duty = 20
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)

