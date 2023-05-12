# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:22:53 2013


"""

import random

x=0
generator=[]
while x<6:
    cislo=random.randint(1,49)
    if generator.count(cislo)<1:
        x+=1
        generator.append(cislo)

generator.sort()
print generator



pocet=0
tip=[]
while pocet<6:
    cislo=input(u"Zadejte číslo od 1 do 49: ")
    if tip.count(cislo)<1:
        pocet+=1
        tip.append(cislo)

tip.sort()


print tip
print generator

kolik=0
for cislo in tip:
    if cislo in generator:
        kolik+=1
        
print u"Udádl jsi ",kolik, u"čísel"