# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011


"""
"""
Cyklus while
- umožňuje opakované provádění příkazů

while PODMÍNKA:
    odsazené příkazy (blok)

Princip:
- dokud platí podmínka, bude se provádět blok
- podmínka má stejnou podobu jako u IFu
- POZOR, může nastat nekonečný cyklus!    
"""


"""

jmeno=raw_input("Zadej jmeno: ")

i=1
while i<=10:
    print str(i)+".",jmeno
    i+=1    #přičte hodnotu k proměnné i

print i

#odhadněte, co bude dělat následující cyklus

"""
import random
x=1
while x<>10:
    x=random.randint(2,10)
    print x

"""

Úkol:
1) Načítejte z klávesnice čísla, dokud nebude zadána
   0.   
2) Načtěte číslo n a sečtěte hodnoty od 1 do n
3) Vypište tabulku goniometrických funkcí pro úhly
   0 - 90° po 5-ti stupních. Pozor na nedefinované
   hodnoty. Čísla zaokrouhlete na 2 des. místa.
"""    