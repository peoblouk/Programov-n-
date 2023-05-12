# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:26:22 2013


"""

# Vrátí seznam náhodných čísel

import random

def VratSeznam(pocet,od,do):
    Seznam=[]
    for i in range(pocet):
        Seznam.append(random.randint(od,do))
    return (Seznam)

print VratSeznam(3,1,10)