import tkinter
from random import *
cn = tkinter.Canvas()
cn.pack()
cn.config(height=800, width=1400)

cnr = cn.create_rectangle
cnt = cn.create_text
cnl = cn.create_line
cno = cn.create_oval

# 1,2
cnl(0, 400, 1400, 400)
    
def tvar(xy):
    x = xy.x
    y = xy.y
    
    if y<400:
        cnr(x,y,x+20,y+20,fill='blue')
    else:
        cno(x,y,x+20,y+20,fill='yellow')

# 3

def ciary(xy):
    x = xy.x
    y = xy.y

    if x<700 and y<=400:
        f = 'red'
    if x<700 and y>=400:
        f = 'green'
    if x>700 and y<=400:
        f = 'blue'
    if x>700 and y>=400:
        f = 'yellow'

    cnl(700,400, x,y, fill = f)

# 4

def hol_vlajka(xy):
    x = xy.x
    y = xy.y

    if y<266:
        f = 'red'
    if y>=267 and y<532:
        f = 'white'
    if y>=533:
        f = 'blue'

    cno(x, y, x+20, y+20, fill = f)

# 5, 6

def pozdravy(event):
    x = randrange(1400)
    y = randrange(800)
    ch = event.char
    
    if ch=='a':
        slovo='ahoj'
        f = 'orange'
    elif ch=='b':
        slovo ='bye'
        f = 'blue'
    elif ch=='c':
        slovo ='cau'
        f = 'red'
    elif ch=='d':
        slovo ='dobry den'
        f = 'brown'
    elif ch=='e':
        slovo='hello there'
        f = 'green'
    elif ch=='n':
        slovo ='nazdar'
        f = 'yellow'
    else:
        slovo ='Daj ine pismeno lebo k tomuto nemam pozdrav'
        f = 'black'
    
    cnt(x, y, text = slovo, fill = f)

cn.bind('<Button-1>', tvar)
cn.bind('<Button-3>', ciary)
cn.bind('<B2-Motion>', hol_vlajka)
cn.bind('<Button-2>', hol_vlajka)
cn.bind_all('<Key>', pozdravy)
