# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:04:46 2013


"""
"""
subplot(x,y,z)
x = řádny
y = sloupce
z = číslo grafu

"""

from pylab import *

subplot(2,2,1)
plot([1,2,3,5], linewidth=4,)
plot([3,1,5,2])

subplot(2,2,2)
plot([3,2,6,2])

subplot(2,2,3)
plot([2,3,1,5], linewidth=2,)
plot([3,4,1,2])

subplot(2,2,4)
plot([3,1,2,1])

show()