# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:11:52 2013


"""

from Tkinter import *
from random import *


Okno=Tk()

def Priklady():
    a=randint(0,100)
    b=randint(0,100)
    c=a+b
    if (a+b)<=100:
        print a, "+", b, "="



Priklad = Button(Okno, text=u"Příklad", command=Priklady)
Priklad.pack()

Napis = Label(Okno, text=u"Zadejte výsledek:")
Napis.pack()

Vysledek = Entry(Okno)
Vysledek.pack()

Overit = Button(Okno, text=u"Ověřit výsledek")
Overit.pack()

Konec = Button(Okno, text="Konec", command=quit)
Konec.pack()





Okno.mainloop()