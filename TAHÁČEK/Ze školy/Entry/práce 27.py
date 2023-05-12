# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Documents and Settings\roz30375\.spyder2\.temp.py

Zkuste vygenerevat seznam desíti náhodných čísel, které 
budou od 50 do 100, seznam setřídit a vypsat.

Odeberte druhý prvek v seznamu a znovu vypiště seznam.

Vypište hodnotu na pozici 5.

Přidejte na 6. pozici číslo 70.

Odstraňte ze seznamu číslo 52(zda se vyskytuje).

"""

from random import *

seznamolosos=[]
for i in range(10):
    seznamolosos.append(randint(50,100))
seznamolosos.sort()
print seznamolosos

seznamolosos.pop(1)
print seznamolosos

print seznamolosos[4]

seznamolosos.insert(5,70)
print seznamolosos

if seznamolosos.count(52)>0:
    seznamolosos.remove(52)
print seznamolosos