# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:51:56 2013


"""

"""
Napište aplikaci, která bude obsahovat: 
-Label (Tajná šifra)
-Entry pro vstup textu
-Button šifruj vstup
-Label pro výstup
-Button quit

->Po stisku tlačítka se řetězec ze vstupu zašifruje libovolnou metodou 
a výsledek se zobrazí v Labelu
"""

from Tkinter import *

hlavni=Tk()

popisek1=Label(hlavni,text="Tajná šifra",fg="red")
popisek1.pack()

popisek2=Label(hlavni,text="Zadej text!",fg="red")
popisek2.pack()

ramecek=Frame(hlavni, bd=2, width=100, height=50, relief="sunken")
ramecek.pack()

vstup=Entry(ramecek)
vstup.pack(side="right", padx=10, pady=10)

napis=Label(hlavni,text="")
napis.pack()


def sifra():
     x=vstup.get()
     napis["text"]=str(x)+str(x)

Tlacitko1=Button(hlavni, text="Šifruj vstup!", width=10, height=2, command=sifra)
Tlacitko1.pack()


popisek2=Label(hlavni,text="",fg="red")
popisek2.pack()

Tlacitko2=Button(hlavni, text="Quit", width=10, height=1, command=hlavni.quit)
Tlacitko2.pack()


hlavni.mainloop()