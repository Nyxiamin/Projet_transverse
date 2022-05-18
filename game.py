import pygame
from hammer import Hammer
from player import Player
from math import atan2, sin, cos
from decor_object import Decor
from end_object import Object

class Game:
    def __init__(self):
        #know if the game has been launched
        self.running = False
        self.player = Player()
        self.decor = Decor()
        self.hammer = Hammer()
        self.end = Object()
        self.pressed = {}

    def update(self, Screen, R_P):

        # detect mouse position
        hammer_image=self.hammer.image
        position = pygame.mouse.get_pos()
        print(position)
        angle = atan2(position[1] - (self.hammer.position[1]),
                      position[0] - (self.hammer.position[0]))
        self.x_top_hammer=self.player.position_center_x + 130*cos(angle)
        self.y_top_hammer=self.player.position_center_y + 130*sin(angle)
        print("Positions:",self.x_top_hammer, self.y_top_hammer)

        Running = False

        # checks if there is no collision with the decor from the hammer
        pos_x = self.x_top_hammer
        pos_y = self.y_top_hammer
        pos_dec_x = self.decor.x
        pos_dec_y = self.decor.y
        from decor_function import collision
        if not collision(pos_dec_x, pos_dec_y, pos_x, pos_y):
            playerrotate = pygame.transform.rotate(self.hammer.image,
                                                   -angle * 57.29)
            playerpos1 = (self.hammer.position[0] -
                          playerrotate.get_rect().width / 2,
                          self.hammer.position[1] -
                          playerrotate.get_rect().height / 2)
            Screen.blit(playerrotate, playerpos1)
            R_P=(playerrotate, playerpos1)

        else:
            playerpos1 = self.player.x, self.player.y
            Screen.blit(R_P[0], R_P[1])


        # checks if there is no collision with the decor from the player
        pos_x = playerpos1[0]
        pos_y = playerpos1[1]
        pos_dec_x = self.decor.x
        pos_dec_y = self.decor.y
        from decor_function import collision
        if not collision(pos_dec_x, pos_dec_y, pos_x, pos_y):
            pos_x, pos_y = pygame.mouse.get_pos()
            self.player.x, self.player.y = pos_x, pos_y
        else:
            pos_x, pos_y = self.player.x, self.player.y

        # Check that the player has not touched the end condition (objet)
        pos_end_x = self.end.x
        pos_end_y = self.end.y
        from end_function import touch
        if touch(pos_end_x, pos_end_y, pos_x, pos_y):
            Running = True

        # apply the decor

        Screen.blit(self.decor.image, (self.decor.x, self.decor.y))

        # apply the end condition (objet)

        Screen.blit(self.end.image, (self.end.x, self.end.y))

        # apply the player

        Screen.blit(self.player.image, self.player.position)

        return R_P, Running
