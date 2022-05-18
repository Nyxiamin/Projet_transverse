import pygame
from player import Player
import math


# Créer notre classe pour notre personnage principal

class Marteau(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.player=Player()
        self.velocity = 5
        self.image = pygame.image.load('assets/marteau.png').convert_alpha()
        self.x=self.player.position_center_x
        self.y=self.player.position_center_y
        self.position=self.x, self.y
