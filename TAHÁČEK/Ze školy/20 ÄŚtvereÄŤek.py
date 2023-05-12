# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 09:16:23 2012


"""

n=input(u"Zadejte velikost čtverce: ")
while (n<1)or(n>50):
    n=input("CHYBA! Zadejte cislo od 1 do 50: ")

for y in range (n):
    for x in range (n):
        print "*",
    print ""