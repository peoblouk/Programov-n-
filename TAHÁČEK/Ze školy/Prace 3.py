# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:14:48 2013


"""

import random

sez=[]
moc=[]
for i in range (10):
    cisla=(random.randint(1,9))
    x="%2i" %(cisla)
    sez.append(x)
   
    for cisla in sez:
        y=cisla**2
    moc.append(y)


print sez
print moc
