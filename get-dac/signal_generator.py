import time
import numpy as np
import math

def get_sin_wave_amplitude(freq, time):
##   return (np.sin(2 * np.pi * freq * time) + 1) / 2
    sinus = math.sin(2*np.pi*freq*time)
    return (sinus+1)/2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

def tri_gen(freq, time):
    return ((-2.0 / np.pi) * math.asin(math.sin(2*np.pi*freq*time))+1)/2