# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 08:26:32 2013


"""

from pylab import *

x=arange(-3,3,0.01)
y1=x**2-1
y2=2*x+1
fill_between(x,y1,y2,where=(y2>y1), facecolor="#00aac2")
plot(x,y1, "#987654")
plot(x,y2, "#753cf0")
text(0.4,1,u"Blááá", fontsize="20", color="#ffffff")
annotate(u"Vybarvenééé",xy=(0.3,1.5),xytext=(-2,6),arrowprops=dict(facecolor="black",shrink=0.1))

grid(True)
show()