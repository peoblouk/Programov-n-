# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 09:14:19 2013


"""

from Tkinter import *
    
def nula():
       Napis["text"]="0"
       
def plus():
       Napis["text"]=str(int(Napis["text"])+1)
      
def minus():
       Napis["text"]=str(int(Napis["text"])-1)
    
    
Okno = Tk()                                                      

Napis = Label(Okno, text="0", heigh=2, )
Napis.pack()

Tlacitko1 = Button(Okno, text="+", width=10, heigh=2, command=plus)      
Tlacitko1.pack()                                                 

Tlacitko2 = Button(Okno, text="-", width=10, heigh=2, command=minus)
Tlacitko2.pack()

Tlacitko3 = Button(Okno, text=u"RESET", width=10, heigh=2, command=nula)
Tlacitko3.pack()

Tlacitko4 = Button(Okno, text=u"END", width=10, heigh=2, command=Okno.quit)
Tlacitko4.pack()

Okno.mainloop() 