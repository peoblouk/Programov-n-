# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 09:54:43 2013


"""

from Tkinter import *

hlavni=Tk()

def Vypis():
    print u"Proběhl vypis"
    hlavni.after(500,Vypis)

Vypis()

hlavni["bg"]="#124578"

mainloop()


"""
Úkol:
1) Každou sekundu změňte barevné pozadí hlavního okna.
"""