import RPi.GPIO as GPIO

leds = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

vrange = 3.117

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= vrange):

        print(f"Voltage is beyond DAC vrange (0.00 - {vrange:.2f} V)")

        print("Set 0.0 V")
        return 0

    return int(voltage / vrange * 255)

def number_to_dac(x):
    return[int(element) for element in bin(x)[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input('Enter voltage in V: '))
            number = voltage_to_number(voltage)
            pins = number_to_dac(number)
            for i in range(len(leds)):
                GPIO.output(leds[i], pins[i])
            
        except ValueError:
            print("Your enter is not a number. Try again\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()