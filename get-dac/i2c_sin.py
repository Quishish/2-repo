import mcp4725_driver as i2c
import signal_generator as sg
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 50

if __name__ == '__main__':
    dac = i2c.MCP4725(3.117)
    try:
        

        while True:
            try:
                sg.wait_for_sampling_period(sampling_freq)
                time1 = time.time()
                voltage = sg.get_sin_wave_amplitude(signal_freq, time1)
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Your enter is not a number. Try again\n")
    
    finally:
        dac.deinit()