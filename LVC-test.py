# Python script to run the siglent DC power supply for automated testing of the LVC cutoff
# Connection over USB
#
#
import pyvisa 
#import tkinter
import time
import usb.core

# obtain connected devices ID numbers
devices = pyvisa.ResourceManager()
print(devices)
print(devices.list_resources())

# sleep times
stp = .2

#define testing equipment
# DC PSU
psu = devices.open_resource('USB0::1155::30016::SPD3XIDD4R6121::0::INSTR')
# DMM
dmm = devices.open_resource('USB0::62700::60984::SDM36GBC6R0008::0::INSTR')

# add these or else 
psu.write_termination='\n'
psu.read_termination='\n'
dmm.write_termination='\n'
dmm.read_termination='\n'

psu.write('*IDN?')
time.sleep(stp)
SDLIDN = psu.read_bytes(1000, break_on_termchar='\r\n')
#print ("Load: " + str(SDLIDN).rstrip())

# set PSU channel 1 voltage
voltage = 0
current = 2
psu.write('CH1:CURR ' + str(current))
time.sleep(stp)

#max voltage in Volts
max = 7
i = 0
while i < (max * 100):
    psu.write('CH1:VOLT ' + str(voltage))
    time.sleep(stp)
    voltage = voltage + .01
    i = i + 1


