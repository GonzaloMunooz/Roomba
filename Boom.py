import pygame
import concurrent.futures
import time

class Boom:
    def __init__(self, x, y, juego):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 0, 0)
        self.juego = juego
        self.running = True
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.executor.submit(self.move_down)
        self.executor.submit(self.detect_collision)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def is_touched(self, roomba_x, roomba_y, roomba_size):
        distance = ((self.x - roomba_x) ** 2 + (self.y - roomba_y) ** 2) ** 0.5
        return distance < self.size + roomba_size

    def move_down(self):
        while self.running:
            self.y += 1
            time.sleep(0.1)  # Esperar 0.1 segundos antes de la siguiente actualización

    def detect_collision(self):
        while self.running:
            if self.is_touched(self.juego.roomba.x, self.juego.roomba.y, self.juego.roomba.size):
                self.juego.running = False  # Detener el juego si la Roomba toca un explosivo
                self.running = False
            time.sleep(0.1)  # Esperar 0.1 segundos antes de la siguiente verificación

    def stop(self):
        self.running = False
        self.executor.shutdown(wait=True)
