# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:52:05 2013


"""

from Tkinter import *
from random import *

"""


hlavni=Tk()

hodnota=IntVar()

def Nastav(value):
    l["text"]=str(hodnota.get())

w = Scale(from_=0, to=1000, variable=hodnota,command=Nastav, label="Stupnice")
w.pack()
l= Label(hlavni,text="0")
l.pack()





mainloop()

"""
"""
Úkol:
1) Pomocí tří posuvníků s rozsahem (0-255) a tlačítka
   nastavte barvu komponenty Frame.
2) Přidejte tlačítko, které nastaví na posuvnících
   náhodnou barvu.
"""   




Okno=Tk()

R1=IntVar()
G1=IntVar()
B1=IntVar()


def Nahodna():
    Red.set(randint(0,255))
    Green.set(randint(0,255))
    Blue.set(randint(0,255))
    
    

def Nastav(value):
    Ramecek1["bg"]="#%02x%02x%02x" % (R1.get(),G1.get(),B1.get())
    
Ramecek1 = Frame(Okno, width=100, heigh=100)
Ramecek1.pack(side=LEFT, padx=10, pady=10)  
    
Red = Scale(from_=255, to=0, variable=R1, command=Nastav, label="Red")
Red.pack(side=LEFT)

Green = Scale(from_=255, to=0, variable=G1, command=Nastav, label="Green")
Green.pack(side=LEFT)

Blue = Scale(from_=255, to=0, variable=B1, command=Nastav, label="Blue")
Blue.pack(side=LEFT)    



Ramecek2 = Frame(Okno, width=100, heigh=100)
Ramecek2.pack(side=LEFT, padx=10, pady=10)

Tlacitko1= Button(Ramecek2, text=u"Náhodná barva", command=Nahodna)
Tlacitko1.pack(padx=5, pady=5)

Tlacitko2= Button(Ramecek2, text=u"Ukončit", command=Okno.quit)
Tlacitko2.pack(padx=5, pady=5)

Okno.mainloop()
    