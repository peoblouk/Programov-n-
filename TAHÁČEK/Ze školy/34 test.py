# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:12:01 2013


"""

den=input("Zadej den: ")
mesic=input("Zadej mesic: ")
rok=input("Zadej rok: ")
 
def VypisDatum(den,mesic,rok): 
    if mesic<13:
        if mesic==1:
            x="leden"
        if mesic==2:
            x="unor"
        if mesic==3:
            x="brezen"
        if mesic==4:
            x="duben"
        if mesic==5:
            x="kveten"
        if mesic==6:
            x="cerven"
        if mesic==7:
            x="cervenec"
        if mesic==8:
            x="srpen"
        if mesic==9:
            x="zaru"
        if mesic==10:
            x="rijen"
        if mesic==11:
            x="listopad"
        if mesic==12:
            x="prosinec"
    
        print "Datum je" ,den, ".", x, rok
   
    if mesic>12:
        print "Spatne zadany mesic!"
    
print VypisDatum(den,mesic,rok)