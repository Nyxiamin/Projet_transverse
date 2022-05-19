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
    Scores = []
    for i in range(len(LeaderBoard)):
        if i % 2 == 1:
            Scores.append(LeaderBoard[i])
    i = 0
    if player[1] < Scores[0]:
        LeaderBoard.insert(0, player[1])
        LeaderBoard.insert(0, player[0])
    elif player[1] > Scores[-1]:
        LeaderBoard.append(player[0])
        LeaderBoard.append(player[1])
    else:
        i = 1
        end=0
        while i < len(Scores) and end!=1:
            if player[1] > Scores[i]:
                i += 1
            else:
                LeaderBoard.insert(i+1, player[1])
                LeaderBoard.insert(i+1, player[0])
                end = 1
    if len(LeaderBoard)>20:
        LeaderBoard.pop(0)
        LeaderBoard.pop(0)
    with open("ScoreBoard.txt","w") as txt:
        for x in range(len(LeaderBoard)):
            txt.write(str(LeaderBoard[x]))
            txt.write("\n")


def leaderboard_window():
    List=list_scoreboard()
    window = Tk()
    f = font.Font(size=25)
    window.title("GETTING OVER YOU")
    window.configure(background="Black")
    window.geometry("800x500")
    window.resizable()
    number=1

    Title=Label(window, text="LeaderBoard:\r", bg="black",font = f, foreground='#FFFFFF',)
    Title.pack()
    Title=Label(window, text="\r", bg="black",font = f, foreground='#FFFFFF',)
    Title.pack()
    for i in range(0,20,2):
        line = Label(window, text=str(number)+"-  "+str(List[i])+" : "+str(List[i+1])+" sec", bg="black",font = f, foreground='#FFFFFF',)
        line.pack()
        number+=1


    quit = Button(window, text="Close", command=lambda: [window.destroy()])
    quit.config(width=15, height=2, relief='flat', bg='black', foreground='#FFFFFF', activeforeground='#ED1C24',
                activebackground="black", font=f)
    quit.pack(expand=TRUE, anchor='s')
    window.mainloop()



