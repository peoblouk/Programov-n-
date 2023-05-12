# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 08:19:00 2014

@author: spu30141
"""

from Tkinter import *
from datetime import *
from tkMessageBox import *




Okno = Tk()
Okno.title("Kalendář")


Dnes = datetime.now()
Datum="%02d.%02d."  % (Dnes.day, Dnes.month)

Dat = "Dnes je %d. %d. %d" % (Dnes.day, Dnes.month, Dnes.year)

### SVÁTKY ###

Slovnik_Jmena = {}

try:
    Jmena = open("jmena.txt","r")
    Radek = Jmena.readline()
    while Radek <> "":
        Slovnik_Jmena[Radek[:6]]=Radek[12:-2]
        Radek = Jmena.readline()
    Svatek = u"Svátek dnes slaví " + str(Slovnik_Jmena[Datum])

except:
    showerror("Chyba!", "Chyba při otevírání souboru")
else:
    Jmena.close()

### NAROZENINY ###

Slovnik_Narozeniny = {}

try:
    Narozeniny = open("narozky.txt","r")
    Radek = Narozeniny.readline()
    while Radek <> "":
         Slovnik_Narozeniny[Radek[:6]]=Radek[11:-1]
         Radek = Narozeniny.readline()
    Narozky = u"Narozky dnes slaví " + str(Slovnik_Narozeniny[Datum])
except:
    Narozky = u"Narozky dnes nikdo neslaví "
else:
    Narozeniny.close()
    


### FUNKCE ###

def VlozitNarozky():
    Nar = open("narozky.txt","r+")
    Name = VstupName.get()
    Cti =  int(VstupDen.get()), int(VstupMes.get()), int(VstupRok.get())
    Radky = Nar.readlines()
    Pocet = len(Radky)
    Nar.seek(0,0)
    Seznam = []
    for i in range (Pocet):
        Radek = Nar.readline()
        Radek = Radek[:-1]
        Seznam.append(Radek)
    X = ("%02d.%02d.%04d %s"  % (Cti[0], Cti[1], Cti[2], Name))
    
    if X in str(Seznam):
        showinfo("Chyba!", u"Osoba je již na seznamu!")
    else:
        Nar.seek(0,2)
        Nar.write("%02d.%02d.%04d %s\n"  % (Cti[0], Cti[1], Cti[2], Name))
        Okno2.destroy()

def VlozitOkno():
    global Okno2
    global VstupDen
    global VstupMes
    global VstupRok
    global VstupName
    
    
    Okno2=Toplevel()
    Okno2.title("Vložení narozenin")
    
    NapisX = Label(Okno2, text= u"Vložení narozenin", font=("Arial",15))
    NapisX.grid(columnspan=2)
    
    NapisDen = Label(Okno2, text="Zadejte den:")
    NapisDen.grid(column=0, row=1, sticky=E)
    VstupDen = Entry(Okno2)
    VstupDen.grid(column=1, row=1, sticky=W, padx=5, pady=3)
    
    NapisMes = Label(Okno2, text=u"Zadejte měsíc:")
    NapisMes.grid(column=0, row=2, sticky=E)
    VstupMes = Entry(Okno2)
    VstupMes.grid(column=1, row=2, sticky=W, padx=5, pady=3)    

    NapisRok = Label(Okno2, text="Zadejte rok:")
    NapisRok.grid(column=0, row=3, sticky=E)
    VstupRok = Entry(Okno2)
    VstupRok.grid(column=1, row=3, sticky=W, padx=5, pady=3)

    NapisName = Label(Okno2, text=u"Zadejte jméno:")
    NapisName.grid(column=0, row=4, sticky=E)
    VstupName = Entry(Okno2)
    VstupName.grid(column=1, row=4, sticky=W, padx=5, pady=3)

    TlOK = Button(Okno2, text="OK", command=VlozitNarozky)
    TlOK.grid(columnspan=2)
    TlCancel = Button(Okno2, text=u"ZRUŠIT", command=Okno2.destroy)
    TlCancel.grid(columnspan=2)
    

Ramecek1=Frame(Okno)
Ramecek1.grid()

Napis0 = Label(Ramecek1, text="KALENDÁŘ", font=("Arial",15))
Napis0.grid(columnspan=2)

NapisDatum = Label(Ramecek1, text=Dat, font=("Arial",10))
NapisDatum.grid(columnspan=2)

NapisSvatek = Label(Ramecek1, text=Svatek)
NapisSvatek.grid(columnspan=2)

NapisNarozky = Label(Ramecek1, text=Narozky)
NapisNarozky.grid(columnspan=2)


TlVlozit = Button (Ramecek1, text=u"VLOŽIT NAROZENINY", command=VlozitOkno)
TlVlozit.grid(columnspan=2, row=6)

TlKonec = Button (Ramecek1, text="KONEC", command=Okno.destroy)
TlKonec.grid(columnspan=2, row=7)


Okno.mainloop()