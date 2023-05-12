# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 10:00:12 2013


"""

from Tkinter import *

hlavni = Tk()

def LevyKlik(udalost):
    print u"Klikl jsi na frame na pozici:", udalost.x, udalost.y 

def Najeti(udalost):
    print "Najel jsi na frame"

def Klavesa(udalost):
    print "Stiskl jsi ", udalost.char
    
vstup = Entry(hlavni)
vstup.bind("<Key>", Klavesa)
vstup.pack()
  
ramec = Frame(hlavni, width=100, height=100,bg="white")
ramec.bind("<Button-1>", LevyKlik)
ramec.bind("<Enter>", Najeti)
ramec.pack()



hlavni.mainloop()

"""
1) Vložte do hl. okna frame, který bude reagovat na
   pravé tlačítko myši a vždy si nastaví náhodnou
   barvu pozadí.
2) Při stisku levého tlačítka se nastaví bílé pozadí.
3) Vytvořte program s jedním tlačítkem, které se po
   najetí myši přesune na náhodné místo v okně.
"""   