import tkinter
canvas = tkinter.Canvas(height = 800, width = 800)
canvas.pack()

canvas.create_rectangle (100,100,350,500, fill = "yellow", outline = "yellow")
canvas.create_oval (100,50,350,150, fill = "brown", outline = "brown")
canvas.create_oval (75,100,375,150, fill = "brown", outline = "brown")

canvas.create_line(220,225,230,225, fill = "black",width = 4)
canvas.create_oval (230,190,320,260, fill = "yellow", outline = "black",width = 4)
canvas.create_oval (130,190,220,260, fill = "yellow", outline = "black",width = 4)
canvas.create_line(90,175,130,225, fill = "black",width = 4)
canvas.create_line(360,175,320,225, fill = "black",width = 4)


canvas.create_oval (150,200,200,250, fill = "blue", outline = "blue")
canvas.create_oval (250,200,300,250, fill = "blue", outline = "blue")

canvas.create_rectangle (220, 250, 230, 350, fill = "blue", outline = "blue")

canvas.create_oval (130, 360, 320, 435, fill = "red", outline = "red")
canvas.create_oval (130, 380, 320, 450, fill = "yellow", outline = "yellow")
