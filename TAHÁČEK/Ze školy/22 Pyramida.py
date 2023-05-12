# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 09:41:14 2012


"""

n=input(u"Zadejte velikost pyramidy: ")
while (n<1)or(n>20):
    n=input("CHYBA! Zadejte cislo od 1 do 20: ")

for y in range (n):
    for m in range (n-y):
        print " ",
    for x in range (2*y+1):
        print ".",
    print ""

