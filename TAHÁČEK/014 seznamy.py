# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:45:15 2011


"""
"""
                Seznamy
- uvádějí se v [], jednotlivé hodnoty se oddělují čárkou
- mohou obsahovat libovolná data i další seznamy
"""

seznam=[4,2,7]    #prázdný seznam
print seznam    



seznam=[3,"Python",3.0,[1,0,1],False,1000]
print seznam    


print seznam[3]  #práce s jedním prvkem pomocí indexu



seznam[2]="Vanoce" #přiřazení
print seznam  


for i in seznam:
    print i,

print
print seznam[3][0]  #práce s vnořeným indexem



seznam=seznam+seznam #spojování seznamů
print seznam    



seznam=[1,"a"]*10 #násobení seznamu konstantou
print seznam    


"""
print seznam[:4] #podseznam [0..3]
print seznam[4:] #podseznam [4..n]
print seznam[1:4] #podseznam [1..3]
print seznam[1:6:2] #podseznam [1..5] každý 2. prvek
print seznam[-2:]
"""


"""
Úkol:
1) Vytvořte 5-ti prvkový seznam obsahující nuly a 
   vypište jej.
   Pomocí cyklu načtěte 5 nových hodnot a přepište 
   nuly v seznamu těmito novými hodnotami.
   Seznam vypište.
2) Pomocí cyklu najděte v seznamu nejmenší prvek.
"""
