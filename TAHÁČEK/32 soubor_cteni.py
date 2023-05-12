# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012


"""
"""     Soubory (čtení)
        
readlines() - vrátí seznam řádků souboru          
readline() - přečte řetězec od aktuální pozice do 
             konce řádku  
read(x) - přečte řetězec o zadané délce, když neuvedeme
          hodnotu, přečte celý soubor
        - při pokusu o čtení na konci souboru vrací
          prázdný řetězec ""
tell() - vrací aktuální pozici v souboru
seek(pocet,pozice) - posune ukazatel o daný počet
                    bytů od zadané pozice
   pozice:
    0 - začátek souboru
    1 - aktuální pozice
    2 - konec souboru       
"""
"""
soub=open("cisla.txt","r")
sez=soub.readlines()
soub.close()
print sez

for i in range(len(sez)):
    sez[i]=sez[i][:-1]

print sez
"""
"""
soubor=open("32 soubor_zapis.py","r")
seznam=soubor.readlines()
for i in seznam:
    print i,
soubor.close()



"""
"""
soubor=open("32 soubor_zapis.py","r")
soubor.readline()
soubor.readline()
ret=soubor.readline()
print ret 
soubor.close()

"""
"""
soubor=open("32 soubor_zapis.py","r")
vsechno=soubor.read()

soubor.seek(-7,1)
znak=soubor.read(1)
print vsechno
print [znak] 
soubor.close()



"""
soubor=open("32 soubor_zapis.py","r")
#print soubor
print soubor.tell()
soubor.read(10)
print soubor.tell()
soubor.close()


"""
Úkoly:
1) Otevřete soubor pokus.txt a vypište jeho 
   obsah do souboru kopie.txt. 
   Použijte buď readlines nebo read.
2) Vygenerujte soubor VSTUP.TXT, ve kterém budou dva
   sloupce dvojciferných čísel oddělené mezerou. V
   každém bude 100 čísel.
   Tento soubor postupně přečtěte a do jineho souboru
   vypište řádkové součty ve formátu a+b=c.
3) Přečtěte soubor PISMENA.TXT znak po znaku a 
   zjistěte, kolik je v něm písmen "a".
4) Načtěte ze souboru datum a otestujte správnost jeho
   formátu (dd.mm.rrrr).   
"""   
