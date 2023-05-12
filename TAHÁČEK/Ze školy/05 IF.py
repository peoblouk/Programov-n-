# -*- coding: utf-8 -*-
"""
Created on Wed Oct 03 09:43:59 2012


"""

"""
Podmíňěný příkaz (if) - umožńouje rozhodování
if PODMÍNKA1:
    odsazené příkazy (blok1)
elif PODMÍNKA2:
    odsazené příkazy (blok2)
elif ...
    ...
else:
    odsazené příkazy (blokN)
    
"""

x=input(u"Zadej číslo: ")
if x>0:
    print u"Číslo je kladné!"
    print u"Provedla se první větev příkazu IF"
elif x==0:
    print "Nula"
else:
    print u"Číslo je záporné"
    
    
"""
Relační operátory

> větší
< menší
= rovno
>= větší nebo rovno
<= menší nebo rovno
<> nerovno
!= nerovno

"""