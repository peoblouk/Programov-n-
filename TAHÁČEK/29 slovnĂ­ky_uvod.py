# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:57:07 2012


"""
"""
Slovníky (hash, asociativní pole)
- vytvářejí se pomocí {}
- položky mají tvar INDEX(KLÍČ):HODNOTA
- indexovat můžeme pomocí lib. jednoduch. dat. typu
- indexy musí být unikátní
- k hodnotám se přistupuje pomocí klíčů
"""



x={5:'five','nic':None,'cislo':80}
print x


x['elefant']="slon"
print x


print x['elefant'][1]

del x['nic']
print x

"""
keys() - vrátí seznam klíčů ze slovníku
values() - vrátí seznam hodnot
has_key(x) - vrátí log. hodnotu, zda ve slovníku
             existuje daný klíč
"""

print x.keys() 
print x.values()
print x.has_key("elefant") 

for i in x:
    print x[i]


"""
Úkol:
1) Vytvořte si jednoduchý anglicko-český překladový 
   slovník, který obsahuje 5 položek.
   Pokuste se pomocí něj překládat uživatelské vstupy,
   pokud zadané slovo nebude ve slovníku, oznamte to
   uživateli.
"""   
