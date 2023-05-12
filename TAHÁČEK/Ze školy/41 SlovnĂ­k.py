# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:29:50 2013


"""

"""

Slovníky (hash,asociativní pole)
- vytvářejí se pomocí {}
- položky mají tvar INDEX(KLÍČ): HODNOTA
- indexovat můžeme pomocí lib. dat. typu
- indexy musí být unikátní
- k hodnotám se přistupuje pomocí klíčů
"""

x={5: "five", "nic": None, "cislo": 80}
x["new"]=(24,65)
print x
print x["new"][1]



del x["nic"]   #smaže
print x.keys()
print x.values()
print x.has_key("cislo")
