# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 11:14:56 2012


"""

from Tkinter import *
from tkMessageBox import *

"""
showinfo - zobrazení hlášky + tlačítko Ok
askyesno - zobrazení otázky + tlačítka Yes a No, vrací True nebo False
"""
"""


hl_okno=Tk()

showinfo("Informace",u"Prosím, přečtěte si následující informaci.")

x=askyesno(u"Otázka", u"Chcete pokračovat?")
print x

mainloop()

"""
"""
Úkol: 
1) Položte uživateli libovolnou zjišťovací otázku.
   Když správně odpoví vypište na konzolu pochvalu,
   jinak vypište správnou odpověď.
"""

x=askyesno(u"Otázka", u"A prdí taky hadi?")
if x==True:
    print u"Jasněěě, seš borec!"
else:
    print u"Tak to vůůůbec!"
