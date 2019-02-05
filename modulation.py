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
    plt.subplot(3,1,1)
    plt.plot(time, carrier)
    plt.subplot(3,1,2)
    plt.plot(time, pulse)
    plt.subplot(3,1,3)
    plt.plot(time, ask)
    plt.show()

def fsk():
    print 'Modulation FSK'
    freq_carrier = 25
    freq_delta = 10
    freq_pulse = 5
    amplitude = 3
    time = np.arange(0, 1, 0.001)
    carrier_freq_1 = amplitude*np.sin(2*math.pi*(freq_carrier+freq_delta)*time)
    carrier_freq_2 = amplitude*np.sin(2*math.pi*(freq_carrier-freq_delta)*time)
    pulse = 0.5*signal.square(2*math.pi*freq_pulse*time)+0.5
    fsk = []
    for i in range(len(time)):
        if pulse[i] == 0:
            fsk.append (carrier_freq_2[i])
        else:
            fsk.append(carrier_freq_1[i])
    plt.title("FSK")
    plt.subplot(4,1,1)
    plt.plot(time, carrier_freq_1)
    plt.subplot(4,1,2)
    plt.plot(time, carrier_freq_2)
    plt.subplot(4,1,3)
    plt.plot(time, pulse)
    plt.subplot(4,1,4)
    plt.plot(time, fsk)
    plt.show()

def bpsk():
    #dos fases BPSK o PAM
    #cuatro fases QPSK o QAM
    #ocho fases 8-PSK y asi
    print 'Modulation FSK'
    freq_carrier = 25
    fase1 = 0
    fase2 = 180
    freq_pulse = 5
    amplitude = 3
    time = np.arange(0, 1, 0.001)
    carrier_fase_1 = amplitude*np.cos(2*math.pi*freq_carrier*time+fase1)
    carrier_fase_2 = amplitude*np.cos(2*math.pi*freq_carrier*time+fase2)
    pulse = 0.5*signal.square(2*math.pi*freq_pulse*time)+0.5
    fsk = []
    for i in range(len(time)):
        if pulse[i] == 0:
            fsk.append (carrier_fase_2[i])
        else:
            fsk.append(carrier_fase_1[i])
    plt.title("BPSK")
    plt.subplot(4,1,1)
    plt.plot(time, carrier_fase_1)
    plt.subplot(4,1,2)
    plt.plot(time, carrier_fase_2)
    plt.subplot(4,1,3)
    plt.plot(time, pulse)
    plt.subplot(4,1,4)
    plt.plot(time, fsk)
    plt.show()

if __name__ == "__main__":	    
    #ask()
    #fsk()
    bpsk()
