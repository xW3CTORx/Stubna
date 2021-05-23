import tkinter
canvas=tkinter.Canvas()
canvas.pack()
canvas.config(width=1500, height=800, bg="white")
#   LAVA
canvas.create_oval(10,10, 310,310); #ohranicenie
canvas.create_oval(15,15, 305,305, fill="red");     #cerveny kruh
canvas.create_oval(45,45, 275,275, fill="white");   #biely kruh
canvas.create_text(160,160, text="80", font="Arial 120 bold");      #80
canvas.create_rectangle(10,313, 310,460, width=5)       #stvorec pod
canvas.create_rectangle(155,463, 165,510, fill="grey",outline="grey" );     #tyc
canvas.create_text(160,388, text="22:00-06:00", font="Arial 30 bold");      #cas

#   PRAVA
canvas.create_oval(330,10, 630,310);    #ohranicenie
canvas.create_oval(335,15, 625,305, fill="red");        #cerveny kruh
canvas.create_oval(365,45, 595,275, fill="white");      #biely kruh
canvas.create_text(480,160, text="80", font="Arial 120 bold");      #80
canvas.create_rectangle(330,313, 630,460, width=5);     #stvorec pod
canvas.create_rectangle(475,463, 485,510, fill="grey", outline="grey" );    #tyc

#   OBLAK
canvas.create_oval(400,385, 430,415, fill="black");     #zlava1
canvas.create_oval(425,365, 495,435, fill="black");     #zlava2
canvas.create_oval(480,375, 540,430, fill="black");     #zlava3
canvas.create_oval(530,395, 560,420, fill="black");     #zlava4
canvas.create_rectangle(410,405, 560, 450, fill="black");       #cierna
canvas.create_rectangle(370,411, 560,450, fill="white", outline="white");   #biela
canvas.create_line(413,420, 409,425, width=3);      #kvapka1
canvas.create_line(423,420, 408,440, width=3);      #kvapka2
canvas.create_line(433,420, 429,425, width=3);      #kvapka3
canvas.create_line(443,420, 428,440, width=3);      #kvapka4
canvas.create_line(453,420, 449,425, width=3);      #kvapka5
canvas.create_line(463,420, 448,440, width=3);      #kvapka6
canvas.create_line(473,420, 469,425, width=3);      #kvapka7
canvas.create_line(483,420, 468,440, width=3);      #kvapka8
canvas.create_line(493,420, 489,425, width=3);      #kvapka9
canvas.create_line(503,420, 488,440, width=3);      #kvapka10
canvas.create_line(513,420, 509,425, width=3);      #kvapka11
canvas.create_line(523,420, 508,440, width=3);      #kvapka12
canvas.create_line(533,420, 529,425, width=3);      #kvapka13
canvas.create_line(543,420, 528,440, width=3);      #kvapka14

#   podpis
canvas.create_text(500,700, text="Ďurček, III.D", font="Arial 20 bold");
        
