# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:17:24 2013


"""

"""

Příkaz lambda:
    - převede cokoliv na funkci bez parametru
    - můžeme tak používat volání fcí s parametrem v tláčítku 
    
"""


from Tkinter import *
from random import *

hlavni=Tk()

def Mocnina(x):
    print x*x
    
    
tlacitko1=Button(hlavni, text=u"Mocnina náhodného čísla",command=lambda:Mocnina(randint(1,10)))
tlacitko1.pack()

mainloop()