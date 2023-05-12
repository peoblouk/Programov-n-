# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 08:46:16 2014




Úkol:
   
1) Rozmístěte tlačítka a ostatní komponenty jako na kalkulačce.
    
    
"""

from Tkinter import *

hl_okno=Tk()          # toto vytvoří hlavní okno

text=Text()
text.config(heigh=3,width=5)
text.grid(row=0,columnspan=4,sticky=W+E) 
   
tlacitko1=Button(hl_okno,text="Num",width=6, heigh=3)
tlacitko1.grid(row=1,column=0,sticky=W+E)

tlacitko2=Button(hl_okno,text="/",width=6, heigh=3)
tlacitko2.grid(row=1,column=1,sticky=W+E)
    
tlacitko3=Button(hl_okno,text="*",width=6, heigh=3)
tlacitko3.grid(row=1,column=2,sticky=W+E)

tlacitko4=Button(hl_okno,text="-",width=6, heigh=3)
tlacitko4.grid(row=1,column=3,sticky=W+E)

tlacitko5=Button(hl_okno,text="+",width=6, heigh=6)
tlacitko5.grid(rowspan=2,column=3,sticky=N+S+W+E)

tlacitko6=Button(hl_okno,text="7",width=6, heigh=3)
tlacitko6.grid(row=2,column=0,sticky=W+E)

tlacitko7=Button(hl_okno,text="8",width=6, heigh=3)
tlacitko7.grid(row=2,column=1,sticky=W+E)
    
tlacitko8=Button(hl_okno,text="9",width=6, heigh=3)
tlacitko8.grid(row=2,column=2,sticky=W+E)

tlacitko9=Button(hl_okno,text="4",width=6, heigh=3)
tlacitko9.grid(row=3,column=0,sticky=W+E)

tlacitko10=Button(hl_okno,text="5",width=6, heigh=3)
tlacitko10.grid(row=3,column=1,sticky=W+E)
    
tlacitko11=Button(hl_okno,text="6",width=6, heigh=3)
tlacitko11.grid(row=3,column=2,sticky=W+E)
    
tlacitko12=Button(hl_okno,text="ENT",width=6, heigh=6)
tlacitko12.grid(rowspan=3,column=3,sticky=N+S+W+E)

tlacitko13=Button(hl_okno,text="1",width=6, heigh=3)
tlacitko13.grid(row=4,column=0,sticky=W+E)

tlacitko14=Button(hl_okno,text="2",width=6, heigh=3)
tlacitko14.grid(row=4,column=1,sticky=W+E)

tlacitko15=Button(hl_okno,text="3",width=6, heigh=3)
tlacitko15.grid(row=4,column=2,sticky=W+E)

tlacitko16=Button(hl_okno,text="0", width=16, heigh=3)
tlacitko16.grid(row=5,columnspan=2, sticky=N+S+W+E)

tlacitko17=Button(hl_okno,text=".",width=6, heigh=3)
tlacitko17.grid(row=5,column=2,sticky=W+E)


hl_okno.mainloop()       