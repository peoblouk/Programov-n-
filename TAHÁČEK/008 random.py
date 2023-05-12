# -*- coding: utf-8 -*-
"""
Generování náchodných čísel
---------------------------
V programech často potřebujeme získat náhodné číslo:
- počítač má vybrat z několika rovnocenných možností
  (třeba náhodné testové otázky, tahy hráče, házení
   kostkou, zamíchání karet)

Potřebujeme knihovnu random 
randint(od,do) - vygeneruje náhodné číslo z intervalu <od,do>
               - od a do musí být celá čísla, mohou být i záporná 

"""


import random

x=random.randint(1,6)
print "Kostka hodila", x

"""
Úkol:
1) Naprogramujte hru KÁMEN, NŮŽKY, PAPÍR.
   Hraje člověk proti počítači.

Můžete vytvořit pomocné proměnné:
kamen=1
nuzky=2
papir=3

Náhled programu:
Hrajeme hru kámen, nůžky, papír
1) Kámen
2) Nůžky
3) Papír
Zadej svou volbu:
    
vyhodnocení + výpis

"""