import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, drange, verbose = False):
        self.pwm_frequency = pwm_frequency
        self.gpio_pin = gpio_pin
        self.drange = drange
        self.verbose = verbose
        pwm = GPIO.PWM(gpio_pin, pwm_frequency)
        self.duty = 0
        pwm.start(duty)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):

        drange = self.drange
        if not (0.0 <= voltage <= drange):

            print(f"Voltage is beyond DAC vrange (0.00 - {drange:.2f} V)")

            print("Set 0.0 V")
            return 0

        a = int (voltage / drange * 100)

        freq = self.pwm_frequency
        led = self.gpio_pin
        
        pwm.ChangeDutyCycle(a)
        return 0
        

try:
    dac = PWM_DAC(12, 500, 3.117, True)

    while True:
        try:
            voltage = float(input('Enter voltage in V: '))
            dac.set_voltage(voltage)
            
        except ValueError:
            print("Your enter is not a number. Try again\n")
    
finally:
    dac.deinit()