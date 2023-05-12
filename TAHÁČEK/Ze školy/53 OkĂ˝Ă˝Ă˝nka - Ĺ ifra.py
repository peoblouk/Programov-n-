# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:56:52 2013


"""

"""

ÚKOL:
    
- Napište aplikaci, která bude obsahovat:
    - Label (nápis) "Tajná šifra"
    - Entry (vstup)
    - Button (tlačítko) "Šifruj vstup"
    - Label (nápis) - výstup
    - Button (tlačátko) "Konec"
    
    Po stistku tlačítka se řetězec ze vstupu zašifruju libovolnou 
    metodou a výsledek se zobrazí v Labelu (výstup). 

"""


from Tkinter import *


def Sifra():
    x=(Vstup.get())
    Vystup["text"]=Sez
"""
def Sez():
    for i in x:
        sez.append(i)
        sez.sort()
   ret=""
   for i in sez:
       ret+=i
"""
Okno=Tk()
Okno.title("Šifra")

Napis1 = Label(Okno, text=u"TAJNÁ ŠIFRA") 
Napis1.pack(padx=10, pady=5)

Vstup = Entry(Okno)
Vstup.pack(padx=10, pady=5)

Tlacitko0 = Button(Okno, text=u"Šifruj vstup", command=Sifra)
Tlacitko0.pack(padx=10, pady=5)

Ramecek = Frame(Okno, bd=2, width=100, heigh=50, relief="sunken")
Ramecek.pack()

Vystup = Label(Ramecek, text="") 
Vystup.pack(padx=10, pady=5)


Tlacitko1 = Button(Okno, text="Vypnout", command=Okno.quit)
Tlacitko1.pack(padx=10, pady=5)

Okno.mainloop()

                                                     


   