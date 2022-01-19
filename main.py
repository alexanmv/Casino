from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk
from random import randint
from random import shuffle
import random

class mainWindow():
    def __int__(self):
        self.root = Tk()
        self.root.geometry("1000x1000")
        self.root.title("Royal Gambling")

        self.C = Canvas(self.root, width=1000, height=1000)

        self.label = Label(self.root, text="WELCOME TO ROYAL GAMBLING!")
        self.label.place(anchor=NW)

        self.listbox = Listbox(self.root, bg="black", fg="red", height=10, width=17, font='Helvetica', activestyle='dotbox')

        self.listbox.insert(1, "Here you can play:")
        self.listbox.insert(2, "Black Jack")
        self.listbox.insert(3, "Tic Tac Toe")
        self.listbox.insert(4, "Highest Card")
        self.listbox.insert(5, "Dices")
        self.listbox.insert(6, "Find The Red Ball")
        self.listbox.place(relx=0, y=20, anchor=NW)

        self.b1 = Button(self.root, text="Black Jack", command=bjWindow)
        self.b1.place(x=160, y=20, anchor=NW)

        self.b2 = Button(self.root, text="Tic Tac Toe", command=TTTWindow)
        self.b2.place(x=250, y=20, anchor=NW)

        self.b4 = Button(self.root, text="Highest Card", command=HCWindow)
        self.b4.place(x=340, y=20, anchor=NW)

        self.b5 = Button(self.root, text="Dices", command=dicesWindow)
        self.b5.place(x=430, y=20, anchor=NW)

        self.b6 = Button(self.root, text="Find The Red Ball", command=FTRBWindow)
        self.b6.place(x=520, y=20, anchor=NW)

        self.image1 = Image.open("Live-Casino-Challenge.jpg")
        self.image1.resize((1000, 1000)).save('royalcasion.png')

        self.image2 = ImageTk.PhotoImage(Image.open("C:\\Users\\darth\\Desktop\\Tkinter\\royalcasion.png"))
        self.C.create_image(0, 0, anchor=NW, image=image2)
        self.C.pack()

        self.root.mainloop()

root = Tk()
root.geometry("1000x1000")
#dices window----------------------------------------------------------------------


def dicesWindow():
    root.destroy()
    root1 = Tk()
    root1.geometry("1000x1000")
    root1.title("DICES")
    d = Image.open("dices background.jpg")
    d.resize((1000,1000)).save("dices-backg.png")
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\darth\\Desktop\\Tkinter\\dices-backg.png"))
    d1 = Image.open("1.jpg")
    d1.resize((100,100)).save("d1.png")
    d2 = Image.open("dice 2.png")
    d2.resize((100, 100)).save("d2.png")
    d3 = Image.open("dice 3.png")
    d3.resize((100, 100)).save("d3.png")
    d4 = Image.open("dice 4.png")
    d4.resize((100, 100)).save("d4.png")
    d5 = Image.open("dice 5.png")
    d5.resize((100, 100)).save("d5.png")
    d6 = Image.open("dice 6.png")
    d6.resize((100, 100)).save("d6.png")
    image1 = ImageTk.PhotoImage(Image.open("d1.png"))
    image2 = ImageTk.PhotoImage(Image.open("d2.png"))
    image3 = ImageTk.PhotoImage(Image.open("d3.png"))
    image4 = ImageTk.PhotoImage(Image.open("d4.png"))
    image5 = ImageTk.PhotoImage(Image.open("d5.png"))
    image6 = ImageTk.PhotoImage(Image.open("d6.png"))
    label = Label(root1,image=image)
    label.pack()


    #total_var = tk.IntVar()
    #bet_var = tk.IntVar()



    #total_entry = tk.Entry(root, textvariable=total_var)
    #bet_entry = tk.Entry(root, textvariable=bet_var)
    #total_entry.place(x=750, y=500)
    #bet_entry.place(x=750, y=600)

    def startgame():
        dice1 = [1, 2, 3, 4, 5, 6]
        dice2 = [1, 2, 3, 4, 5, 6]
        x1 = randint(0, 5)
        y1 = randint(0, 5)
        x2 = randint(0, 5)
        y2 = randint(0, 5)
        def labeldice(x):
            global ld1, ld2, ld3, ld4, ld5, ld6
            if x == 1:
                ld1 = Label(root1,image = image1)
                return  ld1
            if x == 2:
                ld2 = Label(root1,image = image2)
                return ld2
            if x == 3:
                ld3 = Label(root1,image = image3)
                return ld3
            if x == 4:
                ld4 = Label(root1,image = image4)
                return ld4
            if x == 5:
                ld5 = Label(root1,image = image5)
                return ld5
            if x == 6:
                ld6 = Label(root1,image = image6)
                return ld6
        if dice1[x1] == dice1[y1] and dice2[x2] != dice2[y2]:
            global l1
            labeldice(dice1[x1]).place(x=400, y=300)
            labeldice(dice1[y1]).place(x=600, y=300)
            labeldice(dice2[x2]).place(x=400, y=600)
            labeldice(dice2[y2]).place(x=600, y=600)
            l1 = tk.Label(root1,text=(str(dice1[x1] * dice1[y1]), '-', str(dice2[x2] + dice2[y2])), font = ("Times", 20),  width = 6,bg="black",fg="red")
            l1.place(x=500, y=500)
        elif dice2[x2] == dice2[y2] and dice1[x1] != dice1[y1]:
            global l2
            labeldice(dice1[x1]).place(x=400, y=300)
            labeldice(dice1[y1]).place(x=600, y=300)
            labeldice(dice2[x2]).place(x=400, y=600)
            labeldice(dice2[y2]).place(x=600, y=600)
            l2 = tk.Label(root1,text=(str(dice1[x1] + dice1[y1]), '-', str(dice2[x2] * dice2[y2])),font = ("Times", 20),  width = 6,bg="black",fg="red")
            l2.place(x=500, y=500)
        elif dice1[x1] != dice1[y1] and dice2[x2] != dice2[y2]:
            global l3
            labeldice(dice1[x1]).place(x=400, y=300)
            labeldice(dice1[y1]).place(x=600, y=300)
            labeldice(dice2[x2]).place(x=400, y=600)
            labeldice(dice2[y2]).place(x=600, y=600)
            l3 = tk.Label(root1,text=(str(dice1[x1] + dice1[y1]), '-', str(dice2[x2] + dice2[y2])),font = ("Times", 20),  width = 6,bg="black",fg="red")
            l3.place(x=500, y=500)
        elif dice1[x1] == dice1[y1] and dice2[x2] == dice2[y2]:
            global l4
            labeldice(dice1[x1]).place(x=400, y=300)
            labeldice(dice1[y1]).place(x=600, y=300)
            labeldice(dice2[x2]).place(x=400, y=600)
            labeldice(dice2[y2]).place(x=600, y=600)
            l4 = tk.Label(root1,text= (str(dice1[x1] * dice1[y1]), '-', str(dice2[x2] * dice2[y2])),font = ("Times", 20),  width = 6,bg="black",fg="red")
            l4.place(x=500, y=500)
    b1 = tk.Button(root1, text="ROLL THE DICES",command=startgame, bg = "black", fg="red")
    b1.place(x=500, y=450)
    root1.mainloop()



