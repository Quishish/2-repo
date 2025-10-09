import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    def set_voltage(self, voltage):

        def set_number(number):
            if not isinstance(number, int):
                print("На вход ЦАП можно подавать только целые числа")

            if not (0 <= number <= 4095):
                print("Число выходит за разраядность MCP4752 (12 бит)")

            first_byte = self.wm | self.pds | number >> 8
            second_byte = number & 0xFF
            self.bus.write_byte_data(0x61, first_byte, second_byte)

            if self.verbose:
                print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

        drange = self.dynamic_range
        if not (0.0 <= voltage <= drange):

            print(f"Voltage is beyond DAC vrange (0.00 - {drange:.2f} V)")

            print("Set 0.0 V")
            return
        
        number = int((voltage / self.dynamic_range)*4095)
        set_number(number)

    def deinit(self):
        self.bus.close()

if __name__ == "__main__":

    try:
        dac = MCP4725(5)

        while True:
            try:
                voltage = float(input('Enter voltage in V: '))
                dac.set_voltage(voltage)
                
            except ValueError:
                print("Your enter is not a number. Try again\n")
        
    finally:
        dac.deinit()