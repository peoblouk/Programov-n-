# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 08:16:05 2013


"""

from pylab import *

x=arange(0,2*pi,0.01)
y1=sin(x)
y2=2*sin(x)
fill_between(x,y1,facecolor="#00ac2f")
fill_between(x,y1,y2,where=(y2>1.5)+(y2<1.5),facecolor="#f2ca00")
grid(True)
show()

