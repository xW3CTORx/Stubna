
import tkinter
from random import *
cn = tkinter.Canvas()
cn.pack()
cn.config(width = 1450, height = 800)

cnl = cn.create_line
cnr = cn.create_rectangle
cno = cn.create_oval
cnt = cn.create_text

# 1
def x(miesto):
    x = miesto.x
    y = miesto.y
    cnl(x-10, y-10, x+10, y+10)
    cnl(x-10, y+10, x+10, y-10)
    
# 2
def xD(miesto):
    x = miesto.x
    y = miesto.y
    cno(x-20,y-20,x+20,y+20, fill='yellow')
    cno(x-15,y-10,x-10,y-5)
    cno(x+15,y-10,x+10,y-5)
    cnt(x,y+10,text=')',angle=-90)
    
# 3
def zelene(miesto):
    x = miesto.x
    y = miesto.y
    cnl(700,500,x,y,fill='green',width=5)

# 5 
def grid(i):
    for i in range(1,6):
        cnl(10, i*35, 200, i*35)
        cnl(i*35, 10, i*35, 200)
        cn.update()
    cnt(1000, 500, text = 'Lave tlacidlo mysi = o \n Prave tlacidlo mysi = x', font = 'Arial 20 bold')
    
def o(miesto):
    x = miesto.x
    y = miesto.y
    cno(x-10, y-10, x+10, y+10)

#6

def poz(cin):
    print(cin.keysym)
    print(cin.char)
    print(cin.keycode)
    x = randrange(300, 800)
    y = randrange(300, 800)
        
    cnt(x, y, text= "zobrazenie")

    
cn.bind('<Button-1>', o)
cn.bind('<Button-3>', x)
cn.bind('<Button-2>', zelene)
cn.bind_all('<d>', xD)
cn.bind_all('<Return>', grid)
cn.bind_all('<Key>', poz)
cn.bind_all('<space>', poz)
