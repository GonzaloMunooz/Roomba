import pygame
import random

class Acaro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (0, 0, 255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def is_touched(self, roomba_x, roomba_y, roomba_size):
        distance = ((self.x - roomba_x) ** 2 + (self.y - roomba_y) ** 2) ** 0.5
        return distance < self.size + roomba_size

    def update(self, roomba_x, roomba_y, roomba_size):
        if self.is_touched(roomba_x, roomba_y, roomba_size):
            return True
        return False
