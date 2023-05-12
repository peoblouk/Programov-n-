# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:16:04 2012


"""

"""
        Seznamy:
- hranaté závorky []
- jednotlivé hodnoty se oddělují čárkou
- mohou obsahovat libovolná data
- 
"""



seznam=[] #prázdný seznam
print seznam

seznam=[3,"Python",3.0]
print seznam

print seznam[1] #vytiskne se prvek 1 (0,1,2...)

seznam[2]="Vanoce" #přiřazení
print seznam


seznam=seznam+seznam #sčítání seznamů
print seznam

seznam=seznam*2 #násobení seznamu číslem
print seznam



print seznam[:4] #do 4. prvku pouze
                 # podseznam [0...3]
print seznam[4:] #od 4. prvnku pouze
                 # podseznam [4...x]
print seznam[1:4]