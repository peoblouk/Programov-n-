# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:35:07 2013


"""


from Tkinter import *

okno=Tk()

ramecek=Frame(okno, bd=2, width=100, heigh=50, relief="sunken")
ramecek.pack()

vstup=Entry(ramecek)
vstup.pack(side="right", padx=10, pady=10)

napis=Label(ramecek, text="")
napis.pack(side="right")


def Vypocet():
    x=int(vstup.get())
    napis["text"]=str(x**2)
    
    
tlacitko1=Button(ramecek, text=u"Druhá mocnina", command=Vypocet)
tlacitko1.pack(side="right", padx=10, pady=10)

okno.mainloop()

