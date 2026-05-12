#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:24:18 2026

@author: grace.siegwald
"""

"""
Import a sound file and apply a 1 second fade in and a 1.5 second fade out. Play the resulting waveform using the sounddevice module.
Import two different sound files of the same length. Mix down the two sounds to a single array. Play the resulting waveform using the sounddevice module.
Import two different sound files of the same length. If they are mono, use one as the left channel and the other as the right channel to create a new stereo sound. If the files are stereo, use the left channel of one file and the right channel of the other. Play the resulting waveform using the sounddevice module.
Import a sound file and this impulse response  Download this impulse response(download it from the Files page if you cannot download from this link). Apply convolution reverb using the given impule response. Export the resulting waveform as a WAV file.
"""


import numpy as np # only reqired for examples using np.* methods (but not indexing & slicing)
import soundfile as sf
import sounddevice as sd


class AudioEffects:
    
    def fadeInFadeOut(file_name):
        audio, fs = sf.read(file_name)
        
        # Defining the fade in and fade out in seconds
        in_seconds = 1
        out_seconds = 1.5
        
        # Converting the seconds to the sample rate of the sound file
        in_samples = round(in_seconds * fs)
        out_samples = round(out_seconds * fs)
        
        # Defining the envelope for both in and out fade (idk what that actually means tbh :)
        in_envelope = np.linspace(0, 1, in_samples)
        out_envelope = np.linspace(1, 0, out_samples)
        
        # Making the actual audio of the fade in and fade out
        fade_in = audio[:in_samples] * in_envelope
        fade_out = audio[-out_samples:] * out_envelope
        
        # The middle is the part of the audio that stays the same, that we're not manipulating
        middle = audio[in_samples+1:-out_samples-1]
        
        # Putting each of the sections together
        audio_out = np.concatenate([fade_in, middle, fade_out])
        
        #Playing the audio!
        sd.play(audio_out, samplerate=fs)

    def comboSound(file1, file2):
        audio_1, fs = sf.read(file1)
        audio_2, fs = sf.read(file2)
        
        audio_out = np.concatenate([audio_1, audio_2])
        
        sd.play(audio_out, samplerate=fs)

    def monoToStereo (left_file, right_file):
        audio_1, fs = sf.read(left_file)
        audio_2, fs = sf.read(right_file)
        
        audio_out = (audio_1 + audio_2)/2
        
        sd.play(audio_out, samplerate=fs)
    
    def impulseResponse (file_name):
        audio, fs = sf.read(file_name)
        ir, fs = sf.read('impulse_response.wav')
        
        audio_out = np.convolve(audio, ir)
        
        sd.play(audio_out, samplerate=fs)




AudioEffects.fadeInFadeOut('sound1.wav')
AudioEffects.comboSound('tung-tung-sahur.wav', 'sound1.wav')
AudioEffects.monoToStereo('sound2.wav', 'sound1.wav')
AudioEffects.impulseResponse('sound1.wav')



