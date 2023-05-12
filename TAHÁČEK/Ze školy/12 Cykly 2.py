# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:03:08 2012


Součet čísel od 1 do 10
"""

a=input (u"Zadejte číslo: ")
b=input (u"Zadejte číslo: ")

soucet=0
while a<=b:
    soucet+=a
    a+=1
print "Součet je ", soucet