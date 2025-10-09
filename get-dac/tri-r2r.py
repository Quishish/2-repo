import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 1000

if __name__ == '__main__':
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.117)
    try:
        

        while True:
            try:
                sg.wait_for_sampling_period(sampling_freq)
                time1 = time.time()
                voltage = sg.tri_gen(signal_freq, time1)
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Your enter is not a number. Try again\n")
    
    finally:
        dac.deinit()