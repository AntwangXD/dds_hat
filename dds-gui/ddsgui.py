#!/usr/bin/python3

#
# The main program for the function genrator GUI
# The GUI uses the tkinter GUI tooklit. 
# Most of this file is about setting up the GUI elements
# and wiring the buttoen events etc. to the appropriate routines
#

from tkinter import *
from tkinter import font
import dial
import iio
import math
import flab
import vlab
import sys

test=True

#
def printf(format,*values):
    print(format % values )

#
def setFrequency():
    if test==False:
        iio.setFrequency(frequencyLabel.getFrequency())

#
def setVoltage():
    if test==False:
        iio.setVoltage(voltageLabel.getVoltage())

#
def setWavetype():
    if test==False:
        iio.setWavetype(wavetype.get())

#
def dialIncrement(self):
    digitIncrement()

#
def dialDecrement(self):
    digitDecrement()

#
def digitIncrement():
    if function.get()=='Hz':
        frequencyLabel.inc()
        setFrequency()
    elif function.get()=='V':
        voltageLabel.inc()
        setVoltage()

#
def digitDecrement():
    if function.get()=='Hz':
        frequencyLabel.dec()  
        setFrequency()
    elif function.get()=='V':
        voltageLabel.dec()
        setVoltage()

#
def decadeIncrement():
    if function.get()=='Hz':
        frequencyLabel.incDecade()  
    elif function.get()=='V':
        voltageLabel.incDecade()
  
#
def decadeDecrement():
    if function.get()=='Hz':
        frequencyLabel.decDecade()
    elif function.get()=='V':
        voltageLabel.decDecade()

#
def setUnits():
    frequencyLabel.setUnits(units.get())

#
def shutdown():
    iio.enableOutput(False)
    sys.exit()

# main window
window=Tk()
window.overrideredirect(True)
window.configure(pady=0)
window.title('DDS Function Generator')
window.geometry('800x480')
window.config(cursor='none')

# wavetype selection
wavetypeFrame=Frame(window)
wavetypeFrame.grid(column=0,row=3) 
wavetype=StringVar()
wavetype.set('sine')
sine=Radiobutton(wavetypeFrame,width=8,text='Sine',command=setWavetype,variable=wavetype,value='sine',font=('Ubuntu',20),indicatoron=0)
square=Radiobutton(wavetypeFrame,width=8,text='Square',command=setWavetype,variable=wavetype,value='square',font=('Ubuntu',20),indicatoron=0)
triangle=Radiobutton(wavetypeFrame,width=8,text='Triangle',command=setWavetype,variable=wavetype,value='triangle',font=('Ubuntu',20),indicatoron=0)
sine.grid(column=0,row=0,padx=10)
square.grid(column=0,row=1,padx=10)
triangle.grid(column=0,row=2,padx=10)

# units selection
unitsFrame=Frame(window)
unitsFrame.grid(column=0,row=0,rowspan=3) 
units=StringVar()
units.set('kHz')
hz=Radiobutton(unitsFrame,width=8,text='Hz',command=setUnits,variable=units,value='Hz',font=('Ubuntu',20),indicatoron=0)
khz=Radiobutton(unitsFrame,width=8,text='kHz',command=setUnits,variable=units,value='kHz',font=('Ubuntu',20),indicatoron=0)
mhz=Radiobutton(unitsFrame,width=8,text='MHz',command=setUnits,variable=units,value='MHz',font=('Ubuntu',20),indicatoron=0)
hz.grid(column=0,row=0,padx=10)
khz.grid(column=0,row=1,padx=10)
mhz.grid(column=0,row=2,padx=10)

# function selection for dial
functionFrame=Frame(window)
functionFrame.grid(column=2,row=3,pady=30) 
function=StringVar()
function.set('Hz')
hertz=Radiobutton(functionFrame,width=8,text="Hz",variable=function,value='Hz',font=('Ubuntu',20),indicatoron=0)
volts=Radiobutton(functionFrame,width=8,text="V",variable=function,value='V',font=('Ubuntu',20),indicatoron=0)
exit=Radiobutton(functionFrame,width=8,text="Exit",command=shutdown,value='E',font=('Ubuntu',20),indicatoron=0)
hertz.grid(column=0,row=0,padx=10)
volts.grid(column=0,row=1,padx=10)
exit.grid(column=0,row=2,padx=10)

# frequency display
frequencyLabel=flab.FrequencyLabel(window,width=12,anchor=E,font=('Ubuntu Mono',40),bg='black',fg='green',padx=10,pady=20,underline=3)
frequencyLabel.grid(column=1,row=1,padx=20)

# voltage display
voltageLabel=vlab.VoltageLabel(window,width=13,anchor=E,font=('Ubuntu Mono',30),bg='black',fg='green',padx=10,pady=20,underline=3)
voltageLabel.grid(column=1,row=3,padx=20,sticky=E)

# dial for adjusting frequency and voltage
dialFrame=Frame(window)
freqDial=dial.Dial(dialFrame)

dialFrame.grid(column=2,row=0,rowspan=3,pady=30) 
freqDial.bind('<<DialIncrement>>',dialIncrement)
freqDial.bind('<<DialDecrement>>',dialDecrement)
freqDial.grid(column=0,row=0) 

jogUp=Button(dialFrame,width=1,text='+',command=digitIncrement,font=('Ubuntu',22))
jogUp.grid(column=0,row=0,sticky=SW)
jogDown=Button(dialFrame,width=1,text='-',command=digitDecrement,font=('Ubuntu',22))
jogDown.grid(column=0,row=0,sticky=SE)

decadeUp=Button(dialFrame,width=1,text='<',command=decadeIncrement,font=('Ubuntu',22))
decadeUp.grid(column=0,row=0,sticky=NW)
decadeDown=Button(dialFrame,width=1,text='>',command=decadeDecrement,font=('Ubuntu',22))
decadeDown.grid(column=0,row=0,sticky=NE)

# set defaults and start up
iio.setFrequency(frequencyLabel.getFrequency())
iio.setVoltage(voltageLabel.getVoltage())
iio.setWavetype(wavetype.get())
iio.enableOutput(True)

# enter main loop
window.mainloop()

