# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012


"""
"""     Soubory (textové)
open(cesta,mód) - otevře soubor a nastaví způsob
                  přístupu (mód)

binární zápis 255: 11111111
textový zápis 255: 00110010 00110101 00110101



módy:
  'r' - otevře daný soubor pro čtení, soubor musí
        existovat
  'r+' - otevře existující soubor jak pro čtení, tak pro zápis
  'w' - otevře pro zápis, neexistující soubor bude
        vytvořen, existující soub. bude přepsán
  'a' - pro zápis na konec souboru, neexistující 
        bude vytvořen

close() - zavře soubor, způsobí uložení, uvolní jej
          pro jiné aplikace
flush() - vynucené uložení souboru
write() - zapíše do souboru daný řetězec na aktuální
          pozici
writelines() - zapíše do souboru seznam řádků         
  
"""

   
#seznam=[u'První řádek\n',u"Druhý řádek\n",u"Třetí řádek\n"]
"""
soubor=open('pokus.txt','w')
soubor.write(u'První řádek\n')
soubor.write(u'Druhý řádek\n')
soubor.write(str(1000))
#soubor.writelines(seznam)

soubor.close()


""" 

import random
soubor=open('cisla.txt','w')
for i in range(100):
    x=random.randint(1,1000)
    soubor.write("%i\n" % (x))  #str(x)+"\n"    
soubor.close()




"""
Úkoly:
1) Zapište do souboru CISLA.TXT pod sebe čísla od 1 
   do 1000.
   (Rozšíření: ka každému číslu doplnit jeho dělitele)
2) Opakovací:
   Načtěte z klávesnice název nového souboru, načtěte 
   řetězec a zapište jej do zadaného souboru.
"""   