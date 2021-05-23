import tkinter
import random
canvas=tkinter.Canvas()
canvas.pack()
canvas.config(height=800, width=1550)
#4.1_1
canvas.create_text(10,50, text=random.randint(1,49));
canvas.create_text(30,50, text=random.randint(1,49));
canvas.create_text(50,50, text=random.randint(1,49));
canvas.create_text(70,50, text=random.randint(1,49));
canvas.create_text(90,50, text=random.randint(1,49));
canvas.create_text(110,50, text=random.randint(1,49));

#4.2_2
#deklaracie premennych
d=random.randrange(150);
f=random.randrange(200);
velkost=random.randint(50,100);
farba=random.choice(("red", "blue", "green"));
ciara=random.choice(("grey", "purple"));
sirka=random.choice((2,3,5,8));

#stvrec
canvas.create_rectangle(d,f, d+velkost, f+velkost, fill=farba, outline=ciara, width=sirka);

#text
canvas.create_text(120,250, text="informácie o štvorci: ", font="Ariel 15 bold");

canvas.create_text(100,300, text="vyzrebovana suradnica x je: ", font="Ariel 10 bold");
canvas.create_text(100,350, text="vyzrebovana suradnica y je: ", font="Ariel 10 bold");

canvas.create_text(100,400, text="vyzrebovaná farba stvorca je: ", font="Ariel 10 bold" );
canvas.create_text(100,450, text="vyzrebovaná farba ciary je: ", font="Ariel 10 bold");
canvas.create_text(100,500, text="vyzrebovana sirka ciary je: ", font="Ariel 10 bold");

canvas.create_text(230,300, text=d, font="Ariel 10 bold");
canvas.create_text(230,350, text=f, font="Ariel 10 bold");
canvas.create_text(230,400, text=farba, font="Ariel 10 bold");
canvas.create_text(230,450, text=ciara, font="Ariel 10 bold");
canvas.create_text(230,500, text=sirka, font="Ariel 10 bold");

#4.2_3
vel=random.randrange(100);
a=random.randint(250, 450);
b=random.randint(10, 310);
hrubka=random.randint(2, 8);
canvas.create_line(a,b, a+vel,b+vel, width=hrubka);
a2=a+vel-a;
b2=b+vel-b;
c2=a2*2+b2*2;
dlzka=c2/2;
print("4.2_3 čiara->");
print("     hrúbka je: ", hrubka);
print("     dĺžka je:", dlzka);

#4.2_4
c=random.randint(250,450);
d=random.randint(410,550);
canvas.create_line(c,d, c+50,d);
print("4.2_4 vodorovná čiara->");
print("     súradnica x je: ", d);
print("     súradnica y je: ", c);
print("     dĺžka je 50 bodov");

#4.3_5
x=580;
y=100;

canvas.create_rectangle(x+10,y-50, x+50,y, fill="skyblue");             #hlava
canvas.create_rectangle(x,y, x+60,y+100, fill="skyblue");               #telo
canvas.create_rectangle(x+15,y-40, x+25,y-30, fill="yellow");           #prave oko
canvas.create_rectangle(x+35,y-40, x+45,y-30, fill="yellow");           #lave oko
canvas.create_rectangle(x+15,y-20, x+45,y-10, fill="red");              #usta
canvas.create_line(x,y+10, x-40,y+50, width=15);                        #prava ruka
canvas.create_line(x+60,y+10, x+100,y+50, width=15);                     #lava ruka
canvas.create_rectangle(x,y+100, x+20,y+180, fill="skyblue");           #prava noha
canvas.create_rectangle(x+40,y+100, x+60,y+180, fill="skyblue");      #lava noha

canvas.create_rectangle(x+5,y-40, x+10,y-20, fill="skyblue");           #prave ucho
canvas.create_rectangle(x+50,y-40, x+55,y-20, fill="skyblue");          #lave ucho
canvas.create_line(x+20,y-70, x+20,y-50);                               #antena prava
canvas.create_line(x+40,y-70, x+40,y-50);                               #antena lava
canvas.create_rectangle(x+10,y+30, x+50,y+60, fill="white");            #menovka
canvas.create_text(x+30,y+45, text="Robot");                            #meno

#4.3_6
q=600;
w=500;
rychlost=random.randint(10,130);
canvas.create_oval(q,w, q+100,w+100, fill="red");                   #vonkajsi kruh
canvas.create_oval(q+10,w+10, q+90,w+90, fill="white");                 #vnutrajsi kruh
canvas.create_text(q+50, w+50, text=rychlost, font="Arial 30 bold");
