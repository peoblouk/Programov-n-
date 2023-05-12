"""
 * @author [Petr Oblouk]
 * @github [https://github.com/peoblouk]
 * @create date 09-01-2023 - 09:20:39
 * @modify date 09-01-2023 - 09:20:39
 * @desc [Kalkulačka]
"""
from os.path import basename, splitext
import tkinter as tk
import operator
import math as m

#! Přehození radianů na stupně
rad2rad = lambda x: x
deg2rad = m.radians
wrap = deg2rad  # ukazatel na funkce

opr1 = {
    "sin": lambda x: m.sin(wrap(x)),
    "cos": m.cos,
    "tan": m.tan,
    "tg" : m.tan,
}

opr2 = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**':operator.pow,
    "//":lambda x,y: x // y,
}

const = {
    'pi': m.pi,
    'e': m.e,
}

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = "Kalkulačka"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.geometry("300x400+80+80")  # pozice otevření okna
        self.bind("<Escape>", self.quit)
        self.config(bg="#808080")
        self.lbl = tk.Label(self, text="Hello Kalkukačka")
        self.lbl.pack(anchor="center")
        self.lbl.config(bg="#808080")
        
        #! Main frame
        self.ObsahFrame = tk.Frame(self)
        self.ObsahFrame.pack(anchor="center")
        self.ObsahFrame.config(bg="#808080")
        
        # entry user
        self.entry = MyEntry(self.ObsahFrame)
        self.entry.pack(anchor="w",side="top")
        self.entry.bind("<KP_Enter>", self.process) # reakce na enter
        self.entry.bind("<Return>", self.process) # reakce na enter u numpadu
        self.entry.config(bg="#808080")

        # listbox
        self.listbox = tk.Listbox(self.ObsahFrame)
        self.listbox.pack(anchor="w",side="left")
        self.listbox.config(bg="#808080")

        self.FrameBtn = tk.Frame(self.ObsahFrame)
        self.FrameBtn.pack(side="right")
        self.FrameBtn.config(bg="#808080")


        # tlačítka
        self.btnUp = tk.Button(self.FrameBtn, text="↑",command=self.Up)
        self.btnUp.config(bg="#d7f4ff")
        self.btnUp.pack()

        self.btnDown = tk.Button(self.FrameBtn, text="↓", command=self.Down)
        self.btnUp.config(bg="#d7f4ff")
        self.btnDown.pack()

        self.btnCopy = tk.Button(self.FrameBtn, text="copy", command=self.Copy)
        self.btnCopy.config(bg="#1b6884")
        self.listbox.bind("<c>", self.Copy)
        self.btnCopy.pack()

        self.btnDel = tk.Button(self.FrameBtn, text="del", command=self.Delete)
        self.btnDel.config(bg="#4dbfe9")
        self.listbox.bind("<Delete>", self.Delete)
        self.btnDel.pack()
        
        # klávesové zkratky


        # label status
        self.status = tk.StringVar()
        # self.status.trace("w", self.process)
        self.status.set("ESC to kill app !!")
        self.lblStatus = tk.Label(
            self, textvariable=self.status, height=10, width=50
        )
        self.lblStatus.pack(anchor="center")
        self.lblStatus.config(bg="#808080")

    def focus_on(self,index_of):
        self.listbox.select_set(index_of)
        self.listbox.activate(index_of)

    def process(self, e: tk.Event):
        for v in self.entry.value.split():
            self.token_process(v)
        self.entry.value = ""

    def token_process(self, token:str):
        try:
            token = token.replace(",", ".")
            value = float(token)
            self.listbox.insert(0, value)
            self.status.set("")
        except ValueError:
            # operace se dvěma operandy
            if token in opr2 and self.listbox.size() >= 2:
                self.status.set("")
                a = float(self.listbox.get(0))
                self.listbox.delete(0)
                b = float(self.listbox.get(0))
                self.listbox.delete(0)
                self.listbox.insert(0, opr2[token](a,b))

            # operace s jednným operandem
            elif token in opr1 and self.listbox.size() >= 1:
                self.status.set("")
                a = float(self.listbox.get(0))
                self.listbox.delete(0)
                self.listbox.insert(0, opr1[token](a))

            # operace s konstantou
            elif token in const:
                self.status.set("")
                self.listbox.insert(0, const[token])

            # přepínaní stupňů a radianů
            elif token == "deg":
                self.status.set("")
                wrap = rad2rad
            elif token == "rad":
                self.status.set("")
                wrap = deg2rad
        
            else:
                self.status.set("Chyba! Neznámá operace nebo málo operandů!")
    # funkce posun v zásobníku
    def Up(self):
        if self.listbox.size() >= 2:
            try:
                index = self.listbox.index(self.listbox.curselection()[0])
                if index == 0:
                    raise AttributeError
                num1 = self.listbox.get(index)                
                self.listbox.delete(index)
                self.listbox.insert(index-1, num1)
                self.focus_on(index-1)

            except AttributeError:
                self.status.set("Chyba! Špatně vybraná položka")
        else:
            self.status.set("Chyba! Málo operandů pro provedení operace!")

    def Down(self):
        if self.listbox.size() >= 2:
            try:
                index = self.listbox.index(self.listbox.curselection()[0])
                if index >= self.listbox.size()-1:
                    self.status.set("Chyba! nelze dát číslo mimo list!")
                    raise AttributeError
                num1 = self.listbox.get(index)
                self.listbox.delete(index)
                self.listbox.insert(index+1, num1)
                self.focus_on(index+1)

            except AttributeError:
                self.status.set("Chyba! Špatně vybraná položka")
        else:
            self.status.set("Chyba! Málo operandů pro provedení operace!")

    def Copy(self, E=None):
        if self.listbox.size() == 0:
            self.status.set("Chyba! Málo operandů pro provedení operace!")
        else:
            index = self.listbox.index(self.listbox.curselection()[0])
            item = self.listbox.get(index)
            self.listbox.insert((index-1), item)
            self.focus_on(index-1)

    def Delete(self, E=None):
        if self.listbox.size() == 0:
            self.status.set("Chyba! Málo operandů pro provedení operace!")
        else:
            index = self.listbox.index(self.listbox.curselection()[0])
            self.listbox.delete(index,index)
            self.focus_on(0)

    def quit(self, event=None):
        super().quit()
    print("Tady se neobjeví žádné chybové hlášky! :) (snad)")


app = Application()
app.mainloop()
