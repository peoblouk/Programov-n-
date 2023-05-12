 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:53:10 2012


"""
from pylab import *

x=arange(1,2*pi,0.01)
y1=sin(x)

fill(x,y1,"#00ff42")
#plot(x,y1,linewidth=3)
grid(True)
show()