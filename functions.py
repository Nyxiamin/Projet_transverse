import pygame
from game import Game
from tkinter import *
from hammer import Hammer
def gameplay():
    R_T=(0,)
    pygame.init()
    fps = 60

    # generate a window

    pygame.display.set_caption("Getting Over You")

    # generate base window size

    Screen = pygame.display.set_mode((1000, 720))

    # background import

    background_jeu = pygame.image.load('assets/background.jpg').convert_alpha()


    # creation of the play bouton 

    play_button = pygame.image.load('assets/Button_Start.png').convert_alpha()
    play_button_rect = play_button.get_rect()
    play_button_rect.x = Screen.get_width() / 2.25
    play_button_rect.y = Screen.get_height() / 1.5

    # generate the window 

    running = False

    clock = pygame.time.Clock()

    # load the game

    game = Game()

    while running is False:

        #refresh rate

        clock.tick(fps)

        # apply the background

        Screen.blit(background_jeu, (0, 0))


        for event in pygame.event.get():


            # check game status

            if game.running:

                # trigger game instructions

                R_T, running = game.update(Screen, R_T)
            # check if the game has started

            else:

                # homepage 

                Screen.blit(play_button, play_button_rect)

            # window update

            pygame.display.flip()

            # event to close the window

            if event.type == pygame.QUIT:
                running = True
                pygame.quit()

            # detect if the player presses the keys

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            # button to launch the game

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # check if the mouse touches the button to start the game

                if play_button_rect.collidepoint(event.pos):
                    # launch je game
                    game.running = True

    #The game is ended

    time = pygame.time.get_ticks()/1000
    time=round(time)
    pygame.quit()
    #Opening a window to recup the name of the player to put it in the leaderboard

    def validate():
        ('%s' % entry.get())
        window.destroy()

    window = Tk()
    label = Label(window, text="Tell us your name!", width=50,font=("Times", 20))
    label.pack()
    val = StringVar()
    val.set("Player")
    entry = Entry(window, textvariable=val, width=20)
    entry.pack()
    button = Button(window, text="Valider", command=validate, width=10)
    button.pack()
    window.mainloop()
    player = [val.get(),time]
    from Leaderboard import true_edit_leaderboard
    true_edit_leaderboard(player)