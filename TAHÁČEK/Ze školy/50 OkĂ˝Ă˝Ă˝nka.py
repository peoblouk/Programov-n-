# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 08:38:06 2013


"""

from Tkinter import *

def vypis():
    print u"Lokomotiva sedí na zmrzlině a plete bábovku"
    
def zmena():
       Napis["text"]=Napis["text"]+"!"
    
    
    
Okno = Tk()                                                       # Vytvoří hlavní okno

Napis = Label(Okno, text="Blah blah blah", fg="blue", bg="#00CBCF") # Vytvoří modrý nápis s pozadím 
Napis.pack()

Tlacitko1 = Button(Okno, text="Vypnout", command=Okno.quit)       # Vytvoří tlačítko, které zavírá program
Tlacitko1.pack()                                                  # Aby se tlačítko zobrazilo

Tlacitko2 = Button(Okno, text=u"Výpis do konzole", command=vypis)
Tlacitko2.pack()

Tlacitko3 = Button(Okno, text=u"Změna nápisu", width=30, heigh=3, command=zmena)
Tlacitko3.pack()


Okno.mainloop()                                                   # Aby se okno zobrazilo

