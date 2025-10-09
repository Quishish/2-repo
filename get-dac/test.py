import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, drange, verbose = False):
        self.__gpio_pin = gpio_pin
        self.__pwm_frequency =  pwm_frequency
        self.__dynamic_range = drange
        self.__verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__gpio_pin, GPIO.OUT, initial = 0)

        self.__pwm = GPIO.PWM(self.__gpio_pin, self.__pwm_frequency)
        self.__pwm.start(0)

        

        

    def deinit(self):
        GPIO.output(self.__gpio_pin, 0)
        GPIO.cleanup()
        self.__pwm.stop()

    def set_voltage(self, voltage):

        drange = self.__dynamic_range
        if not (0.0 <= voltage <= drange):

            print(f"Voltage is beyond DAC vrange (0.00 - {drange:.2f} V)")

            print("Set 0.0 V")
            return

        self.__pwm.ChangeDutyCycle((voltage / self.__dynamic_range)*100)


if __name__ == "__main__":

    try:
        dac = PWM_DAC(12, 1000, 3.117, True)

        while True:
            try:
                voltage = float(input('Enter voltage in V: '))
                dac.set_voltage(voltage)
                
            except ValueError:
                print("Your enter is not a number. Try again\n")
        
    finally:
        dac.deinit()