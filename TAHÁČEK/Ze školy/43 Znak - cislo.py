# -*- coding: utf-8 -*-
"""
Created on Wed Apr 03 08:50:47 2013


"""

"""
znak=raw_input("Zadej znak: ")
cislo=ord(znak)                 #vypise hodnotu znaku
print cislo


cislo=input("Zadej cislo znaku: ")
znak=chr(cislo)                 #vypise znak misto cisla
print znak

"""

"""
#ASCII

for i in range(256):
    znak=chr(i)
    print znak,
    
"""
"""
Ukol:
0) Vypište abecedu z malých písmen do řádku  
1) Vygenerujte a vypište náhodný znak z abecedy (Velké 
   písmeno).
2) Vygenerujte náhodné slovo z libovolných malých písmen.
   Maximální délka je 10 a minimální 1.
3) Vygenerujte náhodné slovo z malých písmen tak, aby se 
   střídaly souhlásky a samohlásky. Slovo začíná náhodně
   samohláskou nebo souhláskou.
4) Vygenerujte náhodnou větu. Bude se skládat z náhodného
   počtu slov - min. 1 slovo, max. 15 slov. Věta začíná
   velkým písmenem a končí tečkou.
5) Vygenerujte náhodný text o zadaném množství vět a 
   uložte jej do souboru text.txt. 
6) Vytvořte si pomocný slovník. Uživatel zadá text. 
   Projděte jej a aktualizujte četnosti ve slovníku. 
   Vypište úhlednou statistiku.
"""

"""
#0

for i in range (ord("a"),ord("z")+1):
    znak=chr(i)
    print znak,

"""
"""

#1

import random
for i in range (0,1):
    i=random.randint(ord("A"),ord("Z"))
    print chr(i),

"""
"""


#2

import random
x=""
for i in range (random.randint(1,10)):
    i=chr(random.randint(ord("a"),ord("z")))
    x+=i
print x

"""


#3

from random import *

samohlasky=["a","e","i","o","u","y"]
souhlasky=[]
for i in range (ord("a"),ord("z")+1):
    if chr(i) not in samohlasky:
        souhlasky+=chr(i)

def NaVelka(pismeno):
    if ord(pismeno)>=ord("a") and ord(pismeno)<=ord("z"):
        interval=ord("a")-ord("A")
        vysledek=chr(ord(pismeno)-interval)
    else:
        vysledek=pismeno
    return vysledek

def Slovo():
    delka=randint(1,10)
    samo=randint(0,1)

    if samo==0:
        samo=True
    else: 
        samo=False

    slovo=""
    for i in range(delka):
        if samo==True:
            slovo+=samohlasky[randint(0,len(samohlasky)-1)]
            samo=not samo
        else:
            slovo+=souhlasky[randint(0,len(souhlasky)-1)]
            samo=not samo
    return slovo
    
print Slovo()

#4


def Veta():
    delka=randint(1,15)
    veta=""
    for i in range(delka-1):
        veta+=Slovo()+" "
    veta+=Slovo()+"."
    veta=NaVelka(veta[0])+veta[1:]
    return veta

print Veta()        