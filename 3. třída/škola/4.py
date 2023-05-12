import math as m

print("Tento program vám vypočítá z funkci sinus a cosinus pro zadaný úhel")
print("-------------------------------------------------------------------")

uhel = int(input("Zadejte úhel φ (v stupních): "))

cosinus = m.cos(uhel)
sinus = m.sin(uhel)

print(f"Hodnota funkce sinus je: {sinus}")
print(f"Hodnota funkce cosinus je: {cosinus}")
