from tkinter import *

def Smazat():
    vstup.delete(0,END)      #smaže vše
    #vstup.delete(0)           #smaže jeden znak
    #vstup.delete(INSERT,END)   #smaže znaky od místa kurzoru do konce

def Vlozit():
    vstup.insert(0,"zobrazený text")  #vkládá text na pozici (začátek)
    #vstup.insert(END,"text")  - na konec
    #vstup.insert(INSERT,"text") - na místo kurzoru

def Oznacit():
    vstup.select_range(0,END)   #označí celý text

def Zobrazit():
    vystup["text"]=vstup.get() #vrací obsah Entry(text. řetězec)

hlavni=Tk()
hlavni.title("Text")

vstup=Entry(hlavni,width=20,font="Arial 12",bd=5)
vstup.focus_set()    #kurzor bude v Entry
vstup.pack(padx=5,pady=5)

vystup=Label(hlavni,text="Výstup",font="Arial 15")
vystup.pack(padx=5,pady=5)

akce=LabelFrame(hlavni,text="Výběr akce",relief="ridge",bd=3,padx=10,pady=10)
akce.pack(padx=5,pady=5)

tl1=Button(akce,text="Smaž",width=10,command=Smazat)
tl1.pack(padx=5,pady=5)
tl2=Button(akce,text="Vlož",width=10,command=Vlozit)
tl2.pack(padx=5,pady=5)
tl3=Button(akce,text="Označ",width=10,command=Oznacit)
tl3.pack(padx=5,pady=5)
tl4=Button(akce,text="Zobraz",width=10,command=Zobrazit)
tl4.pack(padx=5,pady=5)


hlavni.mainloop()
            
    
    
    
      
      





















