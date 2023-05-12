# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:17:15 2013


"""

from pylab import *

x=arange(1,3*pi,0.01)
y1=sin(x)

fill(x,y1,"#ff00dd")
plot(x,y1,"#000000",linewidth=5,)
grid(True)

show()