# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 10:01:50 2013


"""

from pylab import *
x=[1,2,3,4]
y=[1,4,9,16]

axis([0,6,0,18]) # rozsah x a y

plot(x,y,'rs')   # rs = pouze body (červené čtverečky)

plot(x,y,'g:')   # g = zelená čára

"""
Styly:
    ro - červená kolečka
    bs - modré čtverečky
    g^ - zelené trojúhelníky
    y  - žlutá čára
"""


show()