import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()
canvas.config(height=800, width=1550)

#1
y=0
for i in range(1,11):
    y=y+10
    canvas.create_line(10,y,150,y)
y=0
x=160
for i in range(1,6):
    y=y+10
    x=x+10
    canvas.create_line(x,y,300,y)
y=0
y2=0
for i in range(1,6):
    y=y+10
    y2=y2+20
    canvas.create_line(310,y,450,y2)

#2    
x=0
for i in range(1,11):
    x=x+10
    canvas.create_line(x,110,x,240)

x=120
y=110
for i in range(1,6):
    x=x+10
    y=y+20
    canvas.create_line(x,y,x,240)

x=180
y=110
for i in range(1,6):
    x=x+10
    y=y+15
    y2=y+70
    canvas.create_line(x,y,x,y2)
    
#3
x=0
for i in range(1,11):
    x=x+20
    canvas.create_rectangle(x,260,x+15,270)
    """
    ak v riadku x=0 zadame ine cislo tak sa obrazok posunie bud doprava alebo dolava
    ak zadame v riadku x=x+20 ine cislo tak budu vacsie medzery
    ak zadame namiesto 15 ine cislo tak sa mozu obdlzniky bud pretiahnut alebo zuzit
    """

#4
x=0
y=280
for i in range(1,11):
    x=x+20
    canvas.create_rectangle(x,y,x+15,y+10)

#5
y = 300
x = 10
for i in range(10, 16):
    y = y + 20
    canvas.create_rectangle(x, y, x+100, y+10)
#6
x=150
y=200
for i in range(10, 13):
    x= x + 150
    #trup
    canvas.create_rectangle(x, y, x+60, y+100, fill='grey')
    #meno
    canvas.create_text(x+30,y+50, text="Viktor")
    #hlava
    canvas.create_rectangle(x+10, y-50, x+50, y, fill='grey')
    #anteny
    canvas.create_line(x+20,y-50,x+20,y-80)
    canvas.create_line(x+40,y-50,x+40,y-80)
    #usi
    canvas.create_rectangle(x+5, y-35, x+10, y-15, fill='blue')
    canvas.create_rectangle(x+50, y-35, x+55, y-15, fill='blue')
    #oci
    canvas.create_rectangle(x+15, y-40, x+25, y-30, fill='gold')
    canvas.create_rectangle(x+35, y-40, x+45, y-30, fill='gold')
    #usta
    canvas.create_rectangle(x+15, y-20, x+45, y-10, fill='red')
    #nohy
    canvas.create_rectangle(x, y+100, x+20, y+180, fill='grey')
    canvas.create_rectangle(x+40, y+100, x+60, y+180, fill='grey')
    #ruky
    canvas.create_line(x, y+10, x-40, y+50, width=15)
    canvas.create_line(x+60, y+10, x+110, y+50, width=15)

#7
##########################################################################################

uhol = 0
x = 550
y = 75
for i in range(1, 7):
    canvas.create_text(x, y, text="                 Python", angle=uhol)
    uhol += 60

#8
##########################################################################################

#9
x=0
y=450
for i in range(1,6):
    y = y + 50
    x = x + 50
    canvas.create_line(x, y, x+50, y)
    canvas.create_line(x+50, y, x+50, y+50)
x=650
y=450
for i in range(1,6):
    y = y + 50
    x = x - 50
    canvas.create_line(x, y, x-50, y)
    canvas.create_line(x-50, y, x-50, y+50)

#10
p=20
for i in range(1,11):
    p=p+2
    print("Párne",p)
n=19
for i in range(1,11):
    n=n+2
    print("Nepárne",n)

#11
na=1
for i in range(0,9):
    na=na*2
    print("Násobky",na)
o=4
for i in range(0,7):
    o=o-1
    print("Odpocitavnie",o)

#12
x=1000
y=10
for i in range(1,26):
    x=x+20
    y=y+20
    canvas.create_line(x+10,10,1510,y, width=2)
    canvas.create_line(x,510,1010,y, width=2)

x=1000
y=10
for i in range(1,26):
    x=x-20
    y=y+20
    canvas.create_line(x+510,510,1510,y, width=2)
    canvas.create_line(x+10+510,10,1010,y, width=2)

#13
y = 550
x = 600
for i in range(1,11):
    x = x+10
    canvas.create_line(x, y, x+10, y+20)
    canvas.create_line(x, y+20, x+10, y)
y = 580
x = 590
for i in range(1,11):
    x = x+20
    canvas.create_line(x, y, x+10, y+20)
    canvas.create_line(x, y+20, x+10, y)

#14
yj = 650
xj = 550
for i in range(1,7):
    xj=xj+80
    canvas.create_line(xj, yj, xj+20, yj-20)
    canvas.create_line(xj+20, yj-20, xj+40, yj)
    canvas.create_line(xj, yj-5, xj+10, yj+5)
    canvas.create_line(xj+10, yj+5, xj+20, yj-5)
    canvas.create_line(xj+20, yj-5, xj+30, yj+5)
    canvas.create_line(xj+30, yj+5, xj+40, yj-5)
yj = 650
xj = 550    
for i in range(1,7):
    xj=xj+80
    canvas.create_line(xj+45, yj-10, xj+55, yj-20)
    canvas.create_line(xj+55, yj-20, xj+65, yj-10)
    canvas.create_line(xj+65, yj-10, xj+75, yj-20)
    canvas.create_line(xj+75, yj-20, xj+85, yj-10)
    canvas.create_line(xj+45, yj-10, xj+65, yj+10)
    canvas.create_line(xj+65, yj+10, xj+85, yj-10)

#odkaz
canvas.create_text(1400,750, text="nedaval som tam ten cas lebo by to dlho trvalo")
canvas.create_text(1400,700, font="Ariel 30 bold", text="Ďurček, III.D")
