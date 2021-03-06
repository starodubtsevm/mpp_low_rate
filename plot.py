import matplotlib.pyplot as plt
import numpy as np
from const import *
from scipy import fft, arange

def to_plot (signal_buf,filter_buf,fsk_det_flt_buf,comp_buf,sem_pll_buf,sem_pll_err_buf):


	fig, axs = plt.subplots(3, 2,sharex=True)
	fig.subplots_adjust(hspace=0.1)

	axs[0,0].plot(t, signal_buf)
	axs[0,0].set_xlabel('Input signal')

	axs[1,0].plot(t, filter_buf)
	#axs[1,0].plot(t, limiter_buf)
	axs[1,0].set_xlabel('After channel filter output')

	axs[2,0].plot(t, fsk_det_flt_buf)
	#axs[2,0].plot(t, fsk_det_buf)
	axs[2,0].set_xlabel('After fsk det and filter output')

	axs[0,1].plot(t, comp_buf)
	axs[0,1].set_ylim(-0.5, 2)
	axs[0,1].set_xlabel('Comp output')

	axs[1,1].plot(t, sem_pll_buf)
	axs[1,1].set_ylim(-0.5, 2)
	axs[1,1].set_xlabel('Sync Pll sem output')

	axs[2,1].plot(t, sem_pll_err_buf)
	#axs[2,1].set_ylim(-0.5, 2)
	axs[2,1].set_xlabel('Error Pll sem output')
	
	
def to_plotSpectrum(y):

	n = len(y) # length of the signal
	k = arange(n)
	T = n/fs
	frq = k/T # two sides frequency range
	frq = frq[range(n//2)] # one side frequency range
	Y = fft(y)/n # fft computing and normalization
	Y = Y[range(n//2)]

	plt.subplot(2,1,1)
	plt.plot(t, y)
	plt.xlabel('Time')
	plt.ylabel('Amplitude')
	
	plt.subplot(2,1,2)
	plt.plot(frq, abs(Y),'r') # plotting the spectrum
	plt.xlabel('Freq (Hz)')
	plt.ylabel('|Y(freq)|')


