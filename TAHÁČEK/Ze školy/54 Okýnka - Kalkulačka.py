# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:11:00 2013


"""

from Tkinter import *

Okno=Tk()
Okno.title("Kalkulačka")

Napis = Label(Okno, text=u"KALKULAČKA", font=("Arial", 25)) 
Napis.pack(padx=5, pady=3)

###

Ramecek1 = Frame(Okno)
Ramecek1.pack()

Napis1 = Label(Ramecek1, text=u"1. číslo") 
Napis1.pack(side="left", padx=5, pady=3)

Vstup1 = Entry(Ramecek1)
Vstup1.pack(side="right", padx=5, pady=3)

###

Ramecek2 = Frame(Okno)
Ramecek2.pack()

Napis2 = Label(Ramecek2, text=u"2. číslo") 
Napis2.pack(side="left", padx=5, pady=5)

Vstup2 = Entry(Ramecek2)
Vstup2.pack(side="right", padx=5, pady=5)

###
# Tlačítka

def Plus():
    a=int(Vstup1.get())
    b=int(Vstup2.get())
    c=a+b
    t.set(c)

def Minus():
    a=int(Vstup1.get())
    b=int(Vstup2.get())
    c=a-b
    t.set(c)

def Krat():
    a=int(Vstup1.get())
    b=int(Vstup2.get())
    c=a*b
    t.set(c)

def Deleno():
    a=int(Vstup1.get())
    b=int(Vstup2.get())
    c=a/b
    t.set(c)

def Zbytek():
    a=int(Vstup1.get())
    b=int(Vstup2.get())
    c=a%b
    t.set(c)


###

Ramecek3 = Frame(Okno)
Ramecek3.pack()

Tlacitko1 = Button(Ramecek3, text="+", width="5", heigh="2", command=Plus)
Tlacitko1.pack(side="left")

Tlacitko2 = Button(Ramecek3, text="-", width="5", heigh="2", command=Minus)
Tlacitko2.pack(side="left")

Tlacitko3 = Button(Ramecek3, text="X", width="5", heigh="2", command=Krat)
Tlacitko3.pack(side="left")

Tlacitko4 = Button(Ramecek3, text="/", width="5", heigh="2", command=Deleno)
Tlacitko4.pack(side="left")

Tlacitko5 = Button(Ramecek3, text="%", width="5", heigh="2", command=Zbytek)
Tlacitko5.pack(side="left")

###
#KONEC
Ramecek5 = Frame(Okno)
Ramecek5.pack(padx=5, pady=5)

Tlacitko6 = Button(Ramecek5, text="KONEC", width="15", heigh="2", command=Okno.quit)
Tlacitko6.pack(side="left")

###

Ramecek4 = Frame(Okno)
Ramecek4.pack()

Napis3 = Label(Ramecek4, text=u"Výsledek", font="15") 
Napis3.pack(side="left", padx=5, pady=2)

t=StringVar()

Vysledek = Entry(Ramecek4, textvariable=t, state="readonly")
Vysledek.pack(side="right", padx=5, pady=2)

###


Okno.mainloop()