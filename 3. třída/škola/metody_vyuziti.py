veta = "Python je skvely objektove orientovany, interpretovany a interaktivni programovaci jazyk."
abc = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


pocet = 0

# vytvoření listu
list = list(veta)

# a
print("a.")
for a in veta:
    pocet = pocet + 1
print(pocet)

# b
print("b.")
pocet = 0
for pismeno in veta:
    if pismeno in abc:
        pocet = pocet + 1
print(pocet)

# c
print("c.")
pocet_a = list.count("a")
pocet_e = list.count("a")

print(f"počet a : {pocet_a}")
print(f"počet e : {pocet_e}")

# d
print("d.")
hledani = veta.count("python")
for word in range(0, hledani):
    print(word)

# e
print("e.")
if "e" in veta:
    print("ano")
else:
    print("ne")

# f
print("f.")
znak = veta[12]
for i in range(0, 50):
    print(znak)

# g
print("g.")
print(veta.replace("e", "x"))

# h
print("h.")
print("uppercase")
print(veta.upper())
