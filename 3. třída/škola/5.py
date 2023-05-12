#import knihoven
import time as t
import math as m

# deklarace proměnných

vyber_funkce = 0

# úvodní hláška
print("Tento program vám vypočítá délku přepony")
print("")

# smyčka
while True:
    # výběr odvěsny
    if (vyber_funkce == 0):
        print("Vyberte jaká strana je odvěsna: ")
        print("Pokud strana a je odvěsna tak zadejte číslo 1")
        print("Pokud strana b je odvěsna tak zadejte číslo 2")
        print("Pokud strana c je odvěsna tak zadejte číslo 3")
        vyber_funkce = int(input("vyber číslo: "))

        # odvěna je strana a
        if (vyber_funkce == 1):

            odvesna_b = int(input("urči rozměr odvěsny b: "))
            odvesna_c = int(input("urči rozměr odvěsny c: "))
            prepona_a = m.sqrt((odvesna_c ** 2) / (odvesna_b ** 2))
            print(f"délka přepony je: {prepona_a}cm")
            t.sleep(2)
            print("--------------------------------")
            vyber_funkce = 0

        # odvěsna je strana b
        if (vyber_funkce == 2):
            odvesna_a = int(input("urči rozměr odvěsny a: "))
            odvesna_c = int(input("urči rozměr odvěsny c: "))
            prepona_b = m.sqrt((odvesna_c ** 2) / (odvesna_a ** 2))
            print(f"délka přepony je: {prepona_b}cm")
            t.sleep(2)
            print("--------------------------------")
            vyber_funkce = 0

        # odvěsna je strana c
        if (vyber_funkce == 3):
            odvesna_a = int(input("urči rozměr odvěsny a: "))
            odvesna_b = int(input("urči rozměr odvěsny b: "))
            prepona_c = m.sqrt((odvesna_a ** 2) + (odvesna_b ** 2))
            print(f"délka přepony je: {prepona_c}cm")
            t.sleep(2)
            print("--------------------------------")
            vyber_funkce = 0
