import pygame
from utils import lerp

class Roomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.size = 20
        self.speed = 15

    def update_position(self):
        self.x = lerp(self.x, self.target_x, 0.45)
        self.y = lerp(self.y, self.target_y, 0.45)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.size)

    

    def move(self, dx, dy):
        self.target_x += dx * self.speed
        self.target_y += dy * self.speed
