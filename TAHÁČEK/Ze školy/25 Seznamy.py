# -*- coding: utf-8 -*-
"""
Created on Wed Jan 09 10:09:09 2013


"""

"""
        Úkol:
        Vygenerujte seznam 10-ti náhodných čísel od 1 do 100,
        seznam setřiďte a vytvořte k němu seznam druhých mocnin.
        Obe seznamy vypište.

"""

import random

x=[]
for i in range(10):
    x.append(random.randint(1,100))



print x
x.sort()
print x

mocniny=[]
for i in x:
    mocniny.append(i**2)

print mocniny

for i in mocniny:
    if i%2==0:
        mocniny.remove(i)

print mocniny