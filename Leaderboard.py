import tkinter
from tkinter import *
import tkinter.font as font
import os
def list_scoreboard():
    with open("ScoreBoard.txt", "r") as f:
        LeaderBoard = f.readlines()
        for i in range(len(LeaderBoard) - 1):
            val = list(LeaderBoard[i])
            val.pop()
            LeaderBoard[i] = "".join(val)
            if i % 2 == 1:
                LeaderBoard[i] = int(LeaderBoard[i])
                LeaderBoard[-1] = int(LeaderBoard[-1])
    return LeaderBoard



def true_edit_leaderboard(player):
    # This function permit to edit the ScoreBoard.txt file and add a new high score
    LeaderBoard = list_scoreboard()
    print("LeaderBoard = ", LeaderBoard)
    Scores = []
    for i in range(len(LeaderBoard)):
        if i % 2 == 1:
            Scores.append(LeaderBoard[i])
    i = 0
    print("Len scores = ", len(Scores))
    print("Scores bb", Scores)
    if player[1] < Scores[0]:
        LeaderBoard.insert(0, player[1])
        LeaderBoard.insert(0, player[0])
        print(1)
    elif player[1] > Scores[-1]:
        LeaderBoard.append(player[0])
        LeaderBoard.append(player[1])
        print(2)
    else:
        i = 0
        add = False
        while i < len(Scores):
            if player[1] > Scores[i]:
                i += 1
            else:
                LeaderBoard.insert(i * 2, player[1])
                LeaderBoard.insert(i * 2, player[0])
    print("final list = ", LeaderBoard)
    if len(LeaderBoard)>20:
        LeaderBoard.pop()
        LeaderBoard.pop()
    return LeaderBoard

def leaderboard_window():
    List=list_scoreboard()
    window = Tk()
    f = font.Font(size=25)
    window.title("GETTING OVER YOU")
    window.configure(background="Black")
    window.geometry("800x800")
    window.resizable(width=0, height=0)
    number=1

    Title=tkinter.Label(text="LeaderBoard:\r", bg="black",font = f, foreground='#FFFFFF',)
    Title.pack()
    Title=tkinter.Label(text="\r", bg="black",font = f, foreground='#FFFFFF',)
    Title.pack()
    for i in range(0,20,2):
        l = tkinter.Label(text=str(number)+"-  "+str(List[i])+" : "+str(List[i+1])+" sec", bg="black",font = f, foreground='#FFFFFF',)
        l.pack()
        number+=1


    quit = Button(window, text="Close", command=lambda: [window.destroy()])
    quit.config(width=15, height=2, relief='flat', bg='black', foreground='#FFFFFF', activeforeground='#ED1C24',
                activebackground="black", font=f)
    quit.pack(expand=TRUE, anchor='s')
    window.mainloop()




def true_edit_leaderboard(player):
    # This function permit to edit the ScoreBoard.txt file and add a new high score
    LeaderBoard = list_scoreboard()
    print("LeaderBoard = ", LeaderBoard)
    Scores = []
    for i in range(len(LeaderBoard)):
        if i % 2 == 1:
            Scores.append(LeaderBoard[i])
    i = 0
    print("Len scores = ", len(Scores))
    print("Scores bb", Scores)
    if player[1] < Scores[0]:
        LeaderBoard.insert(0, player[1])
        LeaderBoard.insert(0, player[0])
        print(1)
    elif player[1] > Scores[-1]:
        LeaderBoard.append(player[0])
        LeaderBoard.append(player[1])
        print(2)
    else:
        i = 0
        add = False
        while i < len(Scores):
            if player[1] > Scores[i]:
                i += 1
            else:
                LeaderBoard.insert(i * 2, player[1])
                LeaderBoard.insert(i * 2, player[0])
    print("final list = ", LeaderBoard)
    if len(LeaderBoard)>20:
        LeaderBoard.pop()
        LeaderBoard.pop()
    return LeaderBoard

def leaderboard_window():
    List=list_scoreboard()
    window = Tk()
    f = font.Font(size=25)
    window.title("GETTING OVER YOU")
    window.configure(background="Black")
    window.geometry("800x800")
    window.resizable(width=0, height=0)
    number=1

    Title=tkinter.Label(text="LeaderBoard:\r", bg="black",font = f, foreground='#FFFFFF',)
    Title.pack()
    Title=tkinter.Label(text="\r", bg="black",font = f, foreground='#FFFFFF',)
    Title.pack()
    for i in range(0,20,2):
        l = tkinter.Label(text=str(number)+"-  "+str(List[i])+" : "+str(List[i+1])+" sec", bg="black",font = f, foreground='#FFFFFF',)
        l.pack()
        number+=1


    quit = Button(window, text="Close", command=lambda: [window.destroy()])
    quit.config(width=15, height=2, relief='flat', bg='black', foreground='#FFFFFF', activeforeground='#ED1C24',
                activebackground="black", font=f)
    quit.pack(expand=TRUE, anchor='s')
    window.mainloop()