#black jack window---------------------------------------------------------------

def bjWindow():
    root.destroy()
    root2 = Tk()
    root2.geometry("1300x1000")
    root2.title("BLACK JACK")
    d = Image.open("blackjack.jpg")
    d.resize((1300,1000)).save("bj1.png")
    image = ImageTk.PhotoImage(Image.open("bj1.png"))
    label = Label(root2, image=image)
    label.place(x=0,y=0)
    image1 = ImageTk.PhotoImage(Image.open("fd.png"))

    ch1 = Image.open("ace of hearts - Αντιγραφή.png")
    ch1.resize((150, 250)).save("ace.png")
    aceh = ImageTk.PhotoImage(Image.open("ace.png"))

    ch2 = Image.open("2.png")
    ch2.resize((150, 250)).save("c2.png")
    hcard2 = ImageTk.PhotoImage(Image.open("c2.png"))

    ch3 = Image.open("3.png")
    ch3.resize((150, 250)).save("c3.png")
    hcard3 = ImageTk.PhotoImage(Image.open("c3.png"))

    ch4 = Image.open("4 - Αντιγραφή.png")
    ch4.resize((150, 250)).save("c4.png")
    hcard4 = ImageTk.PhotoImage(Image.open("c4.png"))

    ch5 = Image.open("5.png")
    ch5.resize((150, 250)).save("c5.png")
    hcard5 = ImageTk.PhotoImage(Image.open("c5.png"))

    ch6 = Image.open("6.png")
    ch6.resize((150, 250)).save("c6.png")
    hcard6 = ImageTk.PhotoImage(Image.open("c6.png"))

    ch7 = Image.open("7.png")
    ch7.resize((150, 250)).save("c7.png")
    hcard7 = ImageTk.PhotoImage(Image.open("c7.png"))

    ch8 = Image.open("8 - Αντιγραφή.png")
    ch8.resize((150, 250)).save("c8.png")
    hcard8 = ImageTk.PhotoImage(Image.open("c8.png"))

    ch9 = Image.open("9.png")
    ch9.resize((150, 250)).save("c9.png")
    hcard9 = ImageTk.PhotoImage(Image.open("c9.png"))

    ch10 = Image.open("10.png")
    ch10.resize((150, 250)).save("c10.png")
    hcard10 = ImageTk.PhotoImage(Image.open("c10.png"))

    ch11 = Image.open("jack of hearts - Αντιγραφή.png")
    ch11.resize((150, 250)).save("cj.png")
    hcard11 = ImageTk.PhotoImage(Image.open("cj.png"))

    ch12 = Image.open("queen of hearts.png")
    ch12.resize((150, 250)).save("cq.png")
    hcard12 = ImageTk.PhotoImage(Image.open("cq.png"))

    ch13 = Image.open("king of hearts - Αντιγραφή.png")
    ch13.resize((150, 250)).save("ck.png")
    hcard13 = ImageTk.PhotoImage(Image.open("ck.png"))

    cd1 = Image.open("ace of diamonds.png")
    cd1.resize((150, 250)).save("cd1.png")
    dace = ImageTk.PhotoImage(Image.open("cd1.png"))

    cd2 = Image.open("two of diamonds.jpg")
    cd2.resize((150, 250)).save("cd2.png")
    dcard2 = ImageTk.PhotoImage(Image.open("cd2.png"))

    cd3 = Image.open("three of diamonds.png")
    cd3.resize((150, 250)).save("cd3.png")
    dcard3 = ImageTk.PhotoImage(Image.open("cd3.png"))

    cd4 = Image.open("four of diamonds.png")
    cd4.resize((150, 250)).save("cd4.png")
    dcard4 = ImageTk.PhotoImage(Image.open("cd4.png"))

    cd5 = Image.open("five of diamonds.png")
    cd5.resize((150, 250)).save("cd5.png")
    dcard5 = ImageTk.PhotoImage(Image.open("cd5.png"))

    cd6 = Image.open("six of diamonds.png")
    cd6.resize((150, 250)).save("cd6.png")
    dcard6 = ImageTk.PhotoImage(Image.open("cd6.png"))

    cd7 = Image.open("seven of diamonds.png")
    cd7.resize((150, 250)).save("cd7.png")
    dcard7 = ImageTk.PhotoImage(Image.open("cd7.png"))

    cd8 = Image.open("eight of diamonds.png")
    cd8.resize((150, 250)).save("cd8.png")
    dcard8 = ImageTk.PhotoImage(Image.open("cd8.png"))

    cd9 = Image.open("nine of cards.png")
    cd9.resize((150, 250)).save("cd9.png")
    dcard9 = ImageTk.PhotoImage(Image.open("cd9.png"))

    cd10 = Image.open("ten of diamonds.png")
    cd10.resize((150, 250)).save("cd10.png")
    dcard10 = ImageTk.PhotoImage(Image.open("cd10.png"))

    cd11 = Image.open("jack of diamonds.png")
    cd11.resize((150, 250)).save("cdj.png")
    dcard11 = ImageTk.PhotoImage(Image.open("cdj.png"))

    cd12 = Image.open("queen of diamonds.jpg")
    cd12.resize((150, 250)).save("cdq.png")
    dcard12 = ImageTk.PhotoImage(Image.open("cdq.png"))

    cd13 = Image.open("king of diamonds.png")
    cd13.resize((150, 250)).save("cdk.png")
    dcard13 = ImageTk.PhotoImage(Image.open("cdk.png"))

    cs1 = Image.open("ace of spades.png")
    cs1.resize((150, 250)).save("cs1.png")
    sace = ImageTk.PhotoImage(Image.open("cs1.png"))

    cs2 = Image.open("two of spades.png")
    cs2.resize((150, 250)).save("cs2.png")
    scard2 = ImageTk.PhotoImage(Image.open("cs2.png"))

    cs3 = Image.open("three of spades.png")
    cs3.resize((150, 250)).save("cs3.png")
    scard3 = ImageTk.PhotoImage(Image.open("cs3.png"))

    cs4 = Image.open("four of spades.png")
    cs4.resize((150, 250)).save("cs4.png")
    scard4 = ImageTk.PhotoImage(Image.open("cs4.png"))

    cs5 = Image.open("five of spades.png")
    cs5.resize((150, 250)).save("cs5.png")
    scard5 = ImageTk.PhotoImage(Image.open("cs5.png"))

    cs6 = Image.open("six of spades.png")
    cs6.resize((150, 250)).save("cs6.png")
    scard6 = ImageTk.PhotoImage(Image.open("cs6.png"))

    cs7 = Image.open("seven of spades.png")
    cs7.resize((150, 250)).save("cs7.png")
    scard7 = ImageTk.PhotoImage(Image.open("cs7.png"))

    cs8 = Image.open("eight of spades.png")
    cs8.resize((150, 250)).save("cs8.png")
    scard8 = ImageTk.PhotoImage(Image.open("cs8.png"))

    cs9 = Image.open("nine of spades.png")
    cs9.resize((150, 250)).save("cs9.png")
    scard9 = ImageTk.PhotoImage(Image.open("cs9.png"))

    cs10 = Image.open("ten of spades.png")
    cs10.resize((150, 250)).save("cs10.png")
    scard10 = ImageTk.PhotoImage(Image.open("cs10.png"))

    cs11 = Image.open("jack of spades.jpg")
    cs11.resize((150, 250)).save("csj.png")
    scard11 = ImageTk.PhotoImage(Image.open("csj.png"))

    cs12 = Image.open("queen of spades.jpg")
    cs12.resize((150, 250)).save("csq.png")
    scard12 = ImageTk.PhotoImage(Image.open("csq.png"))

    cs13 = Image.open("king of spades.png")
    cs13.resize((150, 250)).save("csk.png")
    scard13 = ImageTk.PhotoImage(Image.open("csk.png"))

    cc1 = Image.open("ace of clubs.png")
    cc1.resize((150, 250)).save("cc1.png")
    cace = ImageTk.PhotoImage(Image.open("cc1.png"))

    cc2 = Image.open("two of clubs.png")
    cc2.resize((150, 250)).save("cc2.png")
    ccard2 = ImageTk.PhotoImage(Image.open("cc2.png"))

    cc3 = Image.open("three of clubs.png")
    cc3.resize((150, 250)).save("cc3.png")
    ccard3 = ImageTk.PhotoImage(Image.open("cc3.png"))

    cc4 = Image.open("four of clubs.png")
    cc4.resize((150, 250)).save("cc4.png")
    ccard4 = ImageTk.PhotoImage(Image.open("cc4.png"))

    cc5 = Image.open("five of clubs.png")
    cc5.resize((150, 250)).save("cc5.png")
    ccard5 = ImageTk.PhotoImage(Image.open("cc5.png"))

    cc6 = Image.open("six of clubs.png")
    cc6.resize((150, 250)).save("cc6.png")
    ccard6 = ImageTk.PhotoImage(Image.open("cc6.png"))

    cc7 = Image.open("seven of clubs.png")
    cc7.resize((150, 250)).save("cc7.png")
    ccard7 = ImageTk.PhotoImage(Image.open("cc7.png"))

    cc8 = Image.open("eight of clubs.png")
    cc8.resize((150, 250)).save("cc8.png")
    ccard8 = ImageTk.PhotoImage(Image.open("cc8.png"))

    cc9 = Image.open("nine of clubs.png")
    cc9.resize((150, 250)).save("cc9.png")
    ccard9 = ImageTk.PhotoImage(Image.open("cc9.png"))

    cc10 = Image.open("ten of clubs.png")
    cc10.resize((150, 250)).save("cc10.png")
    ccard10 = ImageTk.PhotoImage(Image.open("cc10.png"))

    cc11 = Image.open("jack of clubs.png")
    cc11.resize((150, 250)).save("ccj.png")
    ccard11 = ImageTk.PhotoImage(Image.open("ccj.png"))

    cc12 = Image.open("queen of clubs.png")
    cc12.resize((150, 250)).save("ccq.png")
    ccard12 = ImageTk.PhotoImage(Image.open("ccq.png"))

    cc13 = Image.open("king of clubs.png")
    cc13.resize((150, 250)).save("cck.png")
    ccard13 = ImageTk.PhotoImage(Image.open("cck.png"))



    def new_game():
        l1 = Label(root2, image=image1)
        l1.place(x=0, y=0)
        l2 = Label(root2, image=image1)
        l2.place(x=10, y=0)
        l3 = Label(root2, image=image1)
        l3.place(x=20, y=0)
        l4 = Label(root2, image=image1)
        l4.place(x=30, y=0)
        l5 = Label(root2, image=image1)
        l5.place(x=40, y=0)
        l6 = Label(root2, image=image1)
        l6.place(x=50, y=0)
        l7 = Label(root2, image=image1)
        l7.place(x=60, y=0)
        b.destroy()

        deck = [aceh, hcard2, hcard3, hcard4, hcard5, hcard6, hcard7, hcard8, hcard9, hcard10, hcard11, hcard12,
                hcard13,
                dace, dcard2, dcard3, dcard4, dcard5, dcard6, dcard7, dcard8, dcard9, dcard10, dcard11, dcard12,
                dcard13,
                sace, scard2, scard3, scard4, scard5, scard6, scard7, scard8, scard9, scard10, scard11, scard12,
                scard13,
                cace, ccard2, ccard3, ccard4, ccard5, ccard6, ccard7, ccard8, ccard9, ccard10, ccard11, ccard12,
                ccard13]

        def points(image):
            if image == aceh or image == dace or image == sace or image == cace:
                return 11
            if image == hcard2 or image == dcard2 or image == scard2 or image == ccard2:
                return 2
            if image == hcard3 or image == dcard3 or image == scard3 or image == ccard3:
                return 3
            if image == hcard4 or image == dcard4 or image == scard4 or image == ccard4:
                return 4
            if image == hcard5 or image == dcard5 or image == scard5 or image == ccard5:
                return 5
            if image == hcard6 or image == dcard6 or image == scard6 or image == ccard6:
                return 6
            if image == hcard7 or image == dcard7 or image == scard7 or image == ccard7:
                return 7
            if image == hcard8 or image == dcard8 or image == scard8 or image == ccard8:
                return 8
            if image == hcard9 or image == dcard9 or image == scard9 or image == ccard9:
                return 9
            if image == hcard10 or image == dcard10 or image == scard10 or image == ccard10:
                return 10
            if image == hcard11 or image == dcard11 or image == scard11 or image == ccard11:
                return 10
            if image == hcard12 or image == dcard12 or image == scard12 or image == ccard12:
                return 10
            if image == hcard13 or image == dcard13 or image == scard13 or image == ccard13:
                return 10

        class HitClass():
            def __init__(self, xcoord, card):
                self.card = card
                self.xcoord = xcoord
                self.l = Label(root2, image=self.card)
                self.l.place(x=self.xcoord, y=700)

        class Points():
            p = []

        y = 51

        def share():
            bs.destroy()
            bh = Button(root2, text="HIT", command=hit)
            bh.place(x=0, y=270)
            shuffle(deck)
            x1 = randint(0, y)
            obj = HitClass(1130, deck[x1])
            objp = Points()
            objp.p.append(points(deck[x1]))
            deck.pop(x1)
            x2 = randint(0, y - 1)
            obj1 = HitClass(950, deck[x2])
            objp.p.append(points(deck[x2]))
            if sum(objp.p) == 21:
                lpw = tk.Label(root2, text="YOU WIN",font = ("Times", 20),  width = 10,bg="black",fg="red")
                lpw.place(x=650, y=500)
            deck.pop(x2)
            ldc = Label(root2, image=image1)
            ldc.place(x=1130, y=0)
            print(sum(objp.p))

        def hit():
            x4 = randint(0, y - 2)
            shuffle(deck)
            obj = HitClass(770, deck[x4])
            objp = Points()
            objp.p.append(points(deck[x4]))
            if sum(objp.p) == 21:
                l = tk.Label(root2, text="YOU WIN",font = ("Times", 20),  width = 10,bg="black",fg="red")
                l.place(x=750, y=500)
            elif sum(objp.p) > 21:
                l = tk.Label(root2, text="YOU LOSE",font = ("Times", 20),  width = 10,bg="black",fg="red")
                l.place(x=750, y=500)
            print(sum(objp.p))
            deck.pop(x4)
            bh.destroy()

            def hit2():
                x4 = randint(0, y - 3)
                shuffle(deck)
                obj = HitClass(590, deck[x4])
                objp.p.append(points(deck[x4]))
                if sum(objp.p) == 21:
                    l = tk.Label(root2, text="YOU WIN",font = ("Times", 20),  width = 10,bg="black",fg="red")
                    l.place(x=750, y=500)
                elif sum(objp.p) > 21:
                    l = tk.Label(root2, text="YOU LOSE",font = ("Times", 20),  width = 10,bg="black",fg="red")
                    l.place(x=750, y=500)
                print(sum(objp.p))
                deck.pop(x4)
                bh2.destroy()

                def hit3():
                    x4 = randint(0, y - 4)
                    shuffle(deck)
                    obj = HitClass(410, deck[x4])
                    objp.p.append(points(deck[x4]))
                    if sum(objp.p) == 21:
                        l = tk.Label(root2, text="YOU WIN",font = ("Times", 20),  width = 10,bg="black",fg="red")
                        l.place(x=750, y=500)
                    elif sum(objp.p) > 21:
                        l = tk.Label(root2, text="YOU LOSE",font = ("Times", 20),  width = 10,bg="black",fg="red")
                        l.place(x=750, y=500)
                    print(sum(objp.p))
                    deck.pop(x4)
                    bh3.destroy()

                    def hit4():
                        x4 = randint(0, y - 5)
                        shuffle(deck)
                        obj = HitClass(230, deck[x4])
                        objp.p.append(points(deck[x4]))
                        if sum(objp.p) == 21:
                            l = tk.Label(root2, text="YOU WIN",font = ("Times", 20),  width = 10,bg="black",fg="red")
                            l.place(x=750, y=500)
                        elif sum(objp.p) > 21:
                            l = tk.Label(root2, text="YOU LOSE",font = ("Times", 20),  width = 10,bg="black",fg="red")
                            l.place(x=750, y=500)
                        print(sum(objp.p))
                        deck.pop(x4)
                        bh4.destroy()

                        def hit5():
                            x4 = randint(0, y - 6)
                            shuffle(deck)
                            obj = HitClass(50, deck[x4])
                            objp.p.append(points(deck[x4]))
                            if sum(objp.p) == 21:
                                l = tk.Label(root2, text="YOU WIN",font = ("Times", 20),  width = 10,bg="black",fg="red")
                                l.place(x=750, y=500)
                            elif sum(objp.p) > 21:
                                l = tk.Label(root2, text="YOU LOSE",font = ("Times", 20),  width = 10,bg="black",fg="red")
                                l.place(x=750, y=500)
                            print(sum(objp.p))
                            deck.pop(x4)

                        bh5 = Button(root2, text="HIT", command=hit5)
                        bh5.place(x=0, y=270)

                    bh4 = Button(root2, text="HIT", command=hit4)
                    bh4.place(x=0, y=270)

                bh3 = Button(root2, text="HIT", command=hit3)
                bh3.place(x=0, y=270)

            bh2 = Button(root2, text="HIT", command=hit2)
            bh2.place(x=0, y=270)

        def stop():
            objp = Points()
            x = randint(0, y - 7)
            l = Label(root2, image=deck[x])
            l.place(x=1130, y=0)
            counterd = points(deck[x])
            deck.pop(x)
            n = 950
            list = [j for j in range(0, 43)]
            while counterd <= 17:
                x1 = random.choice(list)
                l1 = Label(root2, image=deck[x1])
                l1.place(x=n, y=0)
                counterd += points(deck[x1])
                n -= 180
                list.pop(x1)
            if counterd > 21:
                ll = tk.Label(root2, text="DEALER LOSE", font = ("Times", 20),  width = 15,bg="black",fg="red")
                ll.place(x=650, y=500)
            elif counterd == 21:
                lw = tk.Label(root2, text="DEALER WINS",font = ("Times", 20),  width = 15,bg="black",fg="red")
                lw.place(x=650, y=500)
            elif counterd > sum(objp.p) and counterd < 22:
                ld = tk.Label(root2, text="DEALER WINS", font = ("Times", 20),  width = 15,bg="black",fg="red")
                ld.place(x=650, y=500)
            elif counterd < sum(objp.p) and counterd < 22:
                lv = tk.Label(root2, text="DEALER LOSE", font = ("Times", 20),  width = 15,bg="black",fg="red")
                lv.place(x=650, y=500)
            elif counterd == sum(objp.p):
                ld2 = tk.Label(root2, text="DEALER WINS", font = ("Times", 20),  width = 15,bg="black",fg="red")
                ld2.place(x=650, y=500)



        bs = Button(root2, text="SHARE", command=share)
        bs.place(x=0, y=300)
        bh = Button(root2, text="HIT", command=hit)
        bh.place(x=0, y=270)
        bst = Button(root2, text="STOP", command=stop)
        bst.place(x=0, y=330)


    b = tk.Button(root2, text="new game", command=new_game)
    b.place(x=650, y=500)
    root2.mainloop()

