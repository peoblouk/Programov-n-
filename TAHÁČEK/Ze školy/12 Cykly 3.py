# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:09:44 2012


"""

import random
x=1
while x<>10:
    x=random.randint(2,10)
    if x%2==0:
        continue
    print x
    if x==5:
        break
    