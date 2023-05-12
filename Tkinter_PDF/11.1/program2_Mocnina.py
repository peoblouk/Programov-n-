from tkinter import *

def Mocnina():
    x=int(vstup.get())       #float(vstup.get())
    vystup["text"]=str(x**2)
    vstup.select_range(0,END)

hlavni=Tk()
hlavni.title("Mocniny")

ram=Frame(hlavni,bd=2,width=100,height=50,relief="ridge",padx=10,pady=10)
ram.pack(padx=5,pady=5)

vstup=Entry(ram)
vstup.focus_set()
vstup.pack(side="left",padx=5,pady=5)

vystup=Label(ram,text="Výsledek",width=10)
vystup.pack(side="left",padx=5,pady=5)

vyp=Button(hlavni,text="Mocnina",width=15,command=Mocnina)
vyp.pack(padx=5,pady=5)


hlavni.mainloop()
            
    
    
    
      
      





















