import pygame

class Boom:
    def __init__(self, x, y, juego):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 0, 0)
        self.juego = juego
        self.running = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def is_touched(self, roomba_x, roomba_y, roomba_size):
        distance = ((self.x - roomba_x) ** 2 + (self.y - roomba_y) ** 2) ** 0.5
        return distance < self.size + roomba_size

    def update(self):
        self.y += 10  # Mover hacia abajo
        if self.y > 600:  # Si sale de la pantalla, eliminarlo
            self.juego.remove_boom(self)
        if self.is_touched(self.juego.roomba.x, self.juego.roomba.y, self.juego.roomba.size):
            self.juego.running = False  # Detener el juego si la Roomba toca un explosivo
            self.juego.remove_boom(self)
