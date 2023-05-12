import random

"""
while True:
    try:
        vstup = int(input("number: "))
    except:
        print("Wrong input")
        exit()

    number = random.randint(0, 20)

    if vstup == number:
        print("amazing, your number is same as i think")
    else:
        print(f"The was {number}, try it again")

"""
# modely aut
skoda = {"octavia": 0, "kodiaq": 0, "fabia": 0}
renault = {"dacia": 0, "kango": 0, "cole": 0}

try:
    vstup = input("zadejte model auta: ")
except IndexError:
    print("auto není v seznamu")
    exit()

# kontrola a doplňení dictinary
if vstup not in (skoda.keys() or renault.keys()):
    print("není v seznamu")

if vstup in skoda:
    skoda[vstup] = skoda[vstup] + 1

if vstup in renault:
    renault[vstup] = renault[vstup] + 1

print()
for klic, hodnota in skoda.items():
    print(f"{klic}: {hodnota}")

print()
for klic, hodnota in renault.items():
    print(f"{klic}: {hodnota}")
