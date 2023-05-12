# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:48:08 2012


"""
import random
DB={}
DB['Mirek']=['Mirek','Palackeho 16','Olomouc','732 675 810']
DB['Dana']=['Dana','Litovelska 7','Olomouc','775 321 405']
DB['Jana']=['Jana','Husova 7','Litovel','775 321 405']
DB['Pepa']=['Pepa','Komenskeho 9','Praha','845 207 536']
DB['Marek']=['Marek','Jarni','Olomouc','776 345 890']
DB['Michal']=['Michal','Mezice 20','Mezice','606 267 762']
DB['Petra']=['Petra','Neznama 34','Opava','731 456 789']


jmeno=0
ulice=1
mesto=2
telefon=3

#print DB["Jana"][telefon]

for klic in DB:
    print DB[klic][jmeno],DB[klic][telefon]

"""
Úkoly:
0) Přidejte do DB 1 vlastní záznam, vypište všechny údaje    
1) Vypište seznamy údajů lidí z Olomouce
2) Všechna města Olomouc nahraďte v DB za Opavu   
3) Do každého záznamu přidejte náhodný věk 
   (15-25 let) jako 5. položku seznamu
4) Odstraňte záznamy lidí, kteří nejsou z Opavy  
"""




















"""



jm=raw_input("Kdo te zajima?: ")
print DB[jm]

"""
"""
for klic in DB.keys():
    if DB[klic][mesto]=='Olomouc':
        print DB[klic]

for klic in DB.keys():
    DB[klic].append(random.randint(10000,99999))    
    print DB[klic]    
    """