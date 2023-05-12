# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 08:35:56 2011


"""
"""
Podmíněný příkaz (if) - umožňuje rozhodování
--------------------------------------------
if PODMÍNKA1:
    odsazené příkazy (blok1)
elif PODMÍNKA2:    
    odsazené příkazy (blok2)
elif ...
    ...    
else:
    odsazené příkazy (blokN)

Pozn. 
Části elif a else jsou nepovinné.
"""
x=input("Zadej cislo:")
"""
if x>0: 
    print "Cislo je kladne!"
    print "Provedla se prvni vetev prikazu IF"
elif x==0:
    print "Nula"
else:
    print "Cislo je zaporne"
"""
if x>0: 
    print "Cislo je kladne!"
    print "Provedla se prvni vetev prikazu IF"
if x==0:
    print "Nula"
if x<0:
    print "Cislo je zaporne"
    
"""
Relační operátory
>  větší   >= větší nebo rovno
<  menší   <= menší nebo rovno
== rovno   <>, != nerovno
"""

"""
Úkol:
1) Načtěte z klávesnice 2 čísla a zjistěte, které z
   nich je větší, nebo jestli jsou stejná.
2) Načtěte číslo a zjistěte, zda je liché či sudé.
3) Načtěte řetězec (heslo) a zjistěte jestli je rovno
   "klokan".
4) Načtěte koeficienty kvadratické rovnice, zjistětěte
   kolik má řešení a vypište její řešení.   
"""   



