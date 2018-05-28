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

#partie jaune

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
rect2b9=can.create_rectangle(258,537,308,555,fill="yellow")

#partie verte

oval1a1=can.create_oval(216,537,248,555,fill="green")
rect3a7=can.create_rectangle(215,327,236,345,fill="green")
rect3a6=can.create_rectangle(215,350,252,371,fill="green")
rect3a1=can.create_rectangle(215,527,252,506,fill="green")
rect3a2=can.create_rectangle(215,496,252,475,fill="green")
rect3a3=can.create_rectangle(215,465,252,444,fill="green")
rect3a4=can.create_rectangle(215,434,252,413,fill="green")
rect3a5=can.create_rectangle(215,402,252,382,fill="green")
rect3b1=can.create_rectangle(184,314,205,345,fill="green")
rect3b2=can.create_rectangle(153,314,174,345,fill="green")
rect3b3=can.create_rectangle(122,314,143,345,fill="green")
rect3b4=can.create_rectangle(91,314,112,345,fill="green")
rect3b5=can.create_rectangle(60,314,81,345,fill="green")
rect3b6=can.create_rectangle(29,314,50,345,fill="green")
rect3b7=can.create_rectangle(5,314,21,345,fill="green")
rect3b8=can.create_rectangle(5,251,21,310,fill="green")

#partie bleu

oval4a1=can.create_oval(5,215,21,246,fill="blue")
rect4a2=can.create_rectangle(31,215,52,246,fill="blue")
rect4a3=can.create_rectangle(62,215,83,246,fill="blue")
rect4a4=can.create_rectangle(93,215,114,246,fill="blue")
rect4a5=can.create_rectangle(124,215,145,246,fill="blue")
rect4a6=can.create_rectangle(155,215,176,246,fill="blue")
rect4a7=can.create_rectangle(186,215,207,246,fill="blue")
rect4b1=can.create_rectangle(217,215,238,235,fill="blue")
rect4b2=can.create_rectangle(217,184,252,205,fill="blue")
rect4b3=can.create_rectangle(217,153,252,174,fill="blue")
rect4b4=can.create_rectangle(217,122,252,143,fill="blue")
rect4b5=can.create_rectangle(217,91,252,112,fill="blue")
rect4b6=can.create_rectangle(217,60,252,81,fill="blue")
rect4b7=can.create_rectangle(217,29,252,50,fill="blue")
rect4b8=can.create_rectangle(217,5,252,21,fill="blue")
rect4b9=can.create_rectangle(258,5,305,21,fill="blue")

#centre rouge

rectc1r=can.create_rectangle(258,29,305,50,fill="darkred")
rectc2r=can.create_rectangle(258,60,305,81,fill="darkred")
rectc3r=can.create_rectangle(258,91,305,112,fill="darkred")
rectc4r=can.create_rectangle(258,122,305,143,fill="darkred")
rectc5r=can.create_rectangle(258,153,305,174,fill="darkred")
rectc6r=can.create_rectangle(258,184,305,205,fill="darkred")


#centre jaune

rectc1j=can.create_rectangle(509,255,530,305,fill="yellow")
rectc2j=can.create_rectangle(479,255,500,305,fill="yellow")
rectc3j=can.create_rectangle(448,255,469,305,fill="yellow")
rectc4j=can.create_rectangle(417,255,438,305,fill="yellow")
rectc5j=can.create_rectangle(386,255,407,305,fill="yellow")
rectc6j=can.create_rectangle(355,255,376,305,fill="yellow")

#centre vert

rectc1v=can.create_rectangle(258,506,308,527,fill="green")
rectc2v=can.create_rectangle(258,475,308,496,fill="green")
rectc3v=can.create_rectangle(258,444,308,465,fill="green")
rectc4v=can.create_rectangle(258,413,308,434,fill="green")
rectc5v=can.create_rectangle(258,382,308,403,fill="green")
rectc6v=can.create_rectangle(258,351,308,372,fill="green")

#centre bleu

rectc1b=can.create_rectangle(31,251,52,310,fill="blue")
rectc2b=can.create_rectangle(62,251,83,310,fill="blue")
rectc3b=can.create_rectangle(93,251,114,310,fill="blue")
rectc4b=can.create_rectangle(124,251,145,310,fill="blue")
rectc5b=can.create_rectangle(155,251,176,310,fill="blue")
rectc6b=can.create_rectangle(186,251,207,310,fill="blue")





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
