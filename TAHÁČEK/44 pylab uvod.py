# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:35:52 2012


"""
"""
Materiály:
http://matplotlib.org/
http://mamut.spseol.cz/matplotlib/    
    
"""    

from pylab import *
x=arange(-10,10,0.2) #vektor x od -10 do 10, krok 0.2
#print x

#x=linspace(-2,2,50) #vektor x od 0 do 1, 10 hodnot


y1=2*x+1
y2=x**2
y3=x**4

grid() #zobrazení mřížky
title("Graf funkce x3")
xlabel("Osa x") # popis osy x
ylabel("Osa y")
plot(x,y1,label="$y=2x+1$") #vložení údajů do grafu
plot(x,y2,label="$y=x^2$")
plot(x,y3,label="$y=x^4$")
ylim(-1,20) #limity pro osu y
xlim(-2,2)
#legend(loc="lower left") #zobrazení legendy umístění řetězcem nebo číslem 0-10
show() #zobrazení grafu

"""
Úkol:
1) Zobrazte graf funkce y=cos(x), interval <0,4*pi>
2) Vypočítejte hodnoty funkce y1=2cos(3x)-1 a 
   přidejte ji do grafu
"""   