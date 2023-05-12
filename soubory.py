from Tkinter import *
from tkMessageBox import *
from tkSimpleDialog import *
from tkFileDialog import *
import pylab as plt
import random


soubor=None


#########################################################################################################
###################### OPERACE SE SOUBOREM ##############################################################
#########################################################################################################  

def novySoubor():
    ulozitJako()
    text.delete(1.0,END)
    menuSoubor.entryconfig(1,state="normal")
    menuSoubor.entryconfig(2,state="normal")
    menuSoubor.entryconfig(5,state="normal")

def otevritSoubor():
    global soubor
    try:
        jmenoSouboru=askopenfilename(title='Vyber soubor',filetypes=[('Text','.txt')])
        soubor2 = open(jmenoSouboru,"r+")
    except:
        return False
    soubor=soubor2    
    menuSoubor.entryconfig(1,state="normal")
    menuSoubor.entryconfig(2,state="normal")  
    menuSoubor.entryconfig(5,state="normal")
    dataSouboru = soubor.readlines()
    text.delete(1.0,END)
    for radek in dataSouboru:
        text.insert(END,radek)

def zavritSoubor():
    ulozit()    
    menuSoubor.entryconfig(1,state="disabled")
    menuSoubor.entryconfig(2,state="disabled")  
    menuSoubor.entryconfig(5,state="disabled")
    text.delete(1.0,END)
    

def ulozit():  
    try:
        global soubor
        soubor.seek(0)
        soubor.truncate()
        for znak in text.get(1.0,END):
              soubor.write(znak)
        soubor.truncate()
    except:
        None

        
def ulozitJako():
    global soubor
    jmenoSouboru=asksaveasfilename(title=u'Nový soubor',filetypes=[('Text','.txt')])
    try:    
        soubor = open(jmenoSouboru,"w")    
        ulozit()
        menuSoubor.entryconfig(1,state="normal")
        menuSoubor.entryconfig(5,state="normal")
    except:
        None
 

#########################################################################################################
###################### PŘEVEDENÍ NA MALÁ PÍSMENA ########################################################
#########################################################################################################  
       
def prevedNaMala():
    malyText=text.get(1.0,END).lower()  
    text.delete(1.0,END)
    text.insert(1.0,malyText)
 
#########################################################################################################
###################### NAHRAZENÍ ZNAKŮ ##################################################################
#########################################################################################################  
    
def nahradZnak():    
    nahrazeny=askstring(u'Nahrazovaný znak',u'Zadejte znak, který chcete nahradit:')     
    nahrazovaci=askstring(u'Znak',u'Zadejte znak, kterým má být nahrazováno:')
    if nahrazeny=="":
        showinfo("Chyba při zadávání","Musíte zadat znak, který chcete nahradit." )
    else:
        obsah = text.get(1.0,END)
        text.delete(1.0,END)    
        for znak in obsah:
            if znak == nahrazeny:
                text.insert(END,nahrazovaci)
            else:
                text.insert(END,znak)
 
#########################################################################################################
###################### STATISTIKA VÝSKYTU ZNAKŮ #########################################################
######################################################################################################### 

 
def statistika():
    znaky={}
    obsah = text.get(1.0,END)
    popisky = []
    for znak in obsah:
        if znak!="" and znak!="\n" and znak!=" ":
            if znaky.has_key(znak):
                znaky[znak]+=1
            else:
                znaky[znak]=1
                popisky.append(znak)
        
    idZnaku = range(0,len(znaky))
    pocetZnaku = []
    
    for klic in popisky:
        pocetZnaku.append(znaky[klic])
        
    plt.bar(idZnaku, pocetZnaku, align='center')
    plt.xticks(idZnaku, popisky)
    plt.show()

#########################################################################################################
###################### VYGENEROVÁNÍ NÁHODNÉHO TEXTU #####################################################
#########################################################################################################

def vygenerujText():
    menuSoubor.entryconfig(2,state="normal")  
    pocetSlov=askinteger("",u'Zadejte počet slov:')     
    maxPocetSlovVeVete=askinteger("",u'Zadejte maximální počet slov ve větě:')    
    maxDelkaSlova=askinteger("",u'Zadejte maximální délku slova:')   
    
    if pocetSlov>500 or maxDelkaSlova>10 or pocetSlov<1 or maxDelkaSlova < 1:
        showinfo("Chyba při zadávání","Počet slov musí být v rozsahu 1 - 500. Délka slova musí být v rozsahu 1 - 10." )
    else:
        aktualniPocetSlov=0
        text.delete(1.0,END)
        while aktualniPocetSlov<pocetSlov:
            if (pocetSlov-aktualniPocetSlov<maxPocetSlovVeVete):
                maxPocetSlovVeVete=pocetSlov-aktualniPocetSlov
            aktualniPocetSlov+=vygeneruj_vetu(maxDelkaSlova,maxPocetSlovVeVete)

def vygeneruj_slovo(maxDelkaSlova):
    slovo=""
    samohlasky=[97,101,105,111,117,121]
    if random.randint(0,1)==1:
        samohlaska=False
    else:
        samohlaska=True
    while len(slovo)<random.randint(1,maxDelkaSlova):
        nahodne_pismeno=random.randint(ord('a'),ord('z'))
        if samohlaska==True and samohlasky.count(nahodne_pismeno)==0:
            samohlaska=False
            slovo+=chr(nahodne_pismeno)   
        elif samohlaska==False: 
            samohlaska=True
            slovo+=chr(samohlasky[random.randint(0,5)])
    return slovo

def vygeneruj_vetu(maxDelkaSlova,maxPocetSlovVeVete):
    veta=""
    pocetSlov=0
    prvni_slovo=vygeneruj_slovo(maxDelkaSlova)
    pocetSlov+=1
    veta+=chr(ord(prvni_slovo[0])+ord("A")-ord("a"))+prvni_slovo[1:]
    for i in range(random.randint(1,maxPocetSlovVeVete)):
        veta+=" "+vygeneruj_slovo(maxDelkaSlova)
        pocetSlov+=1
    veta+=". "
    text.insert(END,veta)
    return pocetSlov
    

#########################################################################################################
###################### GRAFICKÉ UI ######################################################################
#########################################################################################################  
  
hlavni = Tk()
hlavni.title("Editor souborů")

hlavniMenu = Menu(hlavni)

# Souborové menu
menuSoubor = Menu(hlavniMenu, tearoff=0)
menuSoubor.add_command(label="Otevřít", command=otevritSoubor)
menuSoubor.add_command(label="Uložit", state="disabled", command=ulozit)
menuSoubor.add_command(label="Uložit jako", state="disabled", command=ulozitJako)
menuSoubor.add_separator()
menuSoubor.add_command(label="Nový", command=novySoubor)
menuSoubor.add_command(label="Zavřít", command=zavritSoubor, state="disabled")
hlavniMenu.add_cascade(label="Soubor", menu=menuSoubor)


# Menu úprav
menuUpravy = Menu(hlavniMenu, tearoff=0)
menuUpravy.add_command(label="Převést na malé písmena", command=prevedNaMala)
menuUpravy.add_command(label="Nahradit znak jiným znakem",command=nahradZnak)
menuUpravy.add_command(label="Provést statistiku výskytu", command=statistika)
menuUpravy.add_command(label="Vygenerovat náhodný text", command=vygenerujText)
hlavniMenu.add_cascade(label="Upravit", menu=menuUpravy)

hlavniMenu.add_command(label="Konec", command=hlavni.quit)

# 
hlavni.config(menu=hlavniMenu)

text=Text()
text.pack(fill=BOTH, expand=1)


hlavni.mainloop()