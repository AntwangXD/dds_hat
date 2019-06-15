from tkinter import *
import math

#
# This file implements the central frequency editor label
#

MAX_FREQUENCY=999999
MIN_FREQUENCY=0

class FrequencyLabel(Label):

    #frequency in Hz
    frequency=1000
    divisor=1000
    units='kHz'
    decade=3
    cursor=4
    dpPosition=3
    #
    def __init__(self,parent,**kwargs):
        Label.__init__(self,parent,**kwargs)
        self.update()

    #
    def update(self):
        if self.units=='Hz':
            self.config(text='{:07.0f} {:s}'.format(self.frequency/self.divisor,self.units))       
        if self.units=='kHz':
            self.config(text='{:07.3f} {:s}'.format(self.frequency/self.divisor,self.units))       
        if self.units=='MHz':
            self.config(text='{:07.3f} {:s}'.format(self.frequency/self.divisor,self.units))       
        self.config(underline=6-self.cursor)
        print(self.frequency)

    #
    def setUnits(self,units):
        if self.units=='Hz':
            self.dpPosition=-1
            self.divisor=1    
            self.frequency=1    
        if self.units=='kHz':
            self.dpPosition=3
            self.divisor=1000
            self.frequency=1000    
        if self.units=='MHz':
            self.dpPosition=6
            self.divisor=1000000
            self.frequency=1000000    
        self.cursor=0
        self.units=units
        self.update()

    #
    def incDecade(self):    
       if self.cursor<6:
            self.cursor+=1
            self.decade+=1 
            if self.cursor==self.dpPosition: 
                self.cursor+=1
            self.update()

    #
    def decDecade(self):    
        if self.cursor > 0:
            self.cursor-=1   
            self.decade-=1 
            if self.cursor==self.dpPosition: 
                self.cursor-=1
            self.update()

    #
    def inc(self):
        if self.frequency+math.pow(10,self.decade)<MAX_FREQUENCY:
            self.frequency+=math.pow(10,self.decade)
        self.update()

    #
    def dec(self):
        if self.frequency-math.pow(10,self.decade)>=MIN_FREQUENCY:
            self.frequency-=math.pow(10,self.decade)
        self.update()

    #
    def getFrequency(self):
        return int(self.frequency)

