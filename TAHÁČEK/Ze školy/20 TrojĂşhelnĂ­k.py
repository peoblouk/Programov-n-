# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 09:34:30 2012


"""


n=input(u"Zadejte velikost čtverce: ")
while (n<1)or(n>50):
    n=input("CHYBA! Zadejte cislo od 1 do 50: ")

for y in range (n+1):
    for x in range (y):
        print "*",
    print ""