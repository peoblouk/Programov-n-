# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:36:55 2012


"""

"""
        Seznamy a jejich operace

append(hodnota) - přidá hodnotu na konec seznamu
count(hodnota) - zjistí počer výskytů dané hodnoty
insert(index, hodnota) - vloží hodnotu na pozici v seznamu
pop(index) - odebere prvek z dané pozice
remove(hodnota) - odebere první výskyt této hodnoty
sort() - setřídí seznam podle velikosti


"""
"""

seznam=[2011,2010]
seznam.append(2012)
print seznam

print "Pocet 2011: ", seznam.count(2011)

seznam.insert(50,"Vlozeno") #vlozí hodnotu na pozici 1
print seznam

seznam.insert(0,"Pokus") #vlozí hodnotu na pozici 0
print seznam


x=seznam.pop(0)
print x
print seznam

seznam.remove("Vlozeno")
print seznam

seznam.sort()
print seznam

"""

"""

ÚKOL:
    1) Napiště cyklus, který bude načítat z klávesnice 5 čísel
       postupně je bude dávat na konec prázdného seznamu.
       Seznam nakonec vypiště.
       
    2) Vygenerujte a vypiště seznam 20-ti náhodných čísel.
    
"""

# ÚKOL 1


seznam=[]
x=0
while x<5:
    seznam.append(input(u"Zadejte číslo: "))
    x+=1
seznam.sort()
print u"Úkol 1: "
print seznam


# ÚKOL 2

import random
seznam=[]
x=0
while x<20:
    seznam.append(random.randint(1,100))
    x+=1
seznam.sort()
print u"Úkol 2: "
print seznam




























