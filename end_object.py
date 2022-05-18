import pygame


# Create an object to touch for the end of the game

class Object(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.x=700
        self.y=400
        self.image =pygame.image.load('assets/personnage.png').convert_alpha()



