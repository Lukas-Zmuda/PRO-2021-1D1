import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kruzokzlty(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='yellow')

def kruzokcerveny(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')

canvas.bind('<Button-1>', kruzokzlty)
canvas.bind('<Button-3>', kruzokcerveny)
