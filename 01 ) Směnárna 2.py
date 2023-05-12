# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:38:05 2014

@author: Ocelot
"""

from Tkinter import *

#########

a=27
b=20
c=33
d=6

def Vypocet():
    if Castka.get()=="":
        Napis7.configure(text=u"Zadejte částku!")
    else:
        
    
        if Promenna.get()=="Euro (EUR)":
            y=a
        elif Promenna.get()=="Dolar (USD)":
            y=b
        elif Promenna.get()=="Libra (GBP)":
            y=c
        else:
            y=d

        if Metoda.get()==1:
            Napis4.configure(text=u"Převedená částka:   "+ str(float(Castka.get())*int(y))+u" Kč")
            Napis5.configure(text=u"Poplatek 0,5%:   "+ str((float(Castka.get())*int(y))*0.005)+u" Kč")
            Napis6.configure(text=u"Částka s poplatkem:   "+ str((float(Castka.get())*int(y) -  (float(Castka.get())*int(y))*0.005 ))+u" Kč")
            Napis7.configure(text=u"Vyplatit částku:   "+ str((float(Castka.get())*int(y) -  (float(Castka.get())*int(y))*0.005 ))+u" Kč")
        elif Metoda.get()==2: 
            Napis4.configure(text=u"Převedená částka:   "+ str(float(Castka.get())*int(y))+u" Kč")
            Napis5.configure(text=u"Poplatek 0,5%:   "+ str((float(Castka.get())*int(y))*0.005)+u" Kč")
            Napis6.configure(text=u"Částka s poplatkem:   "+ str((float(Castka.get())*int(y) +  (float(Castka.get())*int(y))*0.005 ))+u" Kč")
            Napis7.configure(text=u"Vybrat částku:   "+ str((float(Castka.get())*int(y) +  (float(Castka.get())*int(y))*0.005 ))+u" Kč")
        else:
            Napis7.configure(text=u"Vyberte metodu!")
    




#######

Okno = Tk()
Okno.title("Směnárna")

Ramecek0 = Frame(Okno)
Ramecek0.pack(pady=1,padx=1)

Napis0 = Label(Ramecek0,text="SMĚNÁRNA", font=("Arial",20))
Napis0.pack(side="top", padx=20,pady=3)

### KURZOVNÍ LÍSTEK

Ramecek1 = LabelFrame(Okno,text=u"Kurzovní lístek:")
Ramecek1.pack(pady=1,padx=1) 

Napis1 = Label(Ramecek1,text="1 EUR = 27 CZK")
Napis1.pack(side="top", padx=20,pady=1)

Napis2 = Label(Ramecek1,text="1 USD = 20 CZK")
Napis2.pack(side="top", padx=20,pady=1)

Napis3 = Label(Ramecek1,text="1 GBP = 33 CZK")
Napis3.pack(side="top", padx=20,pady=1)

Napis4 = Label(Ramecek1,text="1 PLN = 6 CZK")
Napis4.pack(side="top", padx=20,pady=1)

### PRODEJ / NÁKUP

Ramecek2 = Frame(Okno)
Ramecek2.pack(pady=1,padx=1)

Metoda = IntVar() 

Napis1 = Label(Ramecek2,text="Vyberte metodu: ")
Napis1.pack(side="top", padx=20,pady=3)

Nakup=Radiobutton(Ramecek2,text=u"NÁKUP", value=1, variable=Metoda)
Nakup.pack(side=LEFT)

Prodej=Radiobutton(Ramecek2,text=u"PRODEJ", value=2, variable=Metoda)
Prodej.pack(side=LEFT)

### MĚNA

Ramecek3 = Frame(Okno)
Ramecek3.pack(pady=1,padx=1)

Napis2 = Label(Ramecek3,text=u"Vyberte měnu: ")
Napis2.pack(side="left", padx=10,pady=3)

Parametry = ["Euro (EUR)","Dolar (USD)","Libra (GBP)",u"Zlotý (PLN)"]

Promenna = StringVar(Ramecek3)
Promenna.set(Parametry[0]) 

Meny = OptionMenu(Ramecek3, Promenna, *Parametry)
Meny.pack(padx=10,pady=3)

### ČÁSTKA

CastkaVar=StringVar()
CastkaVar.set("")

Ramecek4 = Frame(Okno)
Ramecek4.pack(pady=1,padx=1)

Napis3 = Label(Ramecek4,text=u"Zadejte částku: ")
Napis3.pack(side="left", padx=10,pady=5)

Castka = Entry(Ramecek4, textvariable=CastkaVar)
Castka.pack(side="right", padx=10, pady=5)

Tlacitko0 = Button(Okno, text=u"Spočítat", command=Vypocet)
Tlacitko0.pack(padx=10,pady=5)

### VÝPIS PLATBY


Napis4 = Label(Okno, text=u"Převedená částka: ")
Napis4.pack()

Napis5 = Label(Okno, text=u"Poplatek 0,5%: ")
Napis5.pack()

Napis6 = Label(Okno, text=u"Částka s poplatkem: ")
Napis6.pack()

Napis7 = Label(Okno, text=" ", font=("Arial",15))
Napis7.pack()

TlacitkoX = Button(Okno, text=u"Ukončení")
TlacitkoX.pack(padx=10,pady=5)


mainloop()