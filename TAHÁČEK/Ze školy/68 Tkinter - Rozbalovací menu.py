# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:35:54 2013


"""


from Tkinter import *
from tkMessageBox import *
hlavni = Tk()

#vytvoření hlavního menu
HorniMenu=Menu(hlavni)

def Soubor():
    showinfo("Soubor","Tato část není naprogramována!")
  
#vytvoření jedné rozbalovací nabídky a připojení do hl. menu 
MenuSoubor=Menu(HorniMenu, tearoff=0)
MenuSoubor.add_command(label="Otevřít",command=Soubor)
MenuSoubor.add_command(label="Uložit",command=Soubor)
MenuSoubor.add_separator()
MenuSoubor.add_command(label="Konec",command=hlavni.quit)
HorniMenu.add_cascade(label="Soubor", menu=MenuSoubor)

#zobrazení hlavního menu
hlavni.config(menu=HorniMenu)

mainloop()

"""
Úkol:
1) Vytvořte program s menu pro práci se souborem:

   Soubor
    - Vygenerovat nuly a jedničky
    - Vygenerovat samohlásky
    - Konec
    
   Nápověda
    - O aplikaci
    
   Nuly a jedničky - soubor bude obsahovat 100 
                     náhodných čísel 
   Samohlásky - soubor bude obsahovat 100 náhodných
                samohlásek
"""    
    