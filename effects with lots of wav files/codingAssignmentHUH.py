#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 08:21:03 2026

@author: grace.siegwald
"""

import numpy as np 
import soundfile as sf
import sounddevice as sd
import math


class MultiEffect:
       
    def __init__(self, fileName):
        
        # This is where we take in the actual audio array and sampe rate of whatever file were using!
        self.audio, self.sampleRate = sf.read(fileName)
        
        # Here we are finding the number of samples and channels, differentiating between a mono and a stero file
        if (self.audio.ndim > 1):
            self.numSamples = self.audio.shape[0]
            self.numChannels = self.audio.shape[1]
        else:
            self.numSamples = len(self.audio)
            self.numChannels = 1
        
        # and this is where we find the duration of the file !
        self.duration = self.numSamples / self.sampleRate
        
    
    # this method just returns information about the current file we are manipulating 
    def __str__(self):
        return f'{self.fileName}: \n sample-rate) {self.sampleRate} \n duration) {self.duration} \n Channels) {self.numChannels}'
        
    # this method will reverse whatver file we are manipulating
    def reverse(self):
        # here we reverse the array by using a negitive step size !
        audioOut = self.audio[ : :-1]
        return self.Write(audioOut)
    
    # this method "clips" a waveform based on the inputted number
    def distort(self, amount = 10):
        # I think this stops it from clipping TOOOO much...
        maxAmplitude = .2
        # Just increasing the gain! I convert it to an int just to be safe? idk
        audioOut = self.audio * int(amount)
        # Here is where the clipping actually happens!
        audioOut = np.clip(audioOut, -maxAmplitude, maxAmplitude)
        return self.Write(audioOut)
        
    def mirror(self):
        # I thinkkk this is all that needs to happen for this to work with all types of files
        # if else to distinguish between mono and multi channel 
        if (self.numChannels > 1):
            '''
            # This is where we decide the number if axis to flip on? Idk if this will work tbh its just a hunch
            # My hunch is that we need to flip on 2 axis if its a four-channel input, which this would do
            # But i could just be over complicating things lol
            numAxis = self.numChannels / 2
            # Just using np.flip to flip the chanels!
            audioOut = np.flip(self.audio, axis= numAxis)
            return self.Write(audioOut)
            '''
            audioOut = self.audio[::, ::-1]
            return self.Write(audioOut)
        # else, if its a mono file, do nothing!
        else:
            audioOut = self.audio
            return self.Write(audioOut)
        
    # allows user to apply tremelo effect with a custom rate of "wobble" (we keep it between 1 and 20 behind their backs lol)
    def tremolo(self, rate):
        # empty array for audio out!
        audioOut = np.array([])
        
        audioOut = np.arange(self.numSamples)
        # we are applying the effect to each sample in the audio array
        
        for i, sample in self.audio:
            # just keeping the rate between 1 and 20!
            if rate > 20:
                rate = 20
            if rate < 1:
                rate = 1
            # depth is just how much the volume will drop for each sample
            depth = 0.5
            # finding the current time in seconds !
            time = i / self.sampleRate
            # lfo = low frequency oscilator, to be honest im not sure *why* the formula works, but here it is!
            lfo = math.sin(2 * math.pi * rate * time)
            # doing the modulation with an equation I don't quite understand!
            # volume fluctuates between (1 - depth) and 1 ?
            modulation = 1 - (depth * 0.5 * (1 + lfo))
            # actually applying the modulation to the sample (making sure its and int for... safety?)
            np.append(audioOut, sample * modulation)
            
            print(audioOut)
            return self.Write(audioOut)
    def Write(self, audio):
        # this is where it writes the audio to the file
        sf.write('modulatedFile.wav', audio, self.sampleRate)
        
        
MultiEffect('mono.wav').tremolo(10)



        
        