#TIC TAC TOE WINDOW---------------------------------------------------------------

def TTTWindow():
    root.destroy()
    root3 = Tk()
    root3.geometry("1000x1000")
    root3.title("TIC TAC TOE")
    def shutdown():
        root3.destroy()
    d = Image.open("TTT.png")
    d.resize((1000,1000)).save("t1.png")
    image = ImageTk.PhotoImage(Image.open("t1.png"))
    label = Label(root3, image=image)
    label.pack()
    button = Button(root3, command=shutdown)
    button.pack()
    root3.mainloop()

#HIGHEST CARD WINDOW--------------------------------------------------------------

def HCWindow():
    root.destroy()
    root4 = Tk()
    root4.geometry("1000x1000")
    root4.title("HIGHEST CARD")
    d = Image.open("black.jpg")
    d.resize((1000,1000)).save("hcbackg.png")
    image = ImageTk.PhotoImage(Image.open("hcbackg.png"))
    label = Label(root4, image=image)
    label.pack()

    fd = Image.open("one card.jpg")
    fd.resize((150, 250)).save("fd.png")
    facedown = ImageTk.PhotoImage(Image.open("fd.png"))

    c1 = Image.open("ace of hearts - Αντιγραφή.png")
    c1.resize((150, 250)).save("ace.png")
    ace = ImageTk.PhotoImage(Image.open("ace.png"))

    c2 = Image.open("2.png")
    c2.resize((150, 250)).save("c2.png")
    card2 = ImageTk.PhotoImage(Image.open("c2.png"))

    c3 = Image.open("3.png")
    c3.resize((150, 250)).save("c3.png")
    card3 = ImageTk.PhotoImage(Image.open("c3.png"))

    c4 = Image.open("4 - Αντιγραφή.png")
    c4.resize((150, 250)).save("c4.png")
    card4 = ImageTk.PhotoImage(Image.open("c4.png"))

    c5 = Image.open("5.png")
    c5.resize((150, 250)).save("c5.png")
    card5 = ImageTk.PhotoImage(Image.open("c5.png"))

    c6 = Image.open("6.png")
    c6.resize((150, 250)).save("c6.png")
    card6 = ImageTk.PhotoImage(Image.open("c6.png"))

    c7 = Image.open("7.png")
    c7.resize((150, 250)).save("c7.png")
    card7 = ImageTk.PhotoImage(Image.open("c7.png"))

    c8 = Image.open("8 - Αντιγραφή.png")
    c8.resize((150, 250)).save("c8.png")
    card8 = ImageTk.PhotoImage(Image.open("c8.png"))

    c9 = Image.open("9.png")
    c9.resize((150, 250)).save("c9.png")
    card9 = ImageTk.PhotoImage(Image.open("c9.png"))

    c10 = Image.open("10.png")
    c10.resize((150, 250)).save("c10.png")
    card10 = ImageTk.PhotoImage(Image.open("c10.png"))

    c11 = Image.open("jack of hearts - Αντιγραφή.png")
    c11.resize((150, 250)).save("cj.png")
    card11 = ImageTk.PhotoImage(Image.open("cj.png"))

    c12 = Image.open("queen of hearts.png")
    c12.resize((150, 250)).save("cq.png")
    card12 = ImageTk.PhotoImage(Image.open("cq.png"))

    c13 = Image.open("king of hearts - Αντιγραφή.png")
    c13.resize((150, 250)).save("ck.png")
    card13 = ImageTk.PhotoImage(Image.open("ck.png"))

    tchips = Image.open("total chips.jpg")
    tchips.resize((70, 150)).save("tchips.png")
    tchips1 = ImageTk.PhotoImage(Image.open("tchips.png"))

    wchips = Image.open("winchips.jpg")
    wchips.resize((70, 150)).save("wchips.png")
    wchips1 = ImageTk.PhotoImage(Image.open("wchips.png"))

    lchips = Image.open("lose chips.png")
    lchips.resize((70, 150)).save("lchips.png")
    lchips1 = ImageTk.PhotoImage(Image.open("lchips.png"))

    manychips = Image.open("1000chips.jpg")
    manychips.resize((70, 150)).save("mchips.png")
    mchips1 = ImageTk.PhotoImage(Image.open("mchips.png"))

    pchips = Image.open("200chips.jpg")
    pchips.resize((70, 150)).save("pchips.png")
    pchips1 = ImageTk.PhotoImage(Image.open("pchips.png"))

    def showDeckOfCards():
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        #class chips():

            #def __init__(self, total, image):
                #self.image = image
                #self.total = total
                #self.l = Label(root4, image=self.image)
                #self.l.place(x=0, y=0)

            #def Win(self, bet):
                #self.total += bet
                #if self.total >= 1000:
                    #self.l = Label(root4, image=mchips1)
                    #self.l.place(x=0, y=850)
                #else:
                    #self.l = Label(root4, image=wchips1)
                    #self.l.place(x=0, y=850)

            #def Lose(self, bet):
               # self.total -= bet
                #if self.total <= 200:
                    #self.l = Label(root4, image=pchips1)
                    #self.l.place(x=1430, y=850)
                #else:
                    #self.l = Label(root4, image=lchips1)
                   # self.l.place(x=1430, y=850)

        #total_var = tk.IntVar()
        #bet_var = tk.IntVar()

        #class button():
            #def __init__(self):
                #self.b = tk.Button(root, text="sumbit", command=self.submit)
                #self.b.place(x=750, y=700)

            #def submit(self):
                #totals = total_var.get()
                #bets = bet_var.get()

                #total = int(totals)
                #bet = int(bets)

                #p = chips(total, tchips1)
                #p.Win(bet)
                #print(p.total)
                #self.b.destroy()
                #total_entry.destroy()
                #bet_entry.destroy()

        #total_entry = tk.Entry(root, textvariable=total_var)
        #bet_entry = tk.Entry(root, textvariable=bet_var)

        #total_entry.place(x=750, y=500)
        #bet_entry.place(x=750, y=600)

        #b = button()

        def showFaceDown1():
            lbl1 = Label(root4, image=facedown)
            lbl1.place(x=200, y=300)

        def showFaceDown2():
            lbl2 = Label(root4, image=facedown)
            lbl2.place(x=700, y=300)

        def showResult():
            x1 = randint(0, 12)
            x2 = randint(0, 12)
            player1 = deck[x1]
            player2 = deck[x2]
            listofcards = [card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13,ace]
            if player1 > player2:
                lblr1 = tk.Label(root4, text="PLAYER 1 WINS", bg="black", fg="red", width=20)
                lblr1.place(x=475, y=450)
                lblc1 = Label(root4, image=listofcards[player1 - 1])
                lblc1.place(x=200, y=300)
                lblc2 = Label(root4, image=listofcards[player2 - 1])
                lblc2.place(x=700, y=300)
            if player1 < player2:
                lblr2 = tk.Label(root4, text="PLAYER 2 WINS", bg="black", fg="red", width=20)
                lblr2.place(x=475, y=450)
                lblc3 = Label(root4, image=listofcards[player1 - 1])
                lblc3.place(x=200, y=300)
                lblc4 = Label(root4, image=listofcards[player2 - 1])
                lblc4.place(x=700, y=300)
            if player1 == player2:
                lblr3 = tk.Label(root4, text="IT'S A TIE", bg="black", fg="red", width=20)
                lblr3.place(x=475, y=450)
                lblc5 = Label(root4, image=listofcards[player1 - 1])
                lblc5.place(x=200, y=300)
                lblc6 = Label(root4, image=listofcards[player2 - 1])
                lblc6.place(x=700, y=300)

        b1 = tk.Button(root4, text="PLAYER 1", command=showFaceDown1, bg="black", fg="red")
        b1.place(x=200, y=600)
        b2 = tk.Button(root4, text="PLAYER 2", command=showFaceDown2, bg="black", fg="red")
        b2.place(x=700, y=600)
        bsr = tk.Button(root4, text="SHOW RESULT", command=showResult, bg="black", fg="red")
        bsr.place(x=475, y=300)

    bplay = tk.Button(root4, text="PLAY", command=showDeckOfCards, bg="black", fg="red")
    bplay.place(x=500, y=100)
    root4.mainloop()

