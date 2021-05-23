import tkinter
import random
canvas=tkinter.Canvas()
canvas.pack()
canvas.config(height=800, width=1550)

canvas.create_text(10,50, text=random.randint(1,49));
canvas.create_text(30,50, text=random.randint(1,49));
canvas.create_text(50,50, text=random.randint(1,49));
canvas.create_text(70,50, text=random.randint(1,49));
canvas.create_text(90,50, text=random.randint(1,49));
canvas.create_text(110,50, text=random.randint(1,49));
