# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:17:28 2012


"""
"""
fill_between(x,y1,y2) - vyplní plochu mezi dvěma čarami, druhá je
                        nepovinná
                      - lze doplnit o podmínku   
"""

from pylab import *

x=arange(0,2*pi,0.01)
y1=2*cos(7*x)

y2=3*sin(5*x)

plot(y1,y2)
#plot(x,y2)
#fill_between(x,y1,y2,facecolor="#ff0247")
#fill_between(x,y1,y2,where=(y2<0),facecolor="b")
#fill_between(x,y1,y2,where=(y2>=0)*(x<=1),facecolor="g")

grid()
show()

"""
Úkol:
1) Vyplňte plochu mezi fcemi cos(x) a sin(2*x) fialovou 
   barvou v hexadecimálním tvaru.
"""   