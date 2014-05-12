#!/usr/bin/env python


import serial
import numpy as np
from matplotlib import pyplot as plt
ser = serial.Serial('/dev/tty.usbmodem1451', 9600)
 
plt.ion() # set plot to animated
 
ydata = [0] * 50
ax1=plt.axes()  
 
# make plot
line, = plt.plot(ydata)
plt.ylim([10,100])
 
# start data collection
while True:  
    data = ser.readline().rstrip() # read data from serial 
                                   # port and strip line endings
    if len(data.split(".")) == 2:
        ymin = float(min(ydata))-10
        ymax = float(max(ydata))+10
        plt.ylim([ymin,ymax])
        ydata.append(data)
        del ydata[0]
        line.set_xdata(np.arange(len(ydata)))
        line.set_ydata(ydata)  # update the data
        plt.draw() # update the plot


# works:   ./ard.py --port /dev/tty.usbmodem1451
  


  #old ./ard.py "/dev/tty.usbmodem1451"

  # new:  ./ard.py --port /dev/tty.usbmodem1451

  # printing serial from shell:  screen /dev/tty.usbmodem1451
