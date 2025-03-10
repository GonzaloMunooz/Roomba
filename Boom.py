import pygame

class Boom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def is_touched(self, roomba_x, roomba_y, roomba_size):
        return (self.x - roomba_x)**2 + (self.y - roomba_y)**2 < (self.size + roomba_size)**2
    
    def update_position(self):
        self.y -= 1
        self.clock.tick(30)
