# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:23:26 2014


"""

from Tkinter import *
from tkMessageBox import *

"""

hlavni = Tk()

ramecek=Frame(hlavni, bd=2, relief="ridge")
ramecek.grid(row=0)

a = IntVar()
Radiobutton(ramecek,text="Jedna",variable=a, value=1).pack()
Radiobutton(ramecek,text="Dva",variable=a, value=2).pack()
Radiobutton(ramecek,text=u"Tři",variable=a, value=3).pack()

def tisk():
    print a.get()
    
def nastav():
    a.set(2)
    
tlacitko=Button(hlavni, text="Kontrola", command=tisk)
tlacitko.grid(row=1)

tlacitko2=Button(hlavni, text="Nastav", command=nastav)
tlacitko2.grid(row=2)


mainloop()

"""


"""

ÚKOL:
    
    1) Vytvořte skupinutří radiobuttonů s různými pozdravy
       Přidejte tlačítko 'Pozdrav', po jehož stisku se zobrazí
       hláška s daným pozdravem (showinfo).
       
"""


hlavni = Tk()

ramecek=Frame(hlavni, bd=5, relief="ridge")
ramecek.grid(row=0, column=0)

a = IntVar()
Radiobutton(ramecek, text="Ahoj",  variable=a, value=1).pack(anchor=W)  
Radiobutton(ramecek, text="Nazdar",variable=a, value=2).pack(anchor=W)  
Radiobutton(ramecek, text=u"Čus",  variable=a, value=3).pack(anchor=W)

def Pozdrav():
    if a.get()==1:
        showinfo("","Ahoj")
    if a.get()==2:
        showinfo("","Nazdar")
    if a.get()==3:
        showinfo("",u"Čus")
    
       
tlacitko=Button(hlavni, text="Kontrola", command=Pozdrav)
tlacitko.grid(row=1)

mainloop()