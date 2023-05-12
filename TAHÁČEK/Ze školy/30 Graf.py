# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:26:37 2013


"""

from pylab import *
x=arange(-10,10,0.5) # vektor x od - 10 do 10, krok 0.5

y1=2*x+1
y2=x**2
y3=x**4


grid (True) # mřížka
title("Graf bla bla")  # jméno
xlabel("Osa x")
ylabel("Osa y")
ylim(-5,40) #limity pro osu y
plot(x,y1, label="y1")  # vložení údajů
plot(x,y2, label="y2")
plot(x,y3, label="y3")

legend(("Prvni","Druha","Treti"),"lower right", shadow=True) #center , upper, lower, best
show() # zobrazení grafu




