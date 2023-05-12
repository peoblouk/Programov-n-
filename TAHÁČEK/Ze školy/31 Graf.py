# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:46:31 2013


"""


"""
Úkol:
    1) Zobrazte graf funkci y=cos(x)
    2) Změnte parametry fnkce na y1=2cos(3x)-1
    a přidejte ji do grafu
    
"""

from pylab import *
x=arange(0,4*pi,0.1) # vektor x od - 10 do 10, krok 0.5

y=cos(x)
y1=2*cos(3*x)-1


grid (True) # mřížka
title("Graf funkce cosinus")  # jméno
xlabel("Osa x")
ylabel("Osa y")
#ylim(5,40) #limity pro osu y
plot(x,y,x,y1) # vložení údajů
show() # zobrazení grafu