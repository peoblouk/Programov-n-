# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:44:08 2012


"""
"""
text (x,y,řetězec) 
     - umístí řetězec na zvolené souřadnice v grafu
     - automaticky se vkládá nad y a vpravo od x, ale způsob
       zarovnání můžeme změnit pomocí nepovinných parametrů

annotate (řetězec,xy=(x,y),xytext=(x,y),arrowprops=dict(facecolor=color,shrink=x))
     - poznámka s šipkou
     - šipka ukazuje od poznámky na bod xy
     - poznámka je umístěna na souřadnicích xytext
     - vlastnosti šipky se definují v arrowprops, shrink znamená zkrácení
       šipky v obou směrech, uvádí se jako desetinné číslo (0.25 = čtvrtina)
"""

from pylab import *

x=arange(-3,3,0.01)
y1=x**2-1
y2=2*x+1
fill_between(x,y1,y2,where=(y2>y1), facecolor="gray")
plot(x,y1,"black")
plot(x,y2,"black")
text(0,0,u'Popisek',fontsize="16", color="blue")
#horizontalalignment='right',verticalalignment='center',color="r")

annotate(u'Vybarvená plocha', xy=(-2,8), xytext=(-1,6),
            arrowprops=dict(facecolor='g', shrink=0.2))
grid(True) 
show()

"""
Úkol:
1) Nakreslete funkci y1=-(x-2)^2 + 4.
   Vykreslete přímku y2=x čárkovanou čarou.
   Vybarvěte plochu mezi oběma čarami tam, kde platí
   že (y1>y2).
   Doplňte šipku s popisem směřující přibližně na střed
   vybarvené plochy.
   Přidejte legendu s popisem obou čar.
"""    