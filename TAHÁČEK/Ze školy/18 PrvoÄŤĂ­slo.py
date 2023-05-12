# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:08:12 2012


"""

a=input(u"Zadejte 1. číslo: ")
b=input(u"Zadejte 2. číslo: ")

for cislo in range (a,b+1):
   pocet=0
   for i in range (1,cislo+1):
       if cislo%i==0:
           pocet+=1

   if pocet==2:
       print cislo,