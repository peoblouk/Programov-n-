# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 08:44:39 2013


"""

from pylab import *

x=arange(0,2*pi,0.01)
y1=(-(x-2)**2+4)
y2=x

axis([-1,5,0,5])
plot(x,y1,'black')
plot(x,y2,'--')
fill_between(x,y1,y2,where=(y1>y2),facecolor="#00ff00")
annotate(u"Vybarvená plocha",xy=(1.5,2.5),xytext=(2,1),arrowprops=dict(facecolor="black",shrink=0.2))

legend(("y1=-(x-2)**2+4","y2=x"),"upper right", shadow=True)
grid(True)
show()