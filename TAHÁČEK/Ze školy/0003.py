# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:10:54 2014


"""

from Tkinter import *

hlavni= Tk()
hlavni.title("Zeměměpis")

ramecek=Frame(hlavni)
ramecek.pack(pady=1,padx=1)

ramecek1=LabelFrame(hlavni,text=u"1) Vyber hlavní město Francie")
ramecek1.pack(pady=1,padx=1)

ramecek2=Frame(hlavni)
ramecek2.pack(pady=1,padx=1)

ramecek3=Frame(hlavni, bd=2, width=500,  height=50, relief=GROOVE)
ramecek3.pack(pady=1,padx=1)

ramecek4=LabelFrame(hlavni,text=u"4) Vyber Asijská města")
ramecek4.pack(pady=1,padx=1)

ramecek5=Frame(hlavni)
ramecek5.pack(pady=1,padx=1)

#+++++++++++++++++++++++++++++++++++++++++++++++++

napis= Label(ramecek,text=u"Test na města",font=("Arial",30))
napis.pack(side="top", padx=20,pady=10)

napis= Label(ramecek2,text=u"2) Vídeň je hlavní město:")
napis.pack(side=LEFT, padx=20,pady=10)

napis= Label(ramecek3,text=u"3) Hlavní město Kanady je:")
napis.pack(side=LEFT, padx=10, pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++
v = IntVar() 

okno0=Radiobutton(ramecek1,text=u"Londýn", value=1, variable=v)
okno0.pack(side=LEFT)
okno1=Radiobutton(ramecek1,text=u"Praha", value=2, variable=v)
okno1.pack(side=LEFT)
okno2=Radiobutton(ramecek1,text=u"Paříž", value=3, variable=v)
okno2.pack(side=LEFT)
okno3=Radiobutton(ramecek1,text=u"Brusel", value=4, variable=v)
okno3.pack(side=LEFT)

#+++++++++++++++++++++++++++++++++++++++++++++++++
Tl0=Checkbutton(ramecek4,text=u"Ulánbátar")
Tl0.grid(row=0, column=0,sticky=W)
Tl01=Checkbutton(ramecek4,text=u"Sydney")
Tl01.grid(row=0, column=1,sticky=W)
Tl02=Checkbutton(ramecek4,text=u"Tokio")
Tl02.grid(row=1, column=0,sticky=W)
Tl03=Checkbutton(ramecek4,text=u"New York")
Tl03.grid(row=1, column=1,sticky=W)
#+++++++++++++++++++++++++++++++++++++++++++++++++
PARAMETRY = [u"Rakouska",u"Uzbekistánu",u"České republiky",u"Polska"]

promenna = StringVar(ramecek2)
promenna.set(PARAMETRY[0]) 

w = OptionMenu(ramecek2, promenna, *PARAMETRY)
w.pack(padx=20,pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++

vstup1= Entry(ramecek3)
vstup1.pack(side="right", padx=10, pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++

def vyhodnotit(hodnota):
    if hodnota=="Vencouver":
        print "super"
    elif hodnota=="vencouver":
        print "super"
    else:
        print u"špatně"




tlacitko2= Button (ramecek5, text=u"Vyhodnotit",command=vyhodnotit)
tlacitko2.pack(padx=10,pady=10, side=LEFT)

tlacitko1= Button (ramecek5, text=u"Ukončení", command=hlavni.quit)
tlacitko1.pack(padx=10,pady=10)

hlavni.mainloop()