import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, drange, verbose = False):
        self.gpio_bits = gpio_bits
        self.drange = drange
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_voltage (self, voltage):
        
        def set_number (number):
            return [int(x) for x in bin(number)[2:].zfill(8)]

        drange = self.drange
        if not (0.0 <= voltage <= drange):

            print(f"Voltage is beyond DAC vrange (0.00 - {drange:.2f} V)")

            print("Set 0.0 V")
            return 0

        a = int (voltage / drange * 255)

        pins = set_number(a)

        leds = self.gpio_bits 
        
        for i in range(len(leds)):
            GPIO.output(leds[i], pins[i])

        return 0
    

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.117, True)

        while True:
            try:
                voltage = float(input('Enter voltage in V: '))
                dac.set_voltage(voltage)

            except ValueError:
                print("Your enter is not a number. Try again\n")
    
    finally:
        dac.deinit()