from tkinter import *
import math

#
# This file implements the central voltage editor label
#

MAX_VOLTAGE=10000
MIN_VOLTAGE=0

class VoltageLabel(Label):

    # voltage in mV
    voltage=2000
    units='Vpk-pk'
    divisor=1000
    decade=3
    cursor=4

    #
    def __init__(self,parent,**kwargs):
        Label.__init__(self,parent,**kwargs)
        self.update()

    def update(self):
        self.config(text='{:1.3f} {:s}'.format(self.voltage/self.divisor,self.units))       
        self.config(underline=4-self.cursor)

    #
    def incDecade(self):    
        print(self.cursor)
        if self.cursor<5:
            self.cursor+=1
            self.decade+=1 
            if self.cursor==3: 
                self.cursor+=1
            self.update()

    #
    def decDecade(self):    
        if self.cursor > 0:
            self.cursor-=1   
            self.decade-=1 
            if self.cursor==3: 
                self.cursor-=1
            self.update()

   #
    def inc(self):
        if self.voltage+math.pow(10,self.decade)<MAX_VOLTAGE:
            self.voltage+=math.pow(10,self.decade)
        self.update()

    #
    def dec(self):
        if self.voltage-math.pow(10,self.decade)>=MIN_VOLTAGE:
            self.voltage-=math.pow(10,self.decade)
        self.update()

    def getVoltage(self):
        return int(self.voltage)    


