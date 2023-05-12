# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:01:45 2012


"""

znak=raw_input('Zadej znak: ')
cislo=ord(znak)
print cislo

cislo=input('Zadej cislo znaku: ')
znak=chr(cislo)
print znak

"""
Ukol:
0) Vypište abecedu z malých písmen do řádku  
1) Vygenerujte a vypište náhodný znak z abecedy (Velké 
   písmeno).
2) Vygenerujte náhodné slovo z libovolných malých písmen.
   Maximální délka je 10 a minimální 1.
3) Vygenerujte náhodné slovo z malých písmen tak, aby se 
   střídaly souhlásky a samohlásky. Slovo začíná náhodně
   samohláskou nebo souhláskou.
4) Vygenerujte náhodnou větu. Bude se skládat z náhodného
   počtu slov - min. 1 slovo, max. 15 slov. Věta začíná
   velkým písmenem a končí tečkou.
5) Vygenerujte náhodný text o zadaném množství vět a 
   uložte jej do souboru text.txt. 
6) Vytvořte si pomocný slovník. Uživatel zadá text. 
   Projděte jej a aktualizujte četnosti ve slovníku. 
   Vypište úhlednou statistiku.
"""