"""
 * @author [Petr Oblouk]
 * @github [https://github.com/peoblouk]
 * @create date 07-11-2022 - 09:08:30
 * @modify date 07-11-2022 - 09:08:30
 * @desc [Začátek "s" Tkinter]
"""

#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Frame, Canvas, Label, Entry

# from tkinter import ttk


class Application(tk.Tk):  # potomek třídy tk.Tk
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)  # reakce na klávesnici vyvolá funkci quit

        self.color_get()

        self.lblHlavni = tk.Label(self, text="Petr Oblouk ColorMishMash")  # Label
        self.lblHlavni.pack()  # umístění widgetu do okna

        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)  # tlačítko quit
        self.btnQuit.pack()

        # plátno
        self.canvasMain = tk.Canvas(self, width=333, height=333, bg="white")
        self.canvasMain.pack(side="top")
        self.canvasMain.bind("<Button-1>", self.clickHandler)

        ### tlačítka
        #! Red
        self.varRed = tk.IntVar()  # proměnná pro svázání proměnné entry a scale
        self.varRed.trace("w", self.color_change)  # aktualizace barvy na plátnu Canvas
        self.frameRed = Frame(self)
        self.frameRed.pack()
        self.lblRed = tk.Label(self.frameRed, text="R")  # Label red
        self.lblRed.pack(side="left", anchor="s")
        self.scaleRed = Scale(
            self.frameRed,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=333,
            background="#ff0000",
            variable=self.varRed,
        )  # posuvný výběr barev
        self.scaleRed.pack(side="left", anchor="s")
        self.entryRed = tk.Entry(
            self.frameRed, width=4, textvariable=self.varRed
        )  # vstup uživatele
        self.entryRed.bind("<Key>", self.update)  # která klavesa byla stisknuta
        self.entryRed.pack(side="left", anchor="s")

        #! Green
        self.varGreen = tk.IntVar()  # proměnná pro svázání proměnné entry a scale
        self.varGreen.trace(
            "w", self.color_change
        )  # aktualizace barvy na plátnu Canvas
        self.frameGreen = Frame(self)
        self.frameGreen.pack()
        self.lblGreen = tk.Label(self.frameGreen, text="G")  # Label Green
        self.lblGreen.pack(side="left", anchor="s")
        self.scaleGreen = Scale(
            self.frameGreen,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=333,
            background="#00ff00",
            variable=self.varGreen,
        )  # posuvný výběr barev
        self.scaleGreen.pack(side="left", anchor="s")
        self.entryGreen = tk.Entry(
            self.frameGreen, width=4, textvariable=self.varGreen
        )  # vstup uživatele
        self.entryGreen.pack(side="left", anchor="s")
        self.entryGreen.bind("<Key>", self.update)  # která klavesa byla stisknuta
        self.entryGreen.pack(side="left", anchor="s")

        #! Blue
        self.varBlue = tk.IntVar()  # proměnná pro svázání proměnné entry a scale
        self.varBlue.trace("w", self.color_change)  # aktualizace barvy na plátnu Canvas
        self.frameBlue = Frame(self)
        self.frameBlue.pack()
        self.lblBlue = tk.Label(self.frameBlue, text="B")  # Label Blue
        self.lblBlue.pack(side="left", anchor="s")
        self.scaleBlue = Scale(
            self.frameBlue,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=333,
            background="#0000ff",
            variable=self.varBlue,
        )  # posuvný výběr barev
        self.scaleBlue.pack(side="left", anchor="s")
        self.entryBlue = tk.Entry(
            self.frameBlue, width=4, textvariable=self.varBlue
        )  # vstup uživatele
        self.entryBlue.pack(side="left", anchor="s")

        #! Pole s hodnotou v HEX
        self.entryHex = tk.Entry(self, width=8)  # pole s hodnotou RGB
        self.entryHex.pack(anchor="e")

        #! Paměť barev
        self.frameMem = Frame(self)  # frame pro další jednotlivé canvas
        self.frameMem.pack()
        self.canvasMem = []
        self.colorMem = []
        index = 1
        for row in range(3):
            for colum in range(7):
                canvas = tk.Canvas(self.frameMem, width=50, height=50)
                canvas.grid(
                    row=row,
                    column=colum,
                )  # místo pack, zde dáme grid a zadáme součadnice x = row a y = colomn podle cyklu for
                try:
                    canvas.config(bg=self.result[index])
                except IndexError:
                    canvas.config(bg="#123456")
                if index >= 21:
                    index = 1
                index += 1
                canvas.bind("<Button-1>", self.clickHandler)
                self.canvasMem.append(canvas)

    def color_change(self, var=None, index=None, mode=None):
        r = self.varRed.get()
        g = self.varGreen.get()
        b = self.varBlue.get()
        colorstring = f"#{r:02X}{g:02X}{b:02X}"
        self.canvasMain.config(bg=colorstring)
        print(colorstring)

        self.entryHex.delete(0, "end")  # AKLTUALIZACE pole s hodnotou RGB
        self.entryHex.insert(0, colorstring)

    def quit(self, event=None):  #! funkce na opuštění programu
        self.color_save()
        super().quit()  # umístění widgetu do okna

    def update(
        self, event=None
    ):  #! funkce na zjištění klavesy při kliknutí do entryRed,...
        print(event.keycode, event.keysym)

    def clickHandler(self, event):  #! funkce na obsluhu kliknutí
        if self.cget("cursor") != "pencil":  # při kliknutí poprvé
            self.config(cursor="pencil")
            self.color = event.widget.cget("bg")
        else:  # kliknu podruhé
            self.config(cursor="")
            if (
                event.widget is self.canvasMain
            ):  # řešení updatu posuvníku, při vložení hodnoty do canvasMain
                self.canvasColor2Slids()
            event.widget.config(bg=self.color)

    def canvasColor2Slids(self):
        r = int(self.color[1:3], 16)
        g = int(self.color[3:5], 16)
        b = int(self.color[5:], 16)

        self.varRed.set(r)
        self.varGreen.set(b)
        self.varBlue.set(g)

    def color_save(self):
        with open("barvicky.txt", "w") as file:
            for canvas in self.canvasMem:
                file.write(canvas.cget("bg") + "\n")

    def color_get(self):
        self.result = []
        with open("barvicky.txt", "r") as file:
            while line := file.readline():  # pro každý řádek
                self.result.append(line[0:7])
        return self.result


app = Application()
app.mainloop()
