import pygame
import random
from Roomba import Roomba
from Acaro import Acaro
from Puntuacion import Puntuacion

class Juego:
    def __init__(self):
        pygame.init()  # Inicializar Pygame
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Roomba en movimiento")
        self.WHITE = (255, 255, 255)
        self.acaros = [Acaro(random.randint(50, 750), random.randint(50, 550)) for _ in range(20)]
        self.roomba = Roomba(400, 300)
        self.clock = pygame.time.Clock()
        self.running = True
        self.puntuacion = Puntuacion()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.roomba.move(0, -1)
        if keys[pygame.K_s]:
            self.roomba.move(0, 1)
        if keys[pygame.K_a]:
            self.roomba.move(-1, 0)
        if keys[pygame.K_d]:
            self.roomba.move(1, 0)

    def update_roomba(self):
        self.roomba.update_position()

    def update_acaros(self):
        for acaro in self.acaros[:]:
            if acaro.update(self.roomba.x, self.roomba.y, self.roomba.size):
                self.acaros.remove(acaro)
                self.puntuacion.incrementar()

    def draw(self):
        self.screen.fill(self.WHITE)
        self.roomba.draw(self.screen)
        for acaro in self.acaros:
            acaro.draw(self.screen)
        self.puntuacion.render(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.handle_keys()
            self.update_roomba()
            self.update_acaros()
            self.draw()
            self.clock.tick(30)
        
        pygame.quit()
