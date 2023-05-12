# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:47:57 2013


"""

"""
Opakování seznamy:
1) Vygenerujte seznam 10-ti náhodný čísel <50;100>.
   Seznam vytřiďte a vypište. 
   Odeberte 2. prvek v seznamu a znovu vypište.
   Vypište hodnotu na pozici 5.
   Vložte hodnotu 70 na pozici 6.
   Odstraňte ze seznamu číslo 60 (pokud tam je).
    
"""
#1

import random

sez=[]
for i in range (10):
    sez.append(random.randint(50,100))

sez.sort()
print u"Vygenerováno a seřazeno: ", sez

sez.pop(1)
print u"Odstraňěno 2. číslo: ", sez

print u"Vypsáno 5. číslo: ", sez[4]

sez.insert(5,70)
print u"Na 6. pozici vloženo číslo 70: ", sez


if 90 in sez:
    sez.remove(90)
print u"Číslo 90 pryč: ", sez