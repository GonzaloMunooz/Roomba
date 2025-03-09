import pygame
import random
import concurrent.futures
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

    def draw(self):
        self.screen.fill(self.WHITE)
        self.roomba.draw(self.screen)
        for acaro in self.acaros[:]:
            if acaro.is_touched(self.roomba.x, self.roomba.y, self.roomba.size):
                self.acaros.remove(acaro)
                self.puntuacion.incrementar()
            else:
                acaro.draw(self.screen)
        self.puntuacion.render(self.screen)
        pygame.display.flip()

    def run(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while self.running:
                # Ejecutar eventos y teclas en el hilo principal
                self.handle_events()
                self.handle_keys()

                # Ejecutar actualización de la Roomba y dibujo en hilos separados
                futures = [
                    executor.submit(self.update_roomba),
                    executor.submit(self.draw)
                ]
                concurrent.futures.wait(futures)
                self.clock.tick(30)
        
        pygame.quit()
