# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:26:22 2013


"""


from Tkinter import *

"""
hl_okno=Tk()          # toto vytvoří hlavní okno

sez=[]

for i in range(20):
    txt=StringVar()
    txt.set(u"Tlačítko "+str(i))
    b=Button(hl_okno,textvariable=txt)
    sez.append(b)
    b.pack(fill=X)   

sez[13]["state"]=DISABLED

hl_okno.mainloop()
"""

"""
Úkol:
1) Pomocí obdobného mechanismu vykreslete tabulku
   o 5-ti sloupcích a 10-ti řádcích složenou z komponent
   Entry + zmenšete šířku. Použijte rozmístění Grid.
"""    

Okno=Tk()          # toto vytvoří hlavní okno

sez=[]

for x in range(10):
    for y in range(5):
        txt=StringVar()
        txt.set(u"Pozice " + str(y+1) + ":" + str(x+1))
        E=Entry(Okno,textvariable=txt)
        sez.append(E)
        E.grid(column=y, row=x)

        


Okno.mainloop()










"""
seznam=[]
for i in range(10):
    seznam.append("pokus "+str(i))
    b=Button(hl_okno,text=seznam[i])
    b.pack()
"""

"""
seznam=[]
for i in range(10):
    text=StringVar()
    text.set("pokus "+str(i))
    seznam.append(text)
    b=Label(hl_okno,textvariable=seznam[i])
    b.pack()
    
seznam[0].set("Funguje to?")
"""