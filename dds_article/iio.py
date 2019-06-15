import sys

#
# This file provides routines to control the hardware via the iio
# device drivers, ad their entries in the /sys tree
# This is the least amount of code requirted to control the generator
# all the other files simply provice a GUI front end
# If you want to design your own GUI, or embed the generator in another system,
# this is all you need
#

## dds registers
frequency_register='/sys/bus/iio/devices/iio:device1/out_altvoltage0_frequency0'
wavetype_register='/sys/bus/iio/devices/iio:device1/out_altvoltage0_out0_wavetype'
enable_register='/sys/bus/iio/devices/iio:device1/out_altvoltage0_out_enable'

# dac registers
voltage_register='/sys/bus/iio/devices/iio:device0/out_voltage0_raw'

# disable calls to hardware in test mode
test=(len(sys.argv)>1)

# enable output
def enableOutput(enable):
    if test==False:
        fo=open(enable_register,'w')
        if enable==True:
    	    fo.write('1')
        else:
            fo.write('0')

# write frequency in Hz to DDS
def setFrequency(frequency):
    output=str(int(frequency))
    #print('F='+output)
    if test==False:
        fo=open(frequency_register,'w')
        fo.write(output)

# write to DDS one of 'sine',square',triangle
def setWavetype(wavetype):
    #print('T='+wavetype)
    if test==False:
        fo=open(wavetype_register,"w")
        fo.write(wavetype)

# DAC full scale is 4096 (2^12), so scale from
# 5000 millivolts 1.23=4095/10000
def setVoltage(voltage):
    output=str(int(voltage*4095/10000))
    #print('V='+output)
    if test==False:
        fo=open(voltage_register,'w')
        fo.write(output)


