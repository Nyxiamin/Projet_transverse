import pygame
from game import Game
from tkinter import *

def gameplay():
    R_T=()
    pygame.init()
    fps = 60

    # generate a window

    pygame.display.set_caption("Getting Over You")

    # generate base window size

    Screen = pygame.display.set_mode((1280, 720))

    # background import

    background_jeu = pygame.image.load('assets/background.jpg').convert_alpha()

    # creation of the game menu

    Img_accueil = pygame.image.load('assets/Image_banner.png').convert_alpha()
    Img_accueil_rect = Img_accueil.get_rect()
    Img_accueil_rect.x = Screen.get_width() / 2.5
    Img_accueil_rect.y = Screen.get_height() / 2.5

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
                Screen.blit(Img_accueil, Img_accueil_rect)

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
    pygame.quit()

    def see_score():

        message.configure(text='Your score is ' + str(time))

    fenetre = Tk()

    fenetre.title('Fin du jeu')

    fenetre.minsize(width=500, height=250)

    # marges intérieures

    fenetre.config(padx=20, pady=20)

    # libellé

    libelle = Label(fenetre, text='Enter your name:')

    libelle.pack()

    # boîte de saisie

    nom = Entry(fenetre)

    nom.focus_set()  # boîte de saisie par défaut

    nom.pack(pady=10)

    # libellé pour afficher un message

    message = Label(fenetre, text='')

    message.pack(padx=10, pady=(0, 10))

    # boutons

    bouton_soumettre = Button(fenetre, text='See my score', command=see_score)

    bouton_soumettre.pack(padx=10, pady=(0, 10))

    bouton_terminer = Button(fenetre, text='Quit', command=fenetre.destroy)

    bouton_terminer.pack(padx=10, pady=(0, 10))

    # la fenêtre s'affiche puis attend les interactions de l'usager

    fenetre.mainloop()
    #add_leaderboard(nom.get(), time)