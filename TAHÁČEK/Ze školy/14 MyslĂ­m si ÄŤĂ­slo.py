# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 09:36:05 2012


"""

import random
x=random.randint(1,100)
tip=input(u"Zvol číslo od 1 do 100: ")


while tip<>x:
    if tip>x:
        print u"Zadej MENŠÍ"
        
    else:
        print u"Zadej VĚTŠÍ"
        
    tip=input(u"Zvol nové číslo: ") 
    
print("Gratulace!!!")