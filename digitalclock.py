# importando os modulos

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.tittle('Clock')


def time():
    string = strftime('%H:%M:S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
