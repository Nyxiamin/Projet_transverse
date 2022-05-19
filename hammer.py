import pygame
from player import Player
import math


# class for the hammer

class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player=Player()
        self.velocity = 5
        self.image = pygame.image.load('assets/hammer.png').convert_alpha()
        self.x=self.player.position_center_x
        self.y=self.player.position_center_y
        self.position=self.x, self.y
        self.top=self.x+100, self.y


