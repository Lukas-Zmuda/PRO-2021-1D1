import tkinter
canvas = tkinter.Canvas()

canvas.create_line(20, 50, 100, 50, fill = 'blue',width = 3)
canvas.create_line(20, 50, 20, 100, width = 5)
canvas.create_line(20, 100, 100, 50, fill = 'red')

canvas.create_line(20, 100, 100, 100, 20, 150, 20, 100, fill = 'green', width = 2)
canvas.pack()
