# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:06:32 2013


"""


"""
Úkol:
    1) Napište funkci AnaX, která bude mít 2 pevné parametry.
    2) Napište funkci Linear, která vrátí řešení lienární rovnice.
       (Ax+B=0)
    3) Napište funkci Prumer, která spočítá aritmetický průměr 
       ze trí čísel.
    4) Napište fci Kostka, která vrátí hodnotu hodu kostkou.
"""

# Úkol 1

def AnaX(cislo,mocnina):
    return cislo**mocnina
    
print AnaX(2,2)


# Úkol 2

def Linear(a,b):
    return (-b)/a
    
print Linear(2,-4)


# Úkol 3

def Prumer(x,y,z):
    return ((x+y+z)/3)

print Prumer(1,3,5)

# Úkol 4

import random
def Kostka():
    return random.randint(1,6)

print Kostka()


