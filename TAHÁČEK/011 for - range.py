# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 09:17:29 2011


"""
"""
Cyklus for
----------
- jedná se o cyklus s řídící proměnnou
- dopředu je znám počet opakování
- nemůže nastat nekonečný cyklus

Princip
- řídící proměnná postupně nabývá všech hodnot z
  pevně dané množiny
- pro každou hodnotu se vykoná jedna iterace  

Pozn!
Fce range() pracuje pouze s celými čísly.
Lze použít i záporná čísla.

for i in [množina hodnot]:
    tělo cyklu
"""
"""
for i in [1,3,"text",9,1000]:
    print i
"""
"""
mnozina="Python"
for t in mnozina:
    print t

"""
"""
for i in range(10):     #[0,1,2,...,9]
     print i,"Karel"
#pocatecni hodnota i=0
#krok=1
#koncova hodnota i=9



print ""

for i in range(3,10):
    print i,". Karel"    
#pocatecni hodnota i=3
#krok=1
#koncova hodnota i=9
"""
"""
print ""
for i in range(100,10,-5):  #[100,95,80,...15]
    print i,". Karel"  

#pocatecni hodnota i=100
#krok=-5
#koncova hodnota i=25
"""
"""
Úkol:
1) Načtěte číslo x a vypište pod sebou x hvězdiček.
2) Vypište posloupnost čísel 52, 54, ..., 78.
3) Vypište náhodný počet (1-50) náhodných čísel (1-100).
4) Načtěte číslo a vypište všechny jeho dělitele.
5) Zjistěte, zda zadané číslo je prvočíslo.
"""
import random
pocet=random.randint(1,50)

for i in range(pocet):
    cislo=random.randint(1,100)
    print cislo
