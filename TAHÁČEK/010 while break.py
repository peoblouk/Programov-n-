# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011


"""
"""
continue - přeruší aktuální iteraci, cyklus 
           pokračuje další iterací
break - přeruší vykonávání cyklu
"""           

#co bude dělat tento cyklus a kdy skončí?
import random
x=1
while x<>10:
    x=random.randint(2,10)
    if x%2==0:
        continue
    print x
    if x==5:
        break

""" 
Úkol:
1) Načtěte číslo a spočítejte je ciferný součet.
2) Naprogramujte hru myslím si číslo.
   Rozšíření: Vypsat počet pokusů.
"""

