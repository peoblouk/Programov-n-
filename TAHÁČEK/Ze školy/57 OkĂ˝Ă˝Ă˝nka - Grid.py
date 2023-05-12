# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 08:36:46 2014


"""

from Tkinter import *

hl_okno=Tk()          # toto vytvoří hlavní okno

jmeno=Label(hl_okno, text="Jméno:")
jmeno.grid(row=0,sticky=E)         
prijmeni=Label(hl_okno, text="Příjmení:")
prijmeni.grid(row=1,sticky=E)  
vstup1=Entry(hl_okno)
vstup1.grid(row=0,column=1)         
vstup2=Entry(hl_okno)
vstup2.grid(row=1,column=1)         
kontrola=Label(hl_okno,text="")
kontrola.grid(row=2,columnspan=2)

def Zkontroluj():
    ret1=vstup1.get()
    ret2=vstup2.get()
    ret3=ret1+" "+ret2
    kontrola["text"]=ret3
    
tlacitko1=Button(hl_okno,text="Kontrola",command=Zkontroluj)
tlacitko1.grid(row=3,sticky=W)
tlacitko2=Button(hl_okno,text="Konec",command=hl_okno.quit)
tlacitko2.grid(row=3,column=1,sticky=E)

hl_okno.mainloop()       