#FIND THE RED BALL----------------------------------------------------------------

def FTRBWindow():

    root.destroy()
    root5 = Tk()
    root5.geometry("1000x1000")
    root5.title("FIND THE RED BALL")

    d = Image.open("solidgreen.jpg")
    d.resize((1000,1000)).save("sgreen.png")
    image = ImageTk.PhotoImage(Image.open("sgreen.png"))

    label = Label(root5, image=image)
    label.pack()

    rcups = Image.open("red-cup.jpg")
    rcups.resize((150, 200)).save("redcup.png")

    bcup = Image.open("blue-cup.jpg")
    bcup.resize((150, 200)).save("bcup.png")

    gcup = Image.open("green-cup.jpg")
    gcup.resize((150, 200)).save("gcup.png")

    rball = Image.open("red-ball.jpg")
    rball.resize((150,200)).save("redball.png")

    tchips = Image.open("total chips.jpg")
    tchips.resize((70, 150)).save("tchips.png")
    tchips1 = ImageTk.PhotoImage(Image.open("tchips.png"))

    wchips = Image.open("winchips.jpg")
    wchips.resize((70, 150)).save("wchips.png")
    wchips1 = ImageTk.PhotoImage(Image.open("wchips.png"))

    lchips = Image.open("lose chips.png")
    lchips.resize((70, 150)).save("lchips.png")
    lchips1 = ImageTk.PhotoImage(Image.open("lchips.png"))

    manychips = Image.open("1000chips.jpg")
    manychips.resize((70, 150)).save("mchips.png")
    mchips1 = ImageTk.PhotoImage(Image.open("mchips.png"))

    pchips = Image.open("200chips.jpg")
    pchips.resize((70, 150)).save("pchips.png")
    pchips1 = ImageTk.PhotoImage(Image.open("pchips.png"))

    image1 = ImageTk.PhotoImage(Image.open("redcup.png"))
    image2 = ImageTk.PhotoImage(Image.open("bcup.png"))
    image3 = ImageTk.PhotoImage(Image.open("gcup.png"))
    image4 = ImageTk.PhotoImage(Image.open("redball.png"))

    lbl1 = tk.Label(root5, image=image1,bd=0)
    lbl2 = tk.Label(root5, image=image2,bd=0)
    lbl3 = tk.Label(root5, image=image3,bd=0)
    lbl1.place(x=150, y=250)
    lbl2.place(x=450, y=250)
    lbl3.place(x=700, y=250)

    lblrb1 = tk.Label(root5, image=image4,bd=0)
    lblrb2 = tk.Label(root5, image=image4,bd=0)
    lblrb3 = tk.Label(root5, image=image4,bd=0)

    caps = [' ', 'red ball', ' ']

    #class chips():

        #def __init__(self, total, image):
            #self.image = image
            #self.total = total
            #self.l = Label(root5, image=self.image)
            #self.l.place(x=0, y=0)

        #def Win(self, bet):
            #self.total += bet
            #if self.total >= 1000:
                #self.l = Label(root5, image=mchips1)
                #self.l.place(x=0, y=850)
            #else:
                #self.l = Label(root5, image=wchips1)
                #self.l.place(x=0, y=850)

        #def Lose(self, bet):
            #self.total -= bet
            #if self.total <= 200:
                #self.l = Label(root5, image=pchips1)
                #self.l.place(x=1430, y=850)
           # else:
                #self.l = Label(root5, image=lchips1)
                #self.l.place(x=1430, y=850)

    #total_var = tk.IntVar()
    #bet_var = tk.IntVar()

    #class button():
        #def __init__(self):
            #self.b = tk.Button(root, text="sumbit", command=self.submit)
            #self.b.place(x=750, y=700)

        #def submit(self):
            #totals = total_var.get()
            #bets = bet_var.get()

            #total = int(totals)
            #bet = int(bets)

            #p = chips(total, tchips1)
            #p.Win(bet)
            #print(p.total)
            #self.b.destroy()
            #total_entry.destroy()
            #bet_entry.destroy()

    #total_entry = tk.Entry(root, textvariable=total_var)
    #bet_entry = tk.Entry(root, textvariable=bet_var)

    #total_entry.place(x=750, y=500)
    #bet_entry.place(x=750, y=600)

    #b = button()

    def shuffle_caps(mylist):
        shuffle(mylist)
        return mylist
    def movecups():
        global game_round
        game_round = shuffle_caps(caps)
        lbl1x = lbl1.winfo_x()
        lbl2x = lbl2.winfo_x()
        lbl3x = lbl3.winfo_x()
        lbl1.place(x=lbl2x, y=250)
        lbl2.place(x=lbl3x, y=250)
        lbl3.place(x=lbl1x, y=250)
        lblrb1.place_forget()
        lblrb2.place_forget()
        lblrb3.place_forget()
    def  guessisc1():
        x=0
        if game_round[x] == 'red ball':
            lw1 = tk.Label(root5, text="Correct guess! The ball was in cup 1",width=30,bg="orange",fg="blue",font=("Times",20))
            lw1.place(x=250, y=50)
            lblrb1.place(x=150, y=250)
        elif game_round[x] != 'red ball':
            ll1 = tk.Label(root5, text="Wrong guess! The ball is in cup" + " " + str(game_round.index('red ball')+1), width=30,bg="orange",fg="blue",font=("Times",20))
            ll1.place(x=250, y=50)
    def guessisc2():
        x=1
        if game_round[x] == 'red ball':
            lw2 = tk.Label(root5, text="Correct guess! The ball was in cup 2",width=30,bg="orange",fg="blue",font=("Times",20))
            lw2.place(x=250, y=50)
            lblrb1.place(x=450, y=250)
        elif game_round[x] != 'red ball':
            ll2 = tk.Label(root5, text="Wrong guess! The ball is in cup" +  " " + str(game_round.index('red ball')+1),width=30,bg="orange",fg="blue",font=("Times",20))
            ll2.place(x=250, y=50)
    def guessisc3():
        x=2
        if game_round[x] == 'red ball':
            lw3 = tk.Label(root5, text="Correct guess! The ball was in cup 3",width=30,bg="orange",fg="blue",font=("Times",20))
            lw3.place(x=250, y=50)
            lblrb1.place(x=700, y=250)
        elif game_round[x] != 'red ball':
            ll3 = tk.Label(root5, text="Wrong guess! The ball is in cup" +  " " + str(game_round.index('red ball')+1),width=30,bg="orange",fg="blue",font=("Times",20))
            ll3.place(x=250, y=50)

    bplay = tk.Button(root5, text="PLAY", command=movecups,bg="orange",fg="blue")
    bplay.place(x=450, y=100)

    b1 = tk.Button(root5, text="CUP 1", command=guessisc1,background="orange",fg="blue")
    b1.place(x=150, y=600)

    b2 = tk.Button(root5, text="CUP 2", command=guessisc2,bg="orange",fg="blue")
    b2.place(x=450, y=600)

    b3 = tk.Button(root5, text="CUP 3", command=guessisc3,bg="orange",fg="blue")
    b3.place(x=700, y=600)

    root5.mainloop()


