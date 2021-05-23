import tkinter
from random import *
cn = tkinter.Canvas()
cn.pack()
cn.config(width = 1550, height = 800)

cnr= cn.create_rectangle
cnl= cn.create_line
cno= cn.create_oval
cnt= cn.create_oval
ri= randint
rr= randrange

# 1

cno(100, 10, 200, 110, fill = "red")
cno(70, 50, 170, 150, fill = "yellow")
cno(130, 50, 230, 150, fill = "green")

cnr(70, 100, 230, 150, fill = "white")
cnl(70, 150, 150, 300)
cnl(150, 300, 230, 150)

# 2

cnr(300, 50, 330, 200, fill= "black")
