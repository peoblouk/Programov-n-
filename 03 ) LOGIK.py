# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 15:31:36 2014

@author: Ocelot
"""

from Tkinter import *
from tkMessageBox import *
from random import *

### PROGRAM ###


Okno=Tk()   
Okno.title("Hra LOGIK")

Ramecek0 = Frame(Okno)
Ramecek0.grid(pady=10,padx=10)


Napis0 = Label(Ramecek0,text="HRA LOGIK", font=("Arial",25))
Napis0.grid(row=0, columnspan=6, pady=5, padx=5)


sez0=[]
sez1=[]

for y in range(1,6):
        E0=Entry(Ramecek0, width=8)
        sez0.append(E0)
        E0.grid(row=2, column=y, padx=1, pady=20)

for x in range(3,13):
    for y in range(1,6):
        E1=Entry(Ramecek0, width=8, justify="center")
        sez1.append(E1)
        E1.grid(row=x, column=y, padx=1, pady=1)

sezX=[]
for i in range(5):
    x=randint(0,9)
    sezX.append(x)


c=45
def Hadej():
    global c
    if c<>-5:
        sez1[c].insert(0, Spin1.get())
        sez1[c+1].insert(0, Spin2.get())
        sez1[c+2].insert(0, Spin3.get())
        sez1[c+3].insert(0, Spin4.get())
        sez1[c+4].insert(0, Spin5.get())
        c-=5
    
        if Spin1.get()==str(sezX[0]):
           sez0[0].configure(bg="green") 
        elif Spin1.get() in str(sezX):
            sez0[0].configure(bg="yellow")
        else:
            sez0[0].configure(bg="red")
         ###################        
        if Spin2.get()==str(sezX[1]):
            sez0[1].configure(bg="green")  
        elif Spin2.get() in str(sezX):
            sez0[1].configure(bg="yellow") 
        else:
            sez0[1].configure(bg="red")
          ##################          
        if Spin3.get()==str(sezX[2]):
            sez0[2].configure(bg="green")    
        elif Spin3.get() in str(sezX):
            sez0[2].configure(bg="yellow") 
        else:
            sez0[2].configure(bg="red")
          ####################            
        if Spin4.get()==str(sezX[3]):
            sez0[3].configure(bg="green") 
        elif Spin4.get() in str(sezX):
            sez0[3].configure(bg="yellow")
        else:
            sez0[3].configure(bg="red")
          ##################         
        if Spin5.get()==str(sezX[4]):
            sez0[4].configure(bg="green") 
        elif Spin5.get() in str(sezX):
            sez0[4].configure(bg="yellow") 
        else:
            sez0[4].configure(bg="red")
            
        if Spin1.get()==str(sezX[0]) and Spin2.get()==str(sezX[1]) and Spin3.get()==str(sezX[2]) and Spin4.get()==str(sezX[3]) and Spin5.get()==str(sezX[4]):          
            showinfo(u"Juchůůů",u"Vyhrál jsi !!!")
            Konec()
    else:
        showinfo(u"Cháá cháá",u"Prohrál jsi !!!")
        Konec()
        
def Konec():
    n=askyesno(u"KONEC", u"Chceš spustit novou hru?")
    if n==True:
        Nova()
    else:
        Okno.destroy()

def Nova():
    global c
    c=45
    global sezX
    sezX=[]
    for i in range(5):
        x=randint(0,9)
        sezX.append(x)
    for i in range (5):
        sez0[i].configure(bg="white") 
    for i in range (50):
        sez1[i].delete(0,END)

                ######### SPIN BOX #########

S1=StringVar()
S2=StringVar()
S3=StringVar()
S4=StringVar()
S5=StringVar()

Spin1 = Spinbox(Ramecek0, from_=0, to=9, textvariable=S1, width=5)
Spin1.grid(row=13, column=1, pady=5)

Spin2 = Spinbox(Ramecek0, from_=0, to=9, textvariable=S2, width=5)
Spin2.grid(row=13, column=2, pady=5)

Spin3 = Spinbox(Ramecek0, from_=0, to=9, textvariable=S3, width=5)
Spin3.grid(row=13, column=3, pady=5)

Spin4 = Spinbox(Ramecek0, from_=0, to=9, textvariable=S4, width=5)
Spin4.grid(row=13, column=4, pady=5)

Spin5 = Spinbox(Ramecek0, from_=0, to=9, textvariable=S5, width=5)
Spin5.grid(row=13, column=5, pady=5)

                 ###### NÁPOVĚDA #######

Ramecek1 = Frame(Okno)
Ramecek1.grid(pady=10, padx=10)

Napis1 = Label(Ramecek1,text=u"Špatné číslo")
Napis1.grid(row=1, column=0, padx=5)

Napis2 = Label(Ramecek1,text=u"Špatná pozice")
Napis2.grid(row=1, column=1, padx=5)

Napis3 = Label(Ramecek1,text=u"Správně")
Napis3.grid(row=1, column=2, padx=5)

                       #######

Nap1=Entry(Ramecek1, width=8, bg="RED")
Nap1.grid(row=0, column=0, padx=15)

Nap2=Entry(Ramecek1, width=8, bg="YELLOW")
Nap2.grid(row=0, column=1, padx=15)

Nap3=Entry(Ramecek1, width=8, bg="GREEN")
Nap3.grid(row=0, column=2, padx=15)


                ###### TALČÍTKA ########

Ramecek2 = Frame(Okno)
Ramecek2.grid(pady=5,padx=10)

Tlacitko0 = Button(Ramecek2, text=u"HÁDEJ", command=Hadej)
Tlacitko0.grid(padx=10, pady=5, column=0, row=1)

Tlacitko1 = Button(Ramecek2, text=u"NOVÁ HRA", command=Nova)
Tlacitko1.grid(padx=10, pady=5, column=1, row=1)

Tlacitko2 = Button(Ramecek2, text=u"KONEC", command=Okno.destroy)
Tlacitko2.grid(padx=10, pady=5, column=2, row=1)


Okno.mainloop()