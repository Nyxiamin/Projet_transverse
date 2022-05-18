from tkinter import *
import tkinter.font as font
import os
from Leaderboard import *
from functions import gameplay

def menu():
    """This function is menu page of the game where you can choose between Play, See the Leaderboard and close the game"""
    # -------------------------------------------------------------------------------
    #                                    Window
    # -------------------------------------------------------------------------------
    Fenetre = Tk()
    Fenetre.title("GETTING OVER YOU")
    """Fenetre.iconbitmap(os.path.join("assets", 'logo R (1).ico'))"""
    Fenetre.configure(background="Black")
    Fenetre.resizable(width=0, height=0)

    # -------------------------------------------------------------------------------
    #                              Image Game 1 (gauche)
    # -------------------------------------------------------------------------------
    gauche = PhotoImage(file=os.path.join("assets", "Hammer.png"))
    labnom = Label(Fenetre, image=gauche)
    labnom.config(borderwidth=0)
    labnom.pack(side=LEFT)

    # -------------------------------------------------------------------------------
    #                              Image Game 2 (droite)
    # -------------------------------------------------------------------------------
    droite = PhotoImage(file=os.path.join("assets", "Hammer.png"))
    labnom = Label(Fenetre, image=droite)
    labnom.config(borderwidth=0)
    labnom.pack(side=RIGHT)

    # -------------------------------------------------------------------------------
    #                              Title of the game (nord)
    # -------------------------------------------------------------------------------
    baniere = PhotoImage(file=os.path.join("assets", "Baniere-nom.png"))
    labnom = Label(Fenetre, image=baniere)
    labnom.config(borderwidth=0)
    labnom.pack(anchor='center')

    # -------------------------------------------------------------------------------
    #                            Play Button (center)
    # -------------------------------------------------------------------------------
    f = font.Font(size=25)
    play = Button(
        Fenetre, text="Jouer",
        command=lambda: [Fenetre.destroy(),gameplay()])
    play.config(width=15,
                height=2,
                relief='flat',
                bg='black',
                foreground='#FFFFFF',
                activeforeground='#ED1C24',
                activebackground="black",
                font=f)
    play.pack(expand=TRUE, anchor='center')

    # -------------------------------------------------------------------------------
    #                            LeaderBoard Button (sud)
    # -------------------------------------------------------------------------------
    Lead = Button(Fenetre,
                  text="LeaderBoard",
                  command=lambda: [
                                   leaderboard_window()])
    Lead.config(width=15,
                height=2,
                relief='flat',
                bg='black',
                foreground='#FFFFFF',
                activeforeground='#ED1C24',
                activebackground="black",
                font=f)
    Lead.pack(expand=TRUE, anchor='s')
    # -------------------------------------------------------------------------------
    #                            Close Window Button (sud)
    # -------------------------------------------------------------------------------
    quit = Button(Fenetre, text="Fermer", command=lambda: [Fenetre.destroy()])
    quit.config(width=15,
                height=2,
                relief='flat',
                bg='black',
                foreground='#FFFFFF',
                activeforeground='#ED1C24',
                activebackground="black",
                font=f)
    quit.pack(expand=TRUE, anchor='s')
    Fenetre.mainloop()

