# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:01:49 2013


"""

from Tkinter import *

hlavni=Tk()

def ZobrazOkno1():
    okno1=Toplevel()
    okno1.title(u"První okno")
        
    tlZavriOkno1=Button(okno1,text=u"Zavři toto okno",command=okno1.destroy)
    tlZavriOkno1.pack()
    
def ZobrazOkno2():
    okno2=Toplevel()
    okno2.title(u"Druhé okno")

    tlZavriOkno2=Button(okno2,text=u"Zavři toto okno",command=okno2.destroy)
    tlZavriOkno2.pack()   
    tlZavriAplikaci=Button(okno2,text=u"Zavři celou aplikaci",command=hlavni.quit)
    tlZavriAplikaci.pack() 
    
tlac1 = Button(hlavni, text="Zobraz prvni podokno",command=ZobrazOkno1)
tlac1.pack()
tlac2 = Button(hlavni, text="Zobraz druhe podokno",command=ZobrazOkno2)
tlac2.pack()

mainloop()