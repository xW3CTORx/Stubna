import tkinter
from random import *
cn = tkinter.Canvas()
cn.pack()
cn.config(width= 1360, height= 630)

######## pomocou nazvu objektu

##nadpis = cn.create_text(200,200,text='nadpis')
##obdlznik = cn.create_rectangle(100,100,150,200,fill='red')
##ciara = cn.create_line(50,50,200,150,width=5,fill='blue')
##oval = cn.create_oval(200,100,300,150,fill='green')
##
##def posun_vpravo(event):
##    cn.move(nadpis, 5, 0)
##    cn.move(obdlznik, 5, 0)
##    cn.move(ciara, 5, 0)
##    cn.move(oval, 5, 0)
##
##cn.bind_all('<Right>',posun_vpravo)

########## pomocou cisla objektu

##cn.create_text(200,200,text='nadpis')
##cn.create_rectangle(100,100,150,200,fill='red')
##cn.create_line(50,50,200,150,width=5,fill='blue')
##cn.create_oval(200,100,300,150,fill='green')
##
##def posun_vpravo(event):
##    for i in range(1,5):
##        cn.move(i,5,0)
##        
##cn.bind_all('<Right>',posun_vpravo)

####### ak presuvam vsetky objekty tak staci dat 'all'


############################################## vstky okrem jedneho dolava
##cn.create_text(200,200,text='nadpis')
##cn.create_rectangle(100,100,150,200,fill='red')
##cn.create_line(50,50,200,150,width=5,fill='blue')
##cn.create_oval(200,100,300,150,fill='green')
##
##def posun_vpravo(event):
##    cn.move('all',5,0)
##def posun_vlavo(event):
##    cn.move(randint(1,4),-5,0)
##    
##cn.bind_all('<Right>',posun_vpravo)
##cn.bind_all('<Left>', posun_vlavo)

#######################bike a auto

sirka=600

x_auto = 100
cn.create_rectangle(100,150,200,200,fill='blue',tags='auto')
cn.create_oval(115,200,140,225,fill='yellow',tags='auto')
cn.create_oval(160,200,185,225,fill='yellow',tags='auto')

x_bicykel = 200
cn.create_oval(200,100,230,130, fill='',width=5,outline='black',tags='bicykel')
cn.create_oval(250,100,280,130, fill='',width=5,outline='black',tags='bicykel')
cn.create_line(215,115,230,70, width=5,tags='bicykel')
cn.create_line(225,90,240,115,265,115,270,85, width=5,tags='bicykel')

def posuvaj():
    global x_auto, x_bicykel
    x_bicykel = x_bicykel-5
    cn.move('bicykel',-5,0)
    
    if x_bicykel<0:
        x_bicykel = x_bicykel + sirka
        cn.move('bicykel',sirka,0)

    x_auto = x_auto+5
    cn.move('auto',5,0)    
    if x_auto>sirka:
        x_auto = x_auto - sirka
        cn.move('auto',-sirka,0)
        
    print(x_auto, "   ", x_bicykel) #informácie si môžeme vypísať aj do shellu
    cn.after(100,posuvaj)
    
posuvaj()
