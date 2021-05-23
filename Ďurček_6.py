import tkinter
import random
from random import *

canvas = tkinter.Canvas()
canvas = tkinter.Canvas(width=1450,height=800)
canvas.pack()

# 1

def vagon(x,y):
    canvas.create_rectangle(x,y,x+120,y+40,fill="green")
    canvas.create_rectangle(x+5,y+5,x+45,y+20,fill="blue")
    canvas.create_rectangle(x+75,y+5,x+115,y+20,fill="blue")
    canvas.create_oval(x+10,y+30,x+ 30, y+50,fill="black")

    canvas.create_oval(x+90,y+30, x+110, y+50,fill="black")
    canvas.create_rectangle(x-10,y+15,x,y+25,fill="green")
    
for i in range(1, 5):
    vagon(i*130, 300)
    
# 2

def rusen():
    x = 40
    y = 300
    canvas.create_rectangle(x,y+10,x+80,y+40,fill="green")
    canvas.create_rectangle(x+40,y-5,x+80,y+10,fill="red")
    canvas.create_rectangle(x+10,y,x+20,y+10,fill="blue")
    canvas.create_oval(x,y+40,x+20, y+60,fill="black")
    canvas.create_oval(x+20,y+40,x+40, y+60,fill="black")
    canvas.create_oval(x+40,y+40,x+60, y+60,fill="black")
    canvas.create_oval(x+60,y+40,x+80, y+60,fill="black")

    
rusen()

# 3
def rgb(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def tvar (x,y):
    for i in range(1,5):
        y = y 
        x = x + 100
        velkost = randrange(-5,5)
        farba = rgb(randrange(100),randrange(150),randrange(200))
        farba1 = rgb(randrange(150),randrange(100),randrange(200))
        farba2 = rgb(randrange(200),randrange(150),randrange(150))
        o = randrange(-2,2)
        u = randrange(-2,2)
        us = randrange(-10,3)
        canvas.create_rectangle(x+110,y+50, x+150, y+100)
        canvas.create_rectangle(x+115,y +60,x+125+velkost, y + 70+velkost,fill=farba)
        canvas.create_rectangle(x+135,y +60, x+145+velkost,y + 70+velkost,fill=farba)
        canvas.create_rectangle(x+125-o,y+75-o,x+140+o,y+90+o,fill=farba1)
        canvas.create_rectangle(x+115-us,y+92-u,x+145+us,y+97+u,fill=farba2)
    
    

tvar(500,250)

# 4

def auto (x,y):
    canvas.create_rectangle(x,y,x+200,y+100,fill="red")
    canvas.create_rectangle(x+200,y+20,x+250,y+100,fill="black")
    canvas.create_rectangle(x+230,y+35,x+245,y+62,fill="blue")
    canvas.create_oval(x+20,y+80,x+60,y+120,fill="black")
    canvas.create_oval(x+30,y+90,x+50,y+110,fill="white")
    canvas.create_oval(x+140,y+80,x+180,y+120,fill="black")
    canvas.create_oval(x+150,y+90,x+170,y+110,fill="white")

auto(300,400)

# 5

def post (x,y):
    canvas.create_line(x+100, y+100, x+125, y+50, x+150, y+100)
    canvas.create_line(x+100, y+100,x+150, y+100)
    canvas.create_oval(x+112,y+25,x+138, y+50,fill="red")
    canvas.create_rectangle(x+110,y+100,x+120,y+125,fill="red")
    canvas.create_rectangle(x+130,y+100,x+140,y+125,fill="red")
    
post(100,10)

# 6

def hrad (x,y):
    canvas.create_line(x+100, y+100, x+125, y+20, x+150, y+100)
    canvas.create_line(x+100, y+100,x+150, y+100)
    canvas.create_line(x+300, y+100, x+325, y+20, x+350, y+100)
    canvas.create_line(x+300, y+100,x+350, y+100)
    canvas.create_rectangle(x+100, y+100,x+350, y+200)
    canvas.create_oval(x+125,y+115,x+145,y+140,fill="blue")
    canvas.create_oval(x+305,y+115,x+325,y+140,fill="blue")
    canvas.create_rectangle(x+175, y+80,x+195, y+100,fill="red")
    canvas.create_rectangle(x+215, y+80,x+235, y+100,fill="red")
    canvas.create_rectangle(x+255, y+80,x+275, y+100,fill="red")
    

hrad(500, 50)











    

