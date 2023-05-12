# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:17:33 2013


"""

"""

Ukol:
    1) Načíst číslo z klávesnice a vložit do řetězce v desítkovém i hexa tvaru
    2) Zobrazte do řetězce číslo pí tak, že celá část bude mít 2 místa 
       a desetinná 7 míst
    3) Vygenerujte seznam náhodných čísel tak, aby se některá opakovala 
       a poté odstraňte všechny duplicitní prvky.

"""
"""
#1

x=input(u"Zadejte číslo: ")
ret="Hexa cislo a desitkove cislo %x, %i" %(x,x)
print ret
"""

"""
#2
import math
x=math.pi
ret="Pi %-15.7f" %x
print ret
"""

#3

import random
sez=[]
for i in range (10):
    x=(random.randint(1,5))
    sez.append(x)


sez.sort()   
print sez

for i in sez:
    if sez.count(i) >1:
        sez.remove(i)

print sez


    