import time as t

"""
ucebna_elm2 = 1
ucebna_elm1 = 3
chodba_pav = 5
ucebna_pav = 6
jidelna = 5
ucebna_praxe = 9
okno_mit = 10
chodba_mezi_budovami = 11
vstupni_hala = 12
satny = 13
vychod = 14
"""

# nastaveni
body = 1
time = 1.5

# úvodní hláška
print("-------------------------------------")
print("Vítej ve hře zvané Escape from SPSEOL")
t.sleep(time)
print("Tvým úkolem je dostat se ven ze školy")

# pravidla
print("1) pokud zadáš číslo mimo rozsah máš už pouze jednu možnost to napravit")
print("2) dodržuj kritéria, která jsou stanovena")
print("3) bav se")

t.sleep(time + 3)
while body <= 9:

    # konec hry
    if (body == 0):
        print("Game over")
        t.sleep(time + 2)
        print("---------------")
        raise SystemExit

    # č.1 (ucebna_elm2)
    if (body == 1):
        print("--------------------------------")
        print("Právě se nacházíš v učebně ELM 2")
        print("máš na výběr ze tří cest")
        print("")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr vlevo zadej číslo 2")
        print("pro směr přímo zadej číslo 3")
        t.sleep(time)
        smer = int(input("vyber směr: "))

        # mimo rozsah číslo
        if (smer >= 4):
            smer = int(input("vyber směr: "))

        # směr vpravo (ucebna_elm3)
        if (smer == 1):
            print("-------------------------")
            print("Vešel jsi do učebny ELM 3")
            t.sleep(time)
            print("")
            print("máš na výběr ze dvou cest")
            print("pro směr vpravo zadej číslo 1")
            print("pro směr zpět zadej číslo 2")
            smer1 = int(input("vyber směr: "))

            # mimo rozsah číslo
            if (smer >= 3):
                smer1 = int(input("vyber směr: "))

            # směr zpět
            if (smer1 == 2):
                body = 1

            # směr vpravo (okno_2)
            if (smer1 == 1):
                print("Právě jsi vyskočil z okna")
                t.sleep(time + 1)
                print("skok jsi nepřežil")
                t.sleep(time)
                body = 0

        # směr vlevo (okno_1)
        if (smer == 2):
            print("Právě jsi vyskočil z okna")
            t.sleep(3)
            print("skok jsi nepřežil")
            t.sleep(time)
            body = 0

        # směr přímo (ucebna_elm1)
        if (smer == 3):
            body = 3

    # č.3 (ucebna_elm1)
    if (body == 3):
        print("-------------------------")
        print("Vešel jsi do učebny ELM 1")
        t.sleep(time)
        print("")
        print("máš na výběr ze dvou cest")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr přímo zadej číslo 2")
        smer = int(input("vyber směr: "))

        # mimo rozsah číslo
        if (smer >= 3):
            smer = int(input("vyber směr: "))

        # směr vpravo (zkratka do ucebna_praxe)
        if (smer == 1):
            print("Našel jsi zkratku")
            print("ovšem pokud jí chceš využít musíš splnit úkol")
            t.sleep(time)

            # ukol zkratka1
            print(
                "jelikož jsi byl v učebně ELM 1, kde se vyučuje elektrotechnické měření,")
            print("předmět občasně těžký,")
            print("tak je zde otázka zda umíš převést 0,001A na mA?")

            odpoved2 = int(input("odpoveď: "))
            if (odpoved2 == 1):
                print("správná odpoveď")
                print("můžeš užít zkratku")
                body = 5

            else:
                print("špatná odpoveď")
                t.sleep(time)
                print("pan Losert by tě poslal zpět do 1. třídy,")
                t.sleep(time)
                print("ani na distanční výuku by ses nemohl vymluvit")
                body = 0

            # směr přímo (chodba_pav)
        if (smer == 2):
            body = 4

    # č.4 (chodba_pav)
    if (body == 4):
        print("----------------------------")
        print("Vešel jsi na chodbu před PAV")
        print("")
        t.sleep(time)
        print("máš na výběr ze dvou cest")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr přímo zadej číslo 2")
        smer = int(input("vyber směr: "))

        # mimo rozsah číslo
        if (smer >= 3):
            smer = int(input("vyber směr: "))

        # směr vpravo (ucebna_pav)
        if (smer == 1):
            print("-----------------------")
            print("Vešel jsi do učebny PAV")
            print("")
            # úkol PAV
            print(
                "jelikož se nacházíš v učebně PAV, kde se většinou vyučuje předmět automatizace,")
            print("tak je zde otázka zda znáš, jeden typ regulace?")
            odpoved1 = input("odpoveď (použíj diakritiku): ")
            odpoved1.lower()
            x = ["spojitá", "nespojitá"]
            if (odpoved1 in x):
                print("správná odpoveď")
                print("vracíš se zpět na chodbu před PAV")
                body = 4

            else:
                print("Špatná odpoveď!")
                t.sleep(time)
                print("pan Kyselý by se zlobil začni tedy znovu!")
                body = 0

        # směr přimo (jidelna)
        if (smer == 2):
            body = 5
    # č.5 (jidelna)
    if (body == 5):
        print("--------------------")
        print("Vešel jsi do jídelny")
        print("")
        t.sleep(time)
        print("máš na výběr ze dvou cest")
        print("pro směr vpravo zadej číslo 1")
        print("pro směr přímo zadej číslo 2")
        smer = int(input("vyber směr: "))

        # mimo rozsah číslo
        if (smer >= 3):
            smer = int(input("vyber směr: "))

        # směr vpravo (ucebna_praxe)
        if (smer == 1):
            print("--------------------------")
            print("Vešel jsi do učebny praxí")
            print("")
            t.sleep(time)
            print("Pan Hanina tě načapal a chce, aby jsi řekl")
            print("jaké označení má fázový vodič?")
            odpoved1 = input("odpoveď : ")
            y = ["L", "l"]
            if (odpoved1 in y):
                print("Správná odpoveď!")
                t.sleep(time)
                print("vracíš se zpět do jídelny")
                body = 5

            else:
                print("Špatná odpoveď!")
                t.sleep(time)
                print("číslo 155 bylo vytočeno")
                body = 0
