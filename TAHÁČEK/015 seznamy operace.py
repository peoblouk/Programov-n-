# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:42:31 2012


"""
"""
        Seznamy a jejich operace
append(hodnota)       - přidá hodnotu na konec seznamu
count(hodnota)        - zjistí počet výskytů dané hodnoty
insert(index, hodnota)- vloží hodnotu na pozici v seznamu
pop(index)            - odebere prvek z dané pozice
remove(hodnota)       - odebere první výskyt této hodnoty
sort()                - setřídí seznam podle velikosti

delka=len(seznam)     - zjištění velikosti seznamu
""" 


seznam=["a",2012,"c",3,1,"b"]
seznam.append(2012) 
print seznam

"""
print "Pocet 2012: ",seznam.count(2012)


seznam.insert(0,"Vlozeno") #vloží hod. na začátek
print seznam

#Pokud neuvedeme index, odebírá z konce seznamu
x=seznam.pop(0) #Odebere prvek z pozice 0
print x
print seznam

seznam.remove(2012) #Odebere první výskyt
print seznam


seznam.sort()
print seznam


print u"Seznam má",len(seznam),u"prvků."

"""

"""
Úkol:
1) Napište cyklus, který bude načítat z klávesnice 5 
   čísel a postupně je bude dávat na konec prázdného 
   seznamu. Seznam nakonec vypište.
2) Vygenerujte a vypište seznam 20-ti náhodných čísel.
3) Vygenerujte seznam 20-ti náh. čísel od 1 do 10,
   seznam setřiďte a vytvořte k němu seznam druhých
   mocnin. Oba seznamy vypište.
4) Zjistěte, kolikrát se v mocninách vyskytuje 81.
   Odstraňte všechna čísla 81 ze seznamu mocnin. 
5) Uložte do seznamu 6 náhodných hodů kostkou a zjistěte,
   jestli padla postupka tj. všechny hodnoty od 1 do 6.
6) Napište simulaci sportky. Člověk zadá 6 čísel, poté 
   počítač vylosuje také 6 čísel a vypíše, kolik čísel
   jsme uhádli. Čísla  musí být z intervalu 1-49. Čísla
   se nesmí opakovat.

DU) Zkuste napsat jakoukoli hru s kostkami pro alespoň dva 
    hráče, jeden z nich bude počítač. 
    Musí být zobrazena pravidla.
    Použijte seznam pro uchování hodů.
""" 

