import getpass

x = 1

jmeno = input("jmeno > ")
heslo = getpass.getpass("Password:")

login = input("zadejte jmeno > ")
password = input("zadejte heslo > ")

while x == 1:
    if (login in jmeno) and (heslo in login):
        print(f"Vítejte {jmeno}")
        x = 0

    else:
        print("Špatně zadané heslo")
        x = 1
