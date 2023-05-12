# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:23:05 2011


"""

import random

x=[]
for i in range(10):
    x.append(random.randint(1,100))

print x
x.sort()
print x

mocniny=[]
for i in x:
    mocniny.append(i**2)

print mocniny
