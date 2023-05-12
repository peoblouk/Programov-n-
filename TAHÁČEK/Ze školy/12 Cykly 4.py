# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 09:10:12 2012


"""

cislo=input(u"Zadejte číslo: ")
soucet=0

while cislo>0:
    zbytek=cislo%10
    soucet+=zbytek  #příčetní zbytku k součtu - k 1 proměnné#
    cislo=cislo/10

print u"Ciferný součet je: ", soucet