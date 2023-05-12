# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 08:21:48 2014


"""

from Tkinter import *

hlavni = Tk()


vstup = Entry(hlavni, width=20)
vstup.place(relx=0.5, y=25, anchor=SE )
napis=Label(hlavni, text="")
napis.place(x=85, y=45)

def Vypocet():
    x=int(vstup.get())
    napis["text"]=str(x**2)
    
tlacitko = Button(hlavni, text=u"Druhá mocnina", command=Vypocet)
tlacitko.place(x=60, y=65)
hlavni.mainloop()

