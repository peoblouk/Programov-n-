# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 08:46:16 2014

@author: spu30141

"""

from Tkinter import *
from tkMessageBox import *

##### KLIKÁNÍ JAK O ŽIVOT #####

def Klik0(udalost):
    Entry0.insert(END,0)

def Klik1(udalost):
    Entry0.insert(END,1)
    
def Klik2(udalost):
    Entry0.insert(END,2)

def Klik3(udalost):
    Entry0.insert(END,3)

def Klik4(udalost):
    Entry0.insert(END,4)

def Klik5(udalost):
    Entry0.insert(END,5)
    
def Klik6(udalost):
    Entry0.insert(END,6)

def Klik7(udalost):
    Entry0.insert(END,7)

def Klik8(udalost):
    Entry0.insert(END,8)

def Klik9(udalost):
    Entry0.insert(END,9)
    
def KlikPlus(udalost):
    Entry0.insert(END,"+")

def KlikMinus(udalost):
    Entry0.insert(END,"-")

def KlikKrat(udalost):
    Entry0.insert(END,"*")
    
def KlikDeleno(udalost):
    Entry0.insert(END,"/")

def KlikMezera(udalost):
    Entry0.insert(END," ")

def KlikTecka(udalost):
    Entry0.insert(END,".")
    
def KlikDEL(udalost):
    x = (len(Entry0.get()))
    Entry0.delete(x-1)

def KlikCLR(udalost):
    Entry0.delete(0, END)

def KlikMoc(udalost):
    Entry0.insert(END,"moc")
    
def KlikRoot(udalost):
    Entry0.insert(END,"sqrt")


##### VÝPOČER #####

def Vypocet():
    Vstup = Entry0.get()
    Vstup=Vstup.replace(",",".")
    
    seznam=Vstup.split()
    zasobnik=[]
    
    while len(seznam)>0:
        prvek=seznam.pop(0)
        if prvek=="+":
            zasobnik.append(zasobnik.pop()+zasobnik.pop())
        elif prvek =="-":
            zasobnik.append(zasobnik.pop()-zasobnik.pop())
        elif prvek =="*":
            zasobnik.append(zasobnik.pop()*zasobnik.pop())
        elif prvek =="/":
            zasobnik.append(zasobnik.pop()/zasobnik.pop())
        elif prvek =="moc":
            zasobnik.append(zasobnik.pop()**zasobnik.pop())
        elif prvek =="sqrt":
            zasobnik.append(sqrt(zasobnik.pop()))
        else:
            try:
                zasobnik.append(float(prvek))
            except:
                showerror(u"Chyba!",u"Zadávejte pouze povolené operace a čisla")
                exit
            
    if len(zasobnik)!=1:
        showerror(u"Chyba!",u"Málo operací")
    else:
        showinfo(u"Výsledek", zasobnik[0])


"""

##### ZKRATKY #####

MOCNINA     moc
ODMOCNINA   sqrt
DELETE      DEL
CLEAR       CLR
PLUS        + 
MINUS       - 
KRÁT        * 
DĚLENO      /
MEZERA      __
TEČKA       .

"""

    
Okno=Tk() 

Ramecek1=Frame(Okno)
Ramecek1.grid(pady=3, padx=5, sticky=W+E+S+N)

Entry0=Entry(Ramecek1, font=("Arial",13))
Entry0.grid(row=0,pady=5, columnspan=4, sticky=W+E) 
   
tlacitko1=Button(Ramecek1,text="1",width=5, heigh=2)
tlacitko1.bind("<Button-1>", Klik1)
tlacitko1.grid(row=1,column=0)

tlacitko2=Button(Ramecek1,text="2",width=5, heigh=2)
tlacitko2.bind("<Button-1>", Klik2)
tlacitko2.grid(row=1,column=1)
    
tlacitko3=Button(Ramecek1,text="3",width=5, heigh=2)
tlacitko3.bind("<Button-1>", Klik3)
tlacitko3.grid(row=1,column=2)

tlacitko4=Button(Ramecek1,text="+",width=5, heigh=2)
tlacitko4.bind("<Button-1>", KlikPlus)
tlacitko4.grid(row=1,column=3)

tlacitko5=Button(Ramecek1,text="4",width=5, heigh=2)
tlacitko5.bind("<Button-1>", Klik4)
tlacitko5.grid(row=2,column=0)

tlacitko6=Button(Ramecek1,text="5",width=5, heigh=2)
tlacitko6.bind("<Button-1>", Klik5)
tlacitko6.grid(row=2,column=1)
    
tlacitko7=Button(Ramecek1,text="6",width=5, heigh=2)
tlacitko7.bind("<Button-1>", Klik6)
tlacitko7.grid(row=2,column=2)

tlacitko8=Button(Ramecek1,text="-",width=5, heigh=2)
tlacitko8.bind("<Button-1>", KlikMinus)
tlacitko8.grid(row=2,column=3)

tlacitko9=Button(Ramecek1,text="7",width=5, heigh=2)
tlacitko9.bind("<Button-1>", Klik7)
tlacitko9.grid(row=3,column=0)

tlacitko10=Button(Ramecek1,text="8",width=5, heigh=2)
tlacitko10.bind("<Button-1>", Klik8)
tlacitko10.grid(row=3,column=1)
    
tlacitko11=Button(Ramecek1,text="9",width=5, heigh=2)
tlacitko11.bind("<Button-1>", Klik9)
tlacitko11.grid(row=3,column=2)
    
tlacitko12=Button(Ramecek1,text="*",width=5, heigh=2)
tlacitko12.bind("<Button-1>", KlikKrat)
tlacitko12.grid(row=3,column=3)

tlacitko13=Button(Ramecek1,text="0",width=5, heigh=2)
tlacitko13.bind("<Button-1>", Klik0)
tlacitko13.grid(row=4,column=0)

tlacitko14=Button(Ramecek1,text=".",width=5, heigh=2)
tlacitko14.bind("<Button-1>", KlikTecka)
tlacitko14.grid(row=4,column=1)

tlacitko15=Button(Ramecek1,text="__",width=5, heigh=2)
tlacitko15.bind("<Button-1>", KlikMezera)
tlacitko15.grid(row=4,column=2)

tlacitko16=Button(Ramecek1,text="/",width=5, heigh=2)
tlacitko16.bind("<Button-1>", KlikDeleno)
tlacitko16.grid(row=4,column=3)

tlacitko17=Button(Ramecek1,text="DEL",width=5, heigh=2)
tlacitko17.bind("<Button-1>", KlikDEL)
tlacitko17.grid(row=5,column=0)

tlacitko18=Button(Ramecek1,text="CLR",width=5, heigh=2)
tlacitko18.bind("<Button-1>", KlikCLR)
tlacitko18.grid(row=5,column=1)

tlacitko19=Button(Ramecek1,text="moc",width=5, heigh=2)
tlacitko19.bind("<Button-1>", KlikMoc)
tlacitko19.grid(row=5,column=2)

tlacitko20=Button(Ramecek1,text="sqrt",width=5, heigh=2)
tlacitko20.bind("<Button-1>", KlikRoot)
tlacitko20.grid(row=5,column=3)

tlacitko21=Button(Ramecek1,text="ENTER",width=5, heigh=2, command=Vypocet)
tlacitko21.grid(row=6,columnspan=4, sticky=W+E)



Okno.mainloop()       


