import tkinter
import random
from random import *

canvas = tkinter.Canvas()
canvas = tkinter.Canvas(width=1900,height=1080)
canvas.pack()

# 1

def rgb(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

canvas.create_line(10,50,30,100,50,50,10,50)
canvas.create_oval(17,7,43,30,fill="red",outline="red")
canvas.create_oval(10,15,35,35,fill="yellow",outline="yellow")
canvas.create_oval(25,15,50,35,fill="green",outline="green")
canvas.create_rectangle(10,28,50,50,fill="white")

# 2
def tree (x,y):
    canvas.create_rectangle(x+110,y+100,x+140,y+200,fill="black")
    canvas.create_oval(x+90,y+50,x+160,y+120,fill="green",outline="green")
    canvas.create_oval(x+125,y+85,x+140,y+100,fill="red")
    canvas.create_oval(x+145,y+85,x+160,y+100,fill="red")
    canvas.create_line(x+133,y+85,x+143,y+70,x+153,y+85,width=2)
tree(10,10)

# 3
def balon(x,y):
    canvas.create_line(x+100,y+100,x+130,y+165,x+160,y+100)
    canvas.create_rectangle(x+115,y+165,x+145,y+175,fill="red")
    canvas.create_oval(x+96,y+50,x+164,y+115,fill="blue",outline="blue")
balon(10,200)

# 4
def kod(x,y):
    for i in range(1,20):
        x = x + 10
        nc = randrange(1,9)
        canvas.create_line(x+20,y+10,x+20,y+100,width=0+nc)
        print(nc,end = " , ")
print(end="\n") 
kod(100,500)

# 5
canvas.create_rectangle(700,10,1000,60,fill="cyan2",outline="cyan2")
canvas.create_oval(800,20,980,100,fill="yellow")
canvas.create_rectangle(700,60,1000,100,fill="green2",outline="green2")
canvas.create_line(700,60,1000,60,width=2)
canvas.create_rectangle(720,50,740,85,fill="brown")
canvas.create_oval(710,20,750,55,fill="green",outline="green")
canvas.create_oval(760,30,780,50,fill="black")
canvas.create_line(770,50,770,70,760,90,770,70,780,90,width=2)
canvas.create_line(755,55,785,55,width=2)

#6a
x = 1050
y = 10
for i in range(1,9):
    x = x + 30
    farba = rgb(randrange(100),randrange(150),randrange(200))
    canvas.create_oval(x,y,x+50,y+40,fill=farba)
    canvas.create_line(x+25,y+40,1195,100)
#6b
x = 1050
y = 50
for i in range(1,9):
    x = x + 30
    farba = rgb(randrange(100),randrange(150),randrange(200))
    canvas.create_oval(x,y+150,x+50,y+190,fill=farba)
    canvas.create_line(1195,150,x+25,y+150)

#7
x = 100
y = 400
nahodne_cislo = randrange(-100,100)
for i in range(1,101):
    nc = randrange(-100,100)
    x = x + 100 + nc
    y = y + 100 + nc
    nc = randrange(100)
    farba = rgb(randrange(100),randrange(150),randrange(200))
    velkost = randrange(1,6)
    canvas.create_line(x+ nc,y+ nc,x+ nc,y+ nc,fill=farba,width=1+velkost)

#8
def ostrov (x,y):
    nc = randrange(-20,20)
    canvas.create_rectangle(x+70,y-50,x+400,y+120,fill="white",outline="white")
    canvas.create_oval(x+100,y+100,x+200,y+150,fill="brown",outline="brown")
    canvas.create_rectangle(x+70,y+120,x+400,y+250,fill="blue",outline="blue")
    canvas.create_line(x+150,y,x+150,y+100,width=2)
    canvas.create_rectangle(x+150,y,x+230,y+50,fill="green2",width=2)
    canvas.create_oval(x+180,y+15,x+200,y+35,fill="yellow",outline="yellow")
    canvas.create_oval(x+188,y+15,x+210,y+35,fill="green2",outline="green2")
    canvas.create_line(x+230,y+130,x+290,y+130,x+320,y+100,x+200,y+100,x+230,y+130,width=2)
    canvas.create_line(x+260,y+100,x+260,y+30,x+280,y+70,x+260,y+90,width=2)
    canvas.create_oval(x+350,y+nc,x+380,y+50+nc,fill="yellow",outline="yellow")
    canvas.create_oval(x+362,y+nc,x+400,y+50+nc,outline="white",fill="white")
    canvas.create_oval(x+350,y+150+nc,x+380,y+200+nc,fill="yellow",outline="yellow")
    canvas.create_oval(x+362,y+150+nc,x+400,y+200+nc,outline="blue",fill="blue")
    
ostrov(400,400)

#9
x = 50
y = 400
for i in range(1,11):
    x = x + 4
    y = y + 10
    canvas.create_line(45,400,90,520)
    canvas.create_line(70,400,113,520)
    canvas.create_line(x-10,y+10,x+30,y+10)

#10
x = 200
y = 600
for i in range(1,31):
    x = x + 10
    canvas.create_line(200,700,x-150,y+50)

x = 400
y = 600
for i in range(1,31):
    x = x + 10
    canvas.create_line(400,600,x,y+100,fill="green2")


x = 650
y = 800
for i in range(1,31):
    x = x - 10
    canvas.create_line(650,800,x,y -100,fill="blue")

#11
x = 100
y = 900
for i in range(1,21):
    x = x + 50
    velkost = randrange(50,100)
    farba = rgb(randrange(100),randrange(200),randrange(200))
    canvas.create_oval(x,y,x+velkost,y+velkost,outline=farba,width=3)

#12
x = 1300
y = 300
for i in range(1,30):
    x = x + 10
    canvas.create_rectangle(1310,y,x+10,y+10)
    canvas.create_rectangle(1310,y+10,x+10,y+20)
    canvas.create_rectangle(1310,y+20,x+10,y+30)
    canvas.create_rectangle(1310,y+30,x+10,y+40)
    canvas.create_rectangle(1310,y+40,x+10,y+50)
    canvas.create_rectangle(1310,y+50,x+10,y+60)
    canvas.create_rectangle(1310,y+60,x+10,y+70)
    canvas.create_rectangle(1310,y+70,x+10,y+80)
    canvas.create_rectangle(1310,y+80,x+10,y+90)
    canvas.create_rectangle(1310,y+90,x+10,y+100)
    canvas.create_rectangle(1310,y+100,x+10,y+110)

# 14
x = 1400
y = 10
for i in range(1,401):
    velkost = randrange(20,70)
    x = x + 1
    canvas.create_line(x,y,x+1,y+velkost,fill="green")
    canvas.create_line(x,y+260,x+1,y+260-velkost,fill="green")

#19
def jazierko (x,y):
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(140,150)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    velkost = randrange(10,50)
    x = randrange(1450,1750)
    y = randrange(130,160)
    canvas.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,fill="blue",outline="blue")
    
