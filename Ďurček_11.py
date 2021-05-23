import tkinter
from random import *
cn = tkinter.Canvas()
cn.pack()
cn.config(width = 1360, height = 600)

cnr = cn.create_rectangle
cnt = cn.create_text
cnl = cn.create_line

################################################### 1
def stvorcek(x, y, info):
    cnr(x-10, y-10, x+10, y+10)
    cnt(x, y, text=info)
    
def tlacidlo_klik():
    od = int(vstup1.get())
    do = int(vstup2.get())
    
    for i in range (od-1, do+1):
        stvorcek(i*20-od*20+10, 50, i)
def zmaz():
    cn.delete('all')
    
tlacidlo = tkinter.Button(text='Postupne cisla', command=tlacidlo_klik)
tlacidlo.pack()

zm = tkinter.Button(text='zmaz', command= zmaz)
zm.pack()

vstup1 = tkinter.Entry()
vstup1.pack()

vstup2 = tkinter.Entry()
vstup2.pack()

#################################################### 2 a 3

##def pis(suradnice):
##    x=suradnice.x
##    y=suradnice.y
##    pocet=int(entry1.get())
##    napis=entry2.get()
##    
##    farba = ["red", "green", "blue", "brown", "yellow", "pink", "black"]
##    vyber_f = entry3.get()
##
##    if vyber_f in farba:
##        for i in range(0,pocet):
##            cnt(x,y,text=' '+napis,
##            font='Arial 15',angle=i*360/pocet,tag=napis,
##            fill= vyber_f)
##    else:
##        cnt(100, 50, text="TAKU FARBU NEMAM")
##        
##def zmaz():
##    cn.delete('all')
##    
##button1=tkinter.Button(text='zmaž', command=zmaz)
##button1.pack()
##entry1=tkinter.Entry()
##entry1.pack()
##entry2=tkinter.Entry()
##entry2.pack()
##entry3 = tkinter.Entry()
##entry3.pack()
##
##cn.bind('<Button-1>',pis)
##cn.bind('<B1-Motion>', pis)

############################################### 4

##def znacka(suradnice):
##    x=suradnice.x
##    y=suradnice.y
##    nazov= entry1.get()
##    zk= entry2.get()
##
##    if zk=='z':
##        cnr(x-50, y-20, x+50, y+20)
##        cnt(x, y, text= nazov)
##        cnl(x, y+20, x, y+100, fill='grey')
##    elif zk=='k':
##        cnr(x-50, y-20, x+50, y+20)
##        cnt(x, y, text= nazov)
##        cnl(x, y+20, x, y+100, fill='grey')
##        cnl(x+50, y-20, x-50, y+20)
##
##def zmaz():
##    cn.delete('all')
##
##button = tkinter.Button(text= 'zmaz', command=zmaz)
##button.pack()
##
##entry1= tkinter.Entry()
##entry2= tkinter.Entry()
##entry1.pack()
##entry2.pack()
##
##cn.bind("<Button-1>", znacka)

##################################################### 5, 6

##def c(suradnice):
##    x=suradnice.x
##    y=suradnice.y
##    pocet=int(entry1.get())
##    space=int(entry2.get())
##    dlzka=int(entry3.get())
##    hd=0
##    
##    for i in range(0,pocet):
##        farba=choice(('blue1','blue2','blue3','blue4'))
##        cnl(x+i*space,y+hd - (dlzka/2),x+i*space,y+hd+(dlzka/2),fill=farba,width=3)
##        hd=hd+randint(-1,1)
##
##def zmaz():
##    cn.delete('all')
##    
##button1=tkinter.Button(text='zmaž', command=zmaz)
##button1.pack()
##entry1=tkinter.Entry()
##entry1.pack()
##entry2=tkinter.Entry()
##entry2.pack()
##entry3=tkinter.Entry()
##entry3.pack()
##cn.bind('<Button-1>',c)

