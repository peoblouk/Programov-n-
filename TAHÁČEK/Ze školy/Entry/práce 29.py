# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:23:30 2013


"""

from Tkinter import*

hlavni=Tk()

t=StringVar()
vstup=Entry(hlavni,textvariable=t)
vstup.pack()

def Smaz():
    t.set("Prazdny text")
tlacitko=Button(hlavni,text="Smazani!",command=Smaz)
tlacitko.pack()

mainloop()