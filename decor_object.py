import pygame


# Create our decor 

class Decor(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.x=500
        self.y=400
        self.image = pygame.image.load('assets/personnage.png').convert_alpha()



