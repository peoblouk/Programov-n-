# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:59:50 2012


"""
"""
Připojení knihovny
    1) import knihovna  -> knihovna.funkce()
    2) import knihovna as m -> m.funkce()
    3) from knihovna import * -> funkce() 
       - POZOR, může dojít k přepsání importovaných
       proměnných nebo fcí, pokud se v importovaných
       knihovnách jmenují stejně
"""

import math #připojení knihovny math

print u"Číslo pí: ", math.pi
print u"Eulerovo číslo: ", math.e


print u"Absolutní hodnota: ",math.fabs(-67.5)
print "Odmocnina: ", math.sqrt(16)

print u"Sinus 30°: ", math.sin(math.pi/180*30)
print u"Cosinus 45°: ", math.cos(math.radians(45))
print u"Tangens 45°: ", math.tan(math.radians(45))

print u"Useknutí desetinné části: ", math.trunc(61.4788)
print u"Zaokrouhlení nahoru: ", math.ceil(61.4788)
print u"Zaokrouhlení dolů: ", math.floor(61.4788)
print u"Zaokrouhlení: ", round(61.4788,3)

"""
Ukol:
1)Díváte se na strom ze vzdálenosti 100m pod 
  úhlem 20°. Jak je vysoký?
  Výsledek zaokrouhlete směrem dolů na celé metry.
  
2)Upravte program tak, aby vzdálenost a úhel mohl 
  zadat uživatel z klávesnice.

3) Navíc:
  Uživatel zadá 2 odvěsny. Spočítejte délku přepony.
  Výsledek nezaokrouhlujte.  
"""       