# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:25:45 2013


"""

"""

N-tice (tuple)
- vytvářejí se pomocí ()
- jsou neměnné
- nemají žádné metody (jako např. pop(), ...)

"""
"""
tuple()
print tuple

x=(3, "ahoj", 4.7, None)
print x

print x[1]
"""

"""

Úkol:
    1) Vygenerujte seznam s 10-ti tříprvkovými n-ticemi.
       Náhodná čísla  z intervalu <0,1>, 
       Vypište n-tice pod sebou
       
"""

import random
S=[]
for i in range(10):
    S.append((random.randint(0,1),random.randint(0,1),random.randint(0,1)))
for i in S:
    print i

