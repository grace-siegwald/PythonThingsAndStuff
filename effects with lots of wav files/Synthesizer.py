#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:36:58 2026

@author: grace.siegwald
"""
"""
NOTE:
Make sure you you put the following line into your terminal (if you don't already have the required libraries installed):
    pip install numpy soundfile sounddevice
To play "Twinke Twinkle Little Star", input the following as your MIDI values (and liiiiike 60bpm)
    60 60 67 67 69 69 67 0 65 65 64 64 62 62 60 0
TODO: 
    Have user input array for the duration of each note ! 
"""

import numpy as np 
import soundfile as sf
import sounddevice as sd

class Synthesizer:

    def __init__(self):
        self.sampleRate = 44100
        
        # asking the user for all their inputs and such and things 
        midiInput = input('\nEnter the MIDI values you would like to use beautfiul\n')
        durationInput = input('\nALSO input what duration you want each of those notes to be! btw here is what u entered :D\n'
                                + f'{midiInput}\n')
        bpm = float(input('\nNOW input what bpm you want it to beeeee!\n'))

        midiNotes = np.array(midiInput.split(), dtype=int) # the string.split(with no arguments) splits the string at each empty space
        self.duration = np.array(durationInput.split(), dtype=int)

        audio = self.melody(midiNotes, bpm)

        self.playPrompt(audio)
        self.savePrompt(audio)

# the "convert thing-to-thing" section! ------------------------------------------------------------------------------------------------------------------------
        
    def midiToFrequency(self, midiNote):
        """
         Here is where we convert the usere's MIDI note to a Frequency in Hz !
        """
        if ( midiNote > 127 or midiNote < 0 ):
            return ValueError(f'Your MIDI note {midiNote} is out of range (0–127), silly!')
        else:
            frequency = 440.0 * (2 ** ((midiNote - 69) / 12))
            return frequency
        
    def bpmToSeconds (self, bpm):
        """
         Here is where we convert the user's inputed BPM to duration of one BEAT in seconds !
        """
        if (bpm <= 0):
            return ValueError('Your BPM must be a positive number, silly!')
        else:
            seconds = 60.0 / bpm
            return seconds
        
    def secondsToSamples (self, seconds):
        """
         Anddddd here we convert those beats in seconds to number of SAMPLES !
        """
        self.numSamples = int(seconds * self.sampleRate)
        return self.numSamples
    
    
# the "very-important-methods" section! ----------------------------------------------------------------------------------------------------------------------
    
    def oscillator (self, frequency, numSamples, numHarmonics = 20):
        """
         welp this is an additive sawtooth oscilator... :)
         this creates a sine wave for ONE NOTE AT A TIME 
         isn't that so cool! math is so cool !!
        """
        # "t" is like the timestamps for each sample! blah blah blah
        t = np.linspace(0, numSamples / self.sampleRate, numSamples, endpoint=False)
        # creating empty array that is the size of number of samples
        wave = np.zeros(numSamples)

        # Here is where the magic happens, creating the wave! 
        # for each harmonic (i) in range of numHarmonics 
        # which is set to 20 by defualt idk if that's good but ahhhh that's what I chose!
        for i in range(1, numHarmonics + 1):
            # tbh I do not understand how this equation works... but it's here! :)
            wave += (1.0 / i) * np.sin(2 * np.pi * frequency * i * t)
        
        # this "normalizes" the array (the waveform) by dividing the entire thing by the largest number (np.max) and returns!
        return wave / np.max(np.abs(wave)) 
    
    def envelope(self, numSamples, attackRatio = .1, decayRatio = .1):
        """
         the envelope we apply to each note with a LINEAR attack and decay (what were applying to the begining and end of each "note")
         attackRatio is the precentage of the note we fade in on (so .1 is 10%)
         ecayRatio is the same thing on the other end of the note !
        """
        env = np.ones(numSamples) # I like to think of this as a "blank canvas" array of just 1's, same size as numSamples
        attackSamples = int(numSamples * attackRatio) # finding the duration of the attack (and decay) as samples
        decaySamples = int(numSamples * decayRatio)
        
        # these are slicing at the coresponding points (beginning and end) and creating that fade with linspace() evenly space thingy
        env[:attackSamples] = np.linspace(0, 1, attackSamples) 
        env[-decaySamples:] = np.linspace(1, 0, decaySamples)
        return env
    
    def note(self, frequency, numSamples): # Inheritence, perhaps? Each note HAS a frequency and a number of samples :)
        """
         This is where we actually form each note we are making! wow so exciting! wow wow wow!!!
         a note is literally just: oscillator * envelope (i learned this from notes and magical google :)
        """
        # wow we are simply creating an instance of each method, how object oriented of us! 
        oscilator = self.oscillator(frequency, numSamples) 
        envelope = self.envelope(numSamples)
        return oscilator * envelope
    
    def melody(self, midiNotes, bpm):
        """
         aaaaand here's the most exciting part: where we create the full melody based off the input MIDI list of notes!
         it after all that work were left with a single array... how fitting.... 
        """
        # converting the bpm user's inputted bpm to seconds then to numSamples
        # we love actually getting to use the methods we write :)
        numSeconds = self.bpmToSeconds(bpm)
        numSamples = self.secondsToSamples(numSeconds) # numSamples PER NOTE

        segments = np.array([]) # empty array, we love an empty array
        for note in midiNotes: # for each note in the list of midiNotes...
            frequency = self.midiToFrequency(note) # convert to frequency with our function
            segments = np.append(segments, self.note(frequency, numSamples))

        return segments

    def playPrompt(self, audio):
        play = input('\nWould you like to play the melody? (YES or NO)\n').lower().strip()
        if play == 'yes':
            print('playing...')
            sd.play(audio, self.sampleRate)
            sd.wait() # this "Waits for play()/rec()/playrec() to be finished."
            print('done!')
            return
        if play == 'no':
            return
        else:
            print('thats not the correct input, buddy')
            self.playPrompt(audio) # recursive call
    
    def savePrompt(self, audio):
        save = input('\nWould you like to save your masterpiece to a .wav file? (YES or NO)\n').lower().strip()
        if save == 'yes':
            fileName = input('Enter a file name (e.g. melody.wav):\n').strip()
            sf.write(fileName, audio, self.sampleRate)
            print(f'Saved to {fileName} !')
            return
        if save == 'no':
            print('awwww well thanks for using me!')
            return
        else:
            print('thats not the correct input, buddy')
            self.savePrompt(audio) # recursive call
        
# Initialize class
synth = Synthesizer()

        
        
        
        
        
        
        
        
        