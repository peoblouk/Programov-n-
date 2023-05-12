import tkinter as tk
from tkinter import Frame

import customtkinter as ctk
import time as t


class Application(ctk.CTk):
    name = "Prasátko"

    def __init__(self):
        #! Pojmenování prasátka a zadání cesty a vytvoření proměnných
        prase_jmeno = "Prasatko"
        prase_cesta = "prasatko2.txt"
        self.jmeno = prase_jmeno
        self.cesta = "prasatka/" + prase_cesta
        self.dostupne_penize = 0
        self.bankovky = {}  # slovník s bankovky
        self.vyber_dict = {}  # pomocný slovník
        self.time = 1.4  # čas odpovědi
        super().__init__(className=self.name)

        #! Nastavení okna aplikace
        self.title(self.name)
        self.icon = self.iconbitmap("img/icon.ico")  # ikonka aplikace
        self.resizable(False, False)
        self.geometry("400x400+800+300")  # pozice otevření okna
        self.bind("<Escape>", self.quit)  # reakce na klávesnici vyvolá funkci quit
        self.read()  # načti ze souboru
        self.set_appearance_mode("System")  # m odes

        # Label info
        self.lblInfo = ctk.CTkLabel(
            self,
            text="Prasátko",
            bg="#33727a",
            text_color="white",
        )
        self.lblInfo.pack(side="top")

        # Label počet peněz
        self.lblPocetpenez = ctk.CTkLabel(self, width=6, text=self.dostupne_penize)
        self.lblPocetpenez.pack(side="top", pady=7)
        ####

        #! Frame Entry Sypej
        self.amouth = tk.StringVar()  # proměnná pro Entry
        self.amouth.trace_add("write", self.value_change)
        self.frameEntry = ctk.CTkFrame(self)
        self.frameEntry.pack(side="left", anchor="s")
        self.frameEntry.pack(padx=10, pady=100)
        self.entrySypej = ctk.CTkEntry(
            self.frameEntry, textvariable=self.amouth, width=80
        )
        self.entrySypej.focus()  # zaměření na Entry
        self.entrySypej.pack()
        ####

        self.btnSypej = ctk.CTkButton(
            self.frameEntry,
            command=self.sypej,
            text="Sypej!!!",
            width=80,
        )
        self.btnSypej.pack(pady=5)
        ####

        #! Frame Obsah trezoru
        self.frameObsahtrezoru = ctk.CTkFrame(
            self,
        )  # fram pro obsah trezoru
        self.frameObsahtrezoru.pack(side="bottom", pady=20, padx=5)

        # listbox Obsah trezoru
        self.TextObsahtrezoru = ctk.CTkTextbox(
            self.frameObsahtrezoru, height=200, width=80
        )
        self.TextObsahtrezoru.pack()
        self.refresh()

        self.status = tk.StringVar()
        self.status.trace("w", self.value_change or self.sypej)
        self.lblStatus = ctk.CTkLabel(
            self.frameObsahtrezoru, textvariable=self.status, height=10, width=20
        )
        self.lblStatus.pack(side="bottom")
        ####

    ###############
    #! Funkce na načtení bankovek z prasátka
    def read(self):
        try:
            with open(self.cesta, "r") as prase:
                while line := prase.readline():  # pro každý řádek
                    self.bankovky[line.split()[0]] = line.split()[1]
            self.vyber_dict = dict.fromkeys(self.bankovky.keys(), 0)
            self.dostupne_penize = sum(
                [int(bill) * int(self.bankovky[bill]) for bill in self.bankovky.keys()]
            )
            return self.dostupne_penize and self.bankovky
        except FileNotFoundError:
            print("Soubor neexistuje!")
            raise SystemExit

    #! Funkce na opuštění programu
    def quit(self, event=None):
        super().quit()  # umístění widgetu do okna
        ####

    #! Funkce na aktualizaci status
    def print_error(self):
        self.entrySypej.delete(0, "end")  # vymazání vstupu entry po odeslání
        self.status.set("Error!")
        ####

    #! Funkce na aktualizaci status
    def print_success(self):
        self.entrySypej.delete(0, "end")  # vymazání vstupu entry po odeslání
        self.status.set("Hotovo!")
        ####

    #! Funkce na ošetření Entry
    def value_change(self, var, index, mode):
        self.amouth.set(
            "".join([char for char in list(self.amouth.get()) if char.isdigit()])
        )  # ošetření vstupu
        ####

    #! Funkce na refresh obsahu trezoru
    def refresh(self):
        self.read()
        self.lblPocetpenez.configure(
            text=self.dostupne_penize
        )  # aktualizace lblPocetpeněz
        self.TextObsahtrezoru.destroy()
        self.TextObsahtrezoru = ctk.CTkTextbox(
            self.frameObsahtrezoru, height=200, width=80
        )
        self.TextObsahtrezoru.pack(side="top")
        self.TextObsahtrezoru.insert(
            "0.0",
            "".join(
                [
                    key
                    for key, value in (self.bankovky.items())
                    if self.TextObsahtrezoru.insert("end", f"{key:5} - {value:3}x\n")
                ]
            ),
        )
        ####

    #! Funkce výběr bankovek z prasátka
    def sypej(self):
        pokus = 0
        self.status.set("pracuji..")
        try:
            kolik_vybrat = int(self.amouth.get())
        except ValueError:
            self.print_error()
            print(self.print_error)

        pozadavek = kolik_vybrat
        if kolik_vybrat <= self.dostupne_penize:
            while kolik_vybrat > 0:
                for bankovka in self.bankovky:
                    potrebny_pocet = kolik_vybrat // int(bankovka)

                    if potrebny_pocet > int(self.bankovky[bankovka]):
                        self.vyber_dict[bankovka] = int(self.bankovky[bankovka])
                        kolik_vybrat -= int(bankovka) * int(self.bankovky[bankovka])

                    else:
                        self.vyber_dict[bankovka] = potrebny_pocet
                        kolik_vybrat -= int(bankovka) * potrebny_pocet
                pokus += 1  # ošetření loopu
                if pokus >= 10:
                    kolik_vybrat = 0
                    break
            if (
                sum(
                    [
                        int(bill) * int(self.vyber_dict[bill])
                        for bill in self.vyber_dict.keys()
                    ]
                )
                == pozadavek
            ):
                with open(self.cesta, "w") as prase:
                    for bankovka in self.bankovky:
                        prase.write(
                            f"{bankovka} {int(self.bankovky[bankovka]) - self.vyber_dict[bankovka]}\n"
                        )
                self.print_success()
                return self.refresh()
            else:
                print("V prasátku nejsou dost různorodé peníze.\n")
                self.print_error()
        elif kolik_vybrat == 0:
            self.print_error()
            print("Nemůže být 0!\n")

        else:
            print("V prasátku není dost peněz!\n")
            self.print_error()
        ####

    ###############


app = Application()
app.mainloop()  # kontrola stisku klávesnice, pohybu myši
