import tkinter
from random import *

canvas = tkinter.Canvas()
canvas.pack()

def dom():
    x = randint(100, 300)
    y = randint(100, 300)
    canvas.create_rectangle(x, y, x+50, y+50)
    canvas.create_line(x, y, x+25, y-50, x+50, y)
dom()
dom()
dom()