#home page window-----------------------------------------------------------------



root.title("Royal Gambling")

C = Canvas(root, width=1000, height=1000)

label = Label(root, text="WELCOME TO ROYAL GAMBLING!")
label.place(anchor = NW)

listbox = Listbox(root, bg = "black", fg = "red", height=10, width=17, font = 'Helvetica', activestyle = 'dotbox')

listbox.insert(1, "Here you can play:")
listbox.insert(2, "Black Jack")
listbox.insert(3, "Tic Tac Toe")
listbox.insert(4, "Highest Card")
listbox.insert(5, "Dices")
listbox.insert(6, "Find The Red Ball")
listbox.place(relx=0, y=20, anchor = NW)

b1= Button(root, text="Black Jack",command=bjWindow)
b1.place(x = 160, y=20, anchor = NW )

b2= Button(root, text="Tic Tac Toe",command=TTTWindow)
b2.place(x = 250, y=20, anchor = NW )

b4= Button(root, text="Highest Card",command=HCWindow)
b4.place(x = 340, y=20, anchor = NW )

b5= Button(root, text="Dices", command=dicesWindow)
b5.place(x = 430, y=20, anchor = NW )

b6= Button(root, text="Find The Red Ball",command=FTRBWindow)
b6.place(x = 520, y=20, anchor = NW )

image1= Image.open("Live-Casino-Challenge.jpg")
image1.resize((1000,1000)).save('royalcasion.png')

image2 = ImageTk.PhotoImage(Image.open("C:\\Users\\darth\\Desktop\\Tkinter\\royalcasion.png"))
C.create_image(0,0,anchor=NW,image=image2)
C.pack()

root.mainloop()


p = mainWindow()