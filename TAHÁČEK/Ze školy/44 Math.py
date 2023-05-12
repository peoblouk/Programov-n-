# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:55:01 2013


"""
"""

Vyjímky:    slouží k zachycení chyb a problémových stavů
Try:
- blok s kódem, kde může nastat chyba
Except:
- Blok, který se provede při chybě
Else:
- Nepovinný blok, který se provede když nenastane chyba

"""


import math

# DĚLENÍ

"""
x=8
y=3
try:
    vysledek=x/y
    print vysledek
except:
    print "Nastala chyba deleni!"
else:
    print "Deleni probehlo v poradku"
"""

# ODMOCNINA

"""
x=-8
try:
    vysledek=math.sqrt(x)
    print vysledek
except:
    print "Nastala chyba!"
"""

# OTEVÍRÁNÍ SOUBORU

"""
try:
    soubor=open('google.txt','r')
    soubor.close
except:
    print "Chybi pri otevirani soubru!"
"""

# POZE ČÍSLO

"""
try:
    x=input(u"Zadejte libovolné číslo: ")
    print u"Vaše číslo je: " ,x
except:
    print u"Zadejte pouze číslo!"
"""

# ŘETĚZEC NA ČÍSLO


try:
    x=int(55)
except:
    print u"Tohle není číslo"
else:
    print "Done :)"