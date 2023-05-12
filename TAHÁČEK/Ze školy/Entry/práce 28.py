# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:20:23 2013


"""

from Tkinter import*

hlavni=Tk()

vstup=Entry(hlavni)
vstup.pack()

def Smaz():
    vstup.delete(2,4)
    vstup.insert(1,"gr")
    
tlacitko=Button(hlavni,text="Sifruj!",command=Smaz)
tlacitko.pack()

mainloop()

