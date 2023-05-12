# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 11:31:49 2013


"""

from Tkinter import *

hlavni=Tk()
text=Text()
text.pack()

text.tag_config("modre", font="20", foreground="blue", underline=1)
text.insert(END, "ahoj,","modre")
text.insert(END, " svete")


smazat=Button(hlavni,text="Smazat vše", command=lambda: text.delete(1.0, END))
smazat.pack()

retezec=text.get(1.0,END)
print retezec

mainloop() 

"""
Úkol:
1) Vytvořte jednoduchý textový editor, který umožní
   uložit nebo načíst obsah komponenty text.
   Použijte souborové dialogy.
"""    