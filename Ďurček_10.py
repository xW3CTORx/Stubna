import tkinter
from random import *
import random
cn = tkinter.Canvas()
cn.pack()
cn.config(width = 1550, height = 750)

cno = cn.create_oval
cnt = cn.create_text

##x = 500
##y = 10
##
##x2 = 500
##y2 = 10
##
##x3 = 0
##y3 = 0
##
##x4 = 200
##y4 = 5
##chod = 1
##
##x5 = 300
##y5 = 5
##chod2 = 1
##
x6 = 10
y6 = 10
##
##xc1=0
##xc2=1500
##
chod_bin = 0
jednotky = 0
nuly = 0
##
########################################################## 1
##
##def lopta_vod():
##    global x
##    cn.delete('all')
##    
##    cno(x-5, y-5, x+5, y+5)
##    x = x+5
##    if x<1540:
##        cn.after(10, lopta_vod)
##
########################################################## 2

def lopta_hd():
    global y2
    cn.delete('lopta_hd')
    cno(x2-5, y2-5, x2+5, y2+5)
    
    y2=y2+5
    if y2==750:
        y2 = 0
        
    cn.after(10, lopta_hd)

####################################################### 3
##
##def lop_sik():
##    global x3
##    global y3
##    cn.delete('lopta_sik')
##    
##    cno(x3-5, y3-5, x3+5, y3+5)
##    x3 = x3+5
##    y3 = y3+5
##    if y3==750:
##        y3 = 0
##        x3 = 0
##    elif x3 ==1540:
##        x3 = 0
##
##    cn.after(10, lop_sik)
##
###################################################### 4
##
##def lop_s():
##    global y4
##    cn.delete('lop_s')
##    cno(x4-5, y4-5, x4+5, y4+5)
##    
##    y4 = y4+5
##    if y4>250:
##        y4 = 5
##    if chod == 1:
##        cn.after(10, lop_s)
##        
##def stop(suradnice):
##    global chod
##    chod = 0
##
#################################################### 5
##
##def lop_ss():
##    global y5
##    cn.delete('lop_ss')
##    cno(x5-5, y5-5, x5+5, y5+5)
##    y5 = y5+5
##    
##    if y5>250:
##        y5 = 5
##        
##    if chod2 == 1:
##        cn.after(10, lop_ss)
##        
##def ss(suradnice):
##    global chod2
##    if chod2 == 1:
##        chod2 = 0
##    else:
##        chod2 = 1
##        lop_ss()
##
##################################################### 7
##
##def crash():
##    global xc1,xc2
##    cn.delete('crash')
##    
##    xc1 = xc1 + random.randint(5,10)
##    xc2 = xc2 - random.randint(5,10)
##    
##    cno(xc1-15,190,xc1+15,220,fill='blue')
##    cno(xc2-15,190,xc2+15,220,fill='red')
##    
##    if xc1+5>=xc2-5:
##        cno(xc1-30, 170, xc1+30, 230, fill = 'white')
##        cnt(xc1,200,text='CRASH')
##    else:
##        cn.after(10,crash)
##
##
##lopta_vod()
##lopta_hd()
##lop_sik()
##lop_s()
##cn.bind('<Button-1>', stop)
##lop_ss()
##cn.bind('<Button-3>', ss)
##crash()

############################################### 6

def binary():
    global x6,y6,jednotky,nuly
    c=random.randint(0,1)
    
    if c==0:
        f='blue'
        jednotky += 1
    else:
        f='green'
        nuly += 1
    cnt(x6,y6,text = c, fill = f)
    x6 = x6+20
    
    if x6>200:
        x6 = 10
        y6 = y6+20
    if y6<100 and chod_bin==0:
        cn.after(10,binary)
    if y6>=100:
        print('nuly:',nuly)
        print('jednotky:',jednotky)
        
def p(cin):
    global chod_bin
    if chod_bin==1:
        chod_bin=0
        cn.after(10,binary)
    else:
        chod_bin=1
        

cnt(1400,730,text='P = pauza')
cn.bind_all('p',p)
binary()
