from tkinter import*
from random import*
from tkinter import messagebox
fen = Tk()
fen.title("jeu des petits chevaux")
can=Canvas(fen,width=800,height=600,background='white')
can.pack()

messagebox.showinfo("information", "appuyer sur ok et activez le jeu en appuyant sur lancer ou quitter en appuyent sur quitter",)

rect1=can.create_rectangle(5,5,210,210,fill="blue")
rect2=can.create_rectangle(350,5,555,210,fill="red")
rect3=can.create_rectangle(5,350,210,555,fill="green")
rect4=can.create_rectangle(350,350,555,555,fill="yellow")
rect5=can.create_rectangle(650,250,750,350,fill="black")

#partie rouge

oval1a=can.create_oval(310,5,345,25,fill="red")
rect1a2=can.create_rectangle(310,29,345,50,fill="red")
rect1a3=can.create_rectangle(310,60,345,81,fill="red")
rect1a4=can.create_rectangle(310,91,345,112,fill="red")
rect1a5=can.create_rectangle(310,122,345,143,fill="red")
rect1a6=can.create_rectangle(310,153,345,174,fill="red")
rect1a7=can.create_rectangle(310,184,345,205,fill="red")
rect1a8=can.create_rectangle(325,215,345,236,fill="red")
rect1b1=can.create_rectangle(355,215,376,246,fill="red")
rect1b2=can.create_rectangle(386,215,407,246,fill="red")
rect1b3=can.create_rectangle(417,215,438,246,fill="red")
rect1b4=can.create_rectangle(448,215,469,246,fill="red")
rect1b5=can.create_rectangle(479,215,500,246,fill="red")
rect1b6=can.create_rectangle(510,215,531,246,fill="red")
rect1b7=can.create_rectangle(540,215,557,246,fill="red")
rect1b8=can.create_rectangle(540,255,557,305,fill="red")

oval1a1=can.create_oval(540,310,557,345,fill="yellow")
rect2a1=can.create_rectangle(355,310,376,345,fill="yellow")
rect2a2=can.create_rectangle(386,310,407,345,fill="yellow")
rect2a3=can.create_rectangle(417,310,438,345,fill="yellow")
rect2a4=can.create_rectangle(448,310,469,345,fill="yellow")
rect2a5=can.create_rectangle(479,310,500,345,fill="yellow")
rect2a6=can.create_rectangle(510,310,531,345,fill="yellow")
rect2a7=can.create_rectangle(510,310,531,345,fill="yellow")
rect2b1=can.create_rectangle(314,537,345,555,fill="yellow")
rect2b2=can.create_rectangle(314,506,345,527,fill="yellow")
rect2b3=can.create_rectangle(314,475,345,496,fill="yellow")
rect2b4=can.create_rectangle(314,444,345,465,fill="yellow")
rect2b5=can.create_rectangle(314,413,345,434,fill="yellow")
rect2b6=can.create_rectangle(314,382,345,402,fill="yellow")
rect2b7=can.create_rectangle(314,351,345,372,fill="yellow")
rect2b8=can.create_rectangle(325,325,345,345,fill="yellow")


oval=can.create_oval(650,250,650,250)
oval1=can.create_oval(650,250,650,250)
oval2=can.create_oval(650,250,650,250)
oval3=can.create_oval(650,250,650,250)
oval4=can.create_oval(650,250,650,250)
oval5=can.create_oval(650,250,650,250)
oval6=can.create_oval(650,250,650,250)

#dés

def NouveauLance():
    global oval
    global oval1
    global oval2
    global oval3
    global oval4
    global oval5
    global oval6
    
    can.delete(oval1)
    can.delete(oval2)
    can.delete(oval3)
    can.delete(oval4)
    can.delete(oval5)
    can.delete(oval6)
    can.delete(oval)
    nb = randint(1,6)
    if nb == 1 :
        oval1=can.create_oval(690,290,710,310, fill="white")
    if nb == 2 :
        oval1=can.create_oval(670,270,690,290, fill="white")
        oval2=can.create_oval(710,310,730,330, fill="white")
    if nb == 3 :
        oval1=can.create_oval(690,290,710,310, fill="white")
        oval2=can.create_oval(670,270,690,290, fill="white")
        oval3=can.create_oval(710,310,730,330, fill="white")
    if nb == 4 :
        oval1=can.create_oval(670,270,690,290, fill="white")
        oval2=can.create_oval(710,310,730,330, fill="white")
        oval3=can.create_oval(670,310,690,330, fill="white")
        oval4=can.create_oval(710,270,730,290, fill="white")
    if nb == 5 :
        oval1=can.create_oval(690,290,710,310, fill="white")
        oval2=can.create_oval(670,270,690,290, fill="white")
        oval3=can.create_oval(710,310,730,330, fill="white")
        oval4=can.create_oval(670,310,690,330, fill="white")
        oval5=can.create_oval(710,270,730,290, fill="white")
    if nb == 6 :

        oval1=can.create_oval(670,265,690,285, fill="white")
        oval2=can.create_oval(710,315,730,335, fill="white")
        oval3=can.create_oval(670,315,690,335, fill="white")
        oval4=can.create_oval(710,265,730,285, fill="white")
        oval5=can.create_oval(670,290,690,310, fill="white")
        oval6=can.create_oval(710,290,730,310, fill="white")


# Création d'un widget Button (bouton Lancer)
BoutonLancer = Button(fen, text ='Lancer', command = NouveauLance)
# Positionnement du widget avec la méthode pack()
BoutonLancer.pack(side = RIGHT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(fen, text ='Quitter', command = fen.destroy)
BoutonQuitter.pack(side = RIGHT, padx = 5, pady = 5)

Texte = StringVar()
NouveauLance()

fen.mainloop()
