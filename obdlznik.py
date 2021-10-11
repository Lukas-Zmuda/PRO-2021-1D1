import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 50, 150, 100, fill = 'blue',
                outline = 'yellow', width = 3)

canvas.create_rectangle(150, 50, 250, 100, fill = 'red',
                outline = 'yellow', width = 3)

canvas.create_rectangle(50, 100, 150, 150, fill = 'black',
                outline = 'yellow', width = 3)
