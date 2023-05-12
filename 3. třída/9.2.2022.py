from copy import deepcopy


friends = ["Petr", "Pavel", "Tom", "Katka", "Klára", "Jiří", "Zdeněk"]
stastna_cisla = [3, 4, 7, 13, 23, 27, 43]

"""
# výpis range (vypíše se 2. 3. 4. položka ze seznamu)
print(friends[1:4])

# změna hodnoty
friends[3] = "Lucka"

# rozšíření o jiný seznam
friends.extend(stastna_cisla)

# rozšíření po jednom argumentu
friends.append("Lukáš")

# vezme index a všihne to novou položku a posune seznam
friends.insert(1, "Marcel")

# odebrání položky ze seznamu
friends.remove("Pavel")

# odstranění 
friends.remove(friends[1])

# čištění seznamu
friends.clear()

# odstranění člena ze seznamu (parametr lze dát pořadové číslo ze seznamu)
friends.pop()

# výpočet položek ze seznamu
count = friends.count("Petr")
print(count)

# abecední seřazení
friends.sort()

# kopírování seznamu
friends2 = friends.copy()



print(friends)

"""

cisla = list(range(20))
print(cisla)

prvni, *ostani, posledni = cisla
print(prvni)
print(ostatni)
print(posledni)