# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:21:14 2013


"""

from Tkinter import *
from tkMessageBox import *
hlavni = Tk()

HorniMenu=Menu(hlavni)

def Soubor():
    showinfo("Soubor","Tato část není naprogramována!")
    
HorniMenu.add_command(label="Soubor",command=Soubor)
HorniMenu.add_command(label="Nastavení",command=Soubor)
HorniMenu.add_command(label="Nápověda",command=Soubor)
HorniMenu.add_command(label="Konec",command=hlavni.quit)

hlavni.config(menu=HorniMenu)

mainloop()