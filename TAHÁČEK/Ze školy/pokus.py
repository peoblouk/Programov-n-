# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:56:39 2013


"""

"""

Úkol:
    1)  Napiště funkci "Koktavost", která bude mít jako prametr řetězec.
        Výsledkem bude řetězec, ve kterém budou všechna písmena zdvojena.
    2) Upravit tak nějak trochu .... :P
     
"""

def Koktavost(ret,*pismena):
        vysledek=""
        for znak in ret:
            if znak in pismena:
                vysledek+=3*znak
            else: vysledek+=znak
        return vysledek
        
print Koktavost("Stromoradi","a","o")