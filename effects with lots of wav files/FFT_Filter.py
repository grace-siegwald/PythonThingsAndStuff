#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:14:58 2026

@author: grace.siegwald
"""

import numpy as np
import soundfile as sf
from scipy.fft import rfft, irfft, rfftfreq

def fftTESTFilter(fileName):
    audio, fs = sf.read(fileName)
    
    fft = rfft(audio)
    # number of samples = len(fft)
    frequency = rfftfreq(len(audio), 1/fs)

    cutoff = 5000
    diff = np.abs(frequency - cutoff)
    cutIndex = np.argmin(diff)
    
    fft[:cutIndex] = 0
    
    ifft = irfft(fft)
    sf.write('NEWAUDIO.wav', ifft, fs)


# fftTESTFilter('sound1.wav')
    
def REALfftFilter(fileName):
    audio, fs = sf.read(fileName)
    
    fft = rfft(audio)
    # number of samples = len(fft)
    # frequency = rfftfreq(len(audio), 1/fs)
    magnitudeSpectrum = np.abs(fft)
    
    
    threshold = 100
    
    for i in range(len(fft)):
        if magnitudeSpectrum[i] <= threshold:
            fft[i] = 0
    
    ifft = irfft(fft)

    sf.write('NEWAUDIO.wav', ifft, fs)

REALfftFilter('sound1.wav')