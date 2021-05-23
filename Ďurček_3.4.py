import tkinter
canvas=tkinter.Canvas()
canvas.pack()
canvas.config(height=800, width=1550, bg="grey90")

#15 a 16    elipsy
canvas.create_oval(100,50, 200,100, fill="purple", outline="green", width=3);
canvas.create_oval(205,50, 305,100, fill="red", outline="blue", width=5);

#17     vlajka jap
canvas.create_rectangle(10,150, 210,280, fill="white");
canvas.create_oval(75,180, 145,250, fill="red2", outline="red2");

#18     snehuliak
canvas.create_oval(300,150, 350,200, fill="white", outline="white");                     #hlava
canvas.create_oval(270,197, 380,307, fill="white", outline="white");    #trup   
canvas.create_oval(240,303, 410,473, fill="white", outline="white")     #spodok
canvas.create_oval(315,170, 315,170, fill="black", width=5);            #prave oko
canvas.create_oval(335,170, 335,170, fill="black", width=5);            #lave oko
canvas.create_oval(322,180, 322,180, fill="orange", width=10, outline="orange");        #nos
canvas.create_line(315,185, 335,184, width=10, fill="white");                           #nos2
canvas.create_oval(325,220, 325,220, width=5);              #gombik vrchny
canvas.create_oval(325,250, 325,250, width=5);              #gombik stred
canvas.create_oval(325,280, 325,280, width=5);              #gombik spodny
canvas.create_line(271,230, 250,300, fill="brown", width=5);        #ruka prava
canvas.create_line(379,230, 400,300, fill="brown", width=5);        #ruka lava

#19 20  tvár
canvas.create_oval(430,100, 530,200, fill="white");      
canvas.create_oval(460,130, 465,135);              
canvas.create_oval(495,130, 500,135);               
canvas.create_rectangle(475,140, 485,160);         
canvas.create_oval(460,170, 500,180);

canvas.create_oval(450,120, 475,145);
canvas.create_oval(485,120, 510,145);
canvas.create_line(429,133, 450,133);
canvas.create_line(510,133, 531,133);
canvas.create_line(475,133, 485,133);


#21 vlajka mesiac
canvas.create_rectangle(10,350, 210,480, fill="white");
canvas.create_oval(75,380, 145,450, fill="red", outline="red");
canvas.create_oval(95,380, 165,450, fill="white", outline="white");

#22 postavicka
canvas.create_oval(450,300, 550,400, fill="tan1");                  #tvár
canvas.create_rectangle(460,250, 540,310, fill="black");            #klobuk valec
canvas.create_oval(450,300, 550,320, fill="black");                 #klobuk spodok
canvas.create_oval(460,220, 540,272, fill="black");                 #klobuk vrch
canvas.create_line(480,340, 490,340, width=3);          #oko prave
canvas.create_line(530,340, 540,340, width=3);          #oko lave
canvas.create_line(500,380, 530,380, width=3);          #usta
canvas.create_rectangle(450,400, 550,520, fill="chartreuse2");  #telo

#podpis
canvas.create_text(600,600, text="Ďurček, III.D", font="Ariel 20 bold");
