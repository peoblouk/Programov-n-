# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 10:10:43 2013


"""

"""
Úkol:
    1) Graf fce y=x**3-2*x**5+x-1 > plná čára + kulaté body
    2) Seznam 20-ti náhodných bodů pomocí čtverečků
"""
from pylab import *

# Úkol 1



x=arange(-10,10,0.2) # vektor x od - 10 do 10, krok 0.5

y=x**3-2*x**5+x-1

grid (True) # mřížka
title("Graf funkce: y=x**3-2*x**5+x-1")  # jméno
xlabel("Osa x")
ylabel("Osa y")
#ylim(-5,40) #limity pro osu y
plot(x,y) # vložení údajů
plot(x,y,'go')



# Úkol 2

"""
x=randn(20)
y=randn(20)
plot(x,y,'go')
show()
"""