from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as signal

def ask():
    print 'Modulation ASK'
    freq_carrier = 25
    freq_pulse = 5
    amplitude = 3
    time = np.arange(0, 1, 0.001)
    carrier = amplitude*np.sin(2*math.pi*freq_carrier*time)
    pulse = 0.5*signal.square(2*math.pi*freq_pulse*time)+0.5
    ask = carrier * pulse
    plt.title("ASK")
    plt.plot(time, carrier)
    plt.plot(time, pulse)
    plt.plot(time, ask)
    plt.show()

def fsk():
    print 'Modulation FSK'
    freq_carrier = 25
    freq_delta = 10
    freq_pulse = 5
    amplitude = 3
    time = np.arange(0, 1, 0.001)
    carrier = amplitude*np.sin(2*math.pi*freq_carrier*time)
    pulse = 0.5*signal.square(2*math.pi*freq_pulse*time)+0.5
    ask = carrier * pulse
    plt.title("FSK")
    plt.plot(time, carrier)
    plt.plot(time, pulse)
    plt.plot(time, ask)
    plt.show()

if __name__ == "__main__":	    
    #ask()
    fsk()
