import pygame


# class for the player 

class Player(pygame.sprite.Sprite):
  
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.x=600
        self.y=300
        self.position=(self.x, self.y)
        self.position_center_x=self.x+46
        self.position_center_y=self.y+40
        self.position_center=(self.position_center_x, self.position_center_y)
        self.image = pygame.image.load('assets/personnage.png').convert_alpha()