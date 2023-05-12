# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:06:14 2014

@author: Ocelot
"""

from Tkinter import *
from tkMessageBox import *
import random



### ZÁKLADNÍ ###



def Otevrit():
    global Soubor
    Nazev=askopenfilename(title='Vyberte soubor',filetypes=[(u"Textový soubor","*.txt")])
    Soubor = open(Nazev,"r+")
    Obsah = Soubor.readlines()
    Text.delete(1.0,END)
    for radek in Obsah:
        Text.insert(INSERT,radek)
    MenuSoubor.entryconfig(2,state="normal")
    MenuSoubor.entryconfig(5,state="normal")


def UlozitJako():
    global Soubor
    Nazev=asksaveasfilename(title=u"Uložit jako",filetypes=[(u"Textový soubor","*.txt")])
    Soubor = open(Nazev,"w")    
    Ulozit()
    MenuSoubor.entryconfig(2,state="normal")
    MenuSoubor.entryconfig(5,state="normal")

 
def Ulozit(): 
    global Soubor
    Soubor.seek(0)
    Soubor.truncate()
    for znak in Text.get(1.0,END):
        Soubor.write(znak)
    Soubor.truncate()


def Novy():
    UlozitJako()
    Text.delete(1.0,END)
    MenuSoubor.entryconfig(2,state="normal")
    MenuSoubor.entryconfig(5,state="normal")


def Zavrit():
    Ulozit()    
    Text.delete(1.0,END)
    MenuSoubor.entryconfig(2,state="disabled")
    MenuSoubor.entryconfig(5,state="disabled")
    



### ÚPRAVA ###       


def Znaky():    
    Puvodni=askstring(u"Původní znak",u"Znak, který bude nahrazen:")   
    if Puvodni=="":
        showinfo("Chyba!!!","Zadejte znak!" )
    else:
        Novy=askstring(u"Nový znak",u"Nový znak:")
        Obsah = Text.get(1.0,END)
        Text.delete(1.0,END)    
        for znak in Obsah:
            if znak == Puvodni:
                Text.insert(END,Novy)
            else:
                Text.insert(END,znak)
 
def MalaPismena():
    Mala=Text.get(1.0,END).lower()
    Text.delete(1.0,END)
    Text.insert(1.0,Mala) 
 
################################################################## 

def Statistika():

    Pocetx = {}
    Obsah = Text.get(1.0,END)
    Znaky = []
    for znak in Obsah:
        if znak in Znaky:
            Pocetx[znak]+=1

        else:
            Znaky.append(znak)
            Pocetx[znak]=1

    print Pocetx

        
################################################################

def NahodnyText():
    Slova=askinteger(u"Počet slov",u"Počet slov:")   
    SlovVeta=askinteger(u"Slova ve větě",u"Zadehte maximum slov ve větě:")   
    DelkaSlova=askinteger(u"Délka slova",u'Zadejte maximální délku slova:')   
    
    if Slova>500 or DelkaSlova>10 or Slova<1 or DelkaSlova<1:
        showinfo("Chyba!","Počet slov 1-500  /  Délka slova 1-10." )
    else:
        aktualniSlova=0
        Text.delete(1.0,END)
        while aktualniSlova<Slova:
            if (Slova-aktualniSlova<SlovVeta):
                SlovVeta=Slova-aktualniSlova
            aktualniSlova+=NahodnaVeta(DelkaSlova,SlovVeta)
        UlozitJako()
        Zavrit()
        Text.delete(1.0,END)  

def NahodnaVeta(DelkaSlova,SlovVeta):
    Slova=0    
    Veta=""
    Slovo1=NahodneSlovo(DelkaSlova)
    Slova+=1
    Veta+=chr(ord( Slovo1[0])+ord("A")-ord("a"))+ Slovo1[1:]
    for i in range(random.randint(1,SlovVeta)):
        Veta+=" "+vygeneruj_slovo(DelkaSlova)
        Slova+=1
    Veta+=". "
    Text.insert(END,Veta)
    return Slova
 

def NahodneSlovo(DelkaSlova):
    Slovo=""
    Samohlasky=[97,101,105,111,117,121]
    if random.randint(0,1)==1:
        samohlaska=False
    else:
        samohlaska=True
    while len(Slovo)<random.randint(1,DelkaSlova):
        Pismeno=random.randint(ord('a'),ord('z'))
        if samohlaska==True and Samohlasky.count(Pismeno)==0:
            samohlaska=False
            Slovo+=chr(Pismeno)   
        elif samohlaska==False: 
            samohlaska=True
            Slovo+=chr(Samohlasky[random.randint(0,5)])
    return Slovo


### OKNO ###  

  
Okno = Tk()
Okno.title("Soubory")

MenuHlavni = Menu(Okno)

MenuSoubor = Menu(MenuHlavni, tearoff=0)
MenuSoubor.add_command(label="Nový", command=Novy)
MenuSoubor.add_command(label="Otevřít", command=Otevrit)
MenuSoubor.add_command(label="Uložit", state="disabled", command=Ulozit)
MenuSoubor.add_command(label="Uložit jako", command=UlozitJako)
MenuSoubor.add_separator()
MenuSoubor.add_command(label="Zavřít", state="disabled", command=Zavrit)

MenuHlavni.add_cascade(label="Soubor", menu=MenuSoubor)

MenuUpravy = Menu(MenuHlavni, tearoff=0)
MenuUpravy.add_command(label="Nahrazení znaku",command=Znaky)
MenuUpravy.add_command(label="Převod na malá písmena", command=MalaPismena)
MenuUpravy.add_command(label="Náhodný text", command=NahodnyText)
MenuUpravy.add_command(label="Statistika", command=Statistika)


MenuHlavni.add_cascade(label="Operace", menu=MenuUpravy)
MenuHlavni.add_command(label="Konec", command=Okno.destroy)
Okno.config(menu=MenuHlavni)

Text=Text(Okno, width=25, heigh=10, font=("Arial",13))
Text.pack()

Okno.mainloop()