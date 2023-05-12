# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:31:18 2013


"""
"""
existuje i knihovna time
"""


from datetime import *

dnes = datetime.now()
print str(dnes)


print "Aktualni rok: %d %x" % (dnes.year,dnes.year)

"""print "Aktualni mesic: %d" % dnes.month
print "Aktualni den: %d" % dnes.day
print "Aktualni hodina: %d" % dnes.hour
print "Aktualni minuta: %d" % dnes.minute
print "Aktualni vterina: %d" % dnes.second
print "Aktualni mikrosekunda: %d" % dnes.microsecond
"""

"""
Úkol:
1) Naprogramujte formulářové digitální hodiny, které 
   každou desetinu sekundy aktualizují svůj čas. 
   Zobrazujte pouze h:m:s. Využijte metodu after.
"""   