jazierko(1400,110)

def mostik (x,y):
    for i in range(1,11):
        x = x + 40
        canvas.create_rectangle(x,y+130,x+40,y+170,outline="brown")

mostik(1360,10)


canvas.create_rectangle(300,105,800,340,fill="white")
canvas.create_rectangle(300,320,800,340,fill="green",outline="green")
x = 300
for i in range (1,101):
    x = x + 5
    canvas.create_line(x-5,320,x-5,310,fill="green")

canvas.create_oval(400,180,500,280,fill="red",outline="white")
canvas.create_rectangle(400,230,500,280,fill="white",outline="white")
canvas.create_rectangle(435,230,465,290,fill="brown",outline="brown")
canvas.create_oval(435,280,465,305,fill="brown",outline="brown")
canvas.create_oval(410,210,420,220,fill="white",outline="white")
canvas.create_oval(440,210,450,220,fill="white",outline="white")
canvas.create_oval(465,195,475,205,fill="white",outline="white")
canvas.create_oval(430,195,440,205,fill="white",outline="white")
x = 350
y = 113
for i in range (1,41):
    velkost = randrange(-50,40)
    x = x
    y = y + 2
    canvas.create_line(307,110,x + velkost ,y,fill="yellow",width=2)
x = 630
y = 180
z = 750
q = 300
for i in range(1,21):
    x = x + 3 
    y = y + 3
    z = z - 3
    q = q - 3
    canvas.create_oval(x,y,z,q,outline="blue")

x = 500
y = 110
for i in range(1,6):
    velkost = randrange(1,25)
    canvas.create_rectangle(x,y,x+velkost,y+velkost)
    velkost = randrange(1,25)
    canvas.create_rectangle(x,y+30,x+velkost,y+30+velkost)
    velkost = randrange(1,25)
    canvas.create_rectangle(x,y+60,x+velkost,y+60+velkost)
    x = x + 30
# 20 a 21
canvas.create_rectangle(1000,450,1600,750,fill="white")
def kvet (x,y):
    for i in range(1,31):
        canvas.create_line(x,y,x+ randrange(-50,50),y-randrange(10,40),fill="green",width=2)
        canvas.create_line(x,y,x,y-50,fill="green",width=5)
    for i in range(1,41):
        canvas.create_line(x,y-50,x+randrange(-40,40),y-50+randrange(-40,40),fill="yellow",width=2)


for i in range(randrange(3,15)):
    kvet(randrange(1000,1550),randrange(500,700))
        
def strom(x,y):
    canvas.create_rectangle(x,y,x+5,y-150,fill="brown",outline="brown")
    for i in range(1,3):
        canvas.create_line(x,y-randrange(0,30),x+randrange(-30,30),y-randrange(31,60),fill="brown",width=3)
    for i in range(1,3):
        canvas.create_line(x,y-randrange(31,60),x+randrange(-30,30),y-randrange(61,90),fill="brown",width=3)
    for i in range(1,3):
        canvas.create_line(x,y-randrange(61,90),x+randrange(-30,30),y-randrange(91,120),fill="brown",width=3)
    for i in range(1,3):
        canvas.create_line(x,y-randrange(91,120),x+randrange(-30,30),y-randrange(121,150),fill="brown",width=3)
    for i in range(1,3):
        canvas.create_line(x,y-randrange(121,150),x+randrange(-30,30),y-randrange(151,180),fill="brown",width=3)


for i in range(randrange(3,11)):
    strom(randrange(1030,1600),randrange(600,750))
