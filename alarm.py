from tkinter import *
import pygame
import datetime
import time
import os
from PIL import Image, ImageTk
from playsound import playsound
#____________________________________________________________________________________________________
root=Tk()
def stop():
    os._exit(0)
def timenow():
    return datetime.datetime.now()
def settime():
    samay=timenow()
    s=str(samay)
    hour=(s[11:13])
    minute=(s[14:16])
    second=(s[17:19])
    return hour , minute , second

#___________________________________________________________________________________________________
def ring_alarm(h,m,s):#pygame hybridized in tkinter to use .mixer method of pygame to play the music
    status=0
    alm='off'
    pygame.init()
    clock=pygame.time.Clock()
#__________________________________________________________________________________________________
    while True:   #This loop is for checking time, this loop will not ring the alarm
        clock.tick(27)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        x,y,z =settime()
        g =timenow()
        print(g)
        time.sleep(1)
        p=h[:]+m[:]+s[:]
        for i in p:  #checking for wrong input(only digit)
            if(not i.isdigit()):
                status="break"
                break
        else:  #after verifying input.
            if(x==h and y==m and z==s) :
                alm="on"
                print("Wake Up! ")
                break
        if alm=="on":
            break
        if(status=="break"):
            print("Invalid Input")
            break
    if status=='break':return
#______________________________________________________________________________________________________
                                         #Not calling .init() each time may cause an error
    win=pygame.display.set_mode((400,200))
    pygame.display.set_caption("WAKE UP LAZY_")
    pygame.mixer.music.load("alarm.mp3")
    font=pygame.font.SysFont("Algerian",30)
    pygame.mixer.music.play(-1)
    clock=pygame.time.Clock()
#______________________________________________________________________________________________________
    if alm=='on':
        while True: #This loop is for ringing alarm
            clock.tick(27)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.type==pygame.QUIT:run=False
            win.blit(font.render("Press space to stop:",1,(0,255,0)),(10,10))
            ke=pygame.key.get_pressed()
            if ke[pygame.K_SPACE]:
                print("Alarm Switched off")
                break
            pygame.display.update()
        pygame.quit()
#______________________________________________________________________________________________________
    
def alarm():
    status=0
    alm="off"
    h=(hourvalue.get())
    m=(minutevalue.get())
    s=(secondvalue.get())
    ring_alarm(h,m,s)
#______________________________________________________________________________________________________
standard = "comicsansms 45 bold"
root.title("Alarm Clock ")
root.geometry("700x750")
p1=Image.open("images 4.jpeg")
p2=ImageTk.PhotoImage(p1)
l10=Label(image=p2)
l10.grid()

pic=PhotoImage(file="alarm_frame.png")
l0=Label(root , image=pic)
l0.grid()
l0.place(x=220, y=150)

f1=Frame(root)
f1.grid(row=0 , column=1)
#b2=Button(text="Stop" , command = stop , relief=GROOVE)
#b2.grid()
#b2.place(x=400 , y=500)
f1.place(x=350 , y=250)
l1=Label(text="Alarm Clock" , font=standard , bg="yellow" , fg="black")
l1.grid()
l1.place(x=260, y=50)
l8=Label(text="Enter Time in 24 Hours Format" , bg="black" , fg="white" , font ="Algerian 20 bold")
l8.grid()
l8.place(x=10 , y=140)
l2=Label(text="Hours" , font="comicsansms 20 bold" ,bg="green", fg="black")
l2.grid(row=1 , column=0)
l2.place(x=300 , y=250)
l3=Label(text ="Minutes" , font="comicsansms 20 bold" ,bg="green",  fg="black")
l3.grid(row=2 ,column=0)
l3.place(x=300 , y=300)
l4=Label( text = "Seconds" , font="comicsansms 20 bold"  , bg="green" ,fg="black" )
l4.grid(row=3, column=0)
l4.place(x=300 , y=350)
hourvalue=StringVar()
minutevalue=StringVar()
secondvalue=StringVar()
e1=Entry(textvariable=hourvalue,bg='light blue')
e1.grid(row=1 ,column=1)
e1.place(x=450 , y=260)
e2=Entry( textvariable=minutevalue,bg='light blue')
e2.grid(row=2 ,column=1)
e2.place(x=450 , y=310)
e3=Entry(textvariable=secondvalue,bg='light blue')
e3.grid(row=3 , column=1)
e3.place(x=450 , y=360)
b1=Button(text="Set Alarm" ,command=alarm, relief=GROOVE)
b1.grid()
b1.place(x=500 , y=500)
ln=Label(text = "Made by SHUBHAM SINGH" , bg="black" , fg="white" , font="Algerian 20 bold" )
ln.grid()
ln.place(x=260 , y=650)
l5=Label(text=" CSE 1904220100103 " , bg="black" , fg="white" , font="Algerian 20 bold")
l5.grid()
l5.place(x=260 , y=690)

root.mainloop()
