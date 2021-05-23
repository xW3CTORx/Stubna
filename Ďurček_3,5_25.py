import tkinter
canvas=tkinter.Canvas()
canvas.pack()
canvas.config(width= 1500, height=900)

#    HOSPITAL
canvas.create_rectangle(30,70, 190,300, fill="blue4");      #stvorec
canvas.create_text(110,175, text="H", font="Arial 100 bold", fill="white");      #H
canvas.create_text(110,230, text="NEMOCNICA", font="Arial 10 bold", fill="white");      #nemocnica

#     POLICIA
canvas.create_rectangle(220,70, 370,300, fill="blue4");     #MODRY stvorec
canvas.create_rectangle(240,90, 350,230, fill="white");     #BIELY stvorec
canvas.create_text(295,160, text="POLÍCIA", font="Arial 15 bold");      #policia

#     80
canvas.create_oval(390,70, 620,300 );       #biely kruh vonkajsi
canvas.create_oval(395,75, 615,295, fill="red");    #cerveny kruh
canvas.create_oval(420,100, 590,270, fill="white");     #biely vnutorny kruh
canvas.create_text(505,185, text="80", font="Arial 70 bold");       #80

#    RESERVE
canvas.create_rectangle(650,70, 810,300, fill="blue4");     #stvorec
canvas.create_text(730,140, text="P", font="Arial 90 bold", fill="white");      #P
canvas.create_text(730,270, text="RÉSERVÉ", font="Arial 20 bold", fill="white");        #reserve

#      6t
canvas.create_oval(830,70, 1060,300, fill="red");       #cerveny kruh
canvas.create_oval(855,95, 1035,275, fill="white");     #biely kruh
canvas.create_text(945,185, text="6 t", font="Arial 70 bold");      #6t
    
#   podpis
canvas.create_text(500,500, text="Ďurček, III.D", font="Arial 20 bold");
