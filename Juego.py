import json
import pygame
import random
import concurrent.futures
from Roomba import Roomba
from Acaro import Acaro
from Boom import Boom
from Puntuacion import Puntuacion



class Juego:
    def __init__(self):
        pygame.init()  # Inicializar Pygame
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Roomba en movimiento")
        self.WHITE = (255, 255, 255)
        self.acaros = [Acaro(random.randint(50, 750), random.randint(150, 600)) for _ in range(5)]
        self.booms = []
        self.roomba = Roomba(400, 300)
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False  # Variable para controlar el estado de pausa
        self.puntuacion = Puntuacion()
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.high_score = self.load_high_score()  # Cargar la puntuación máxima al inicio

    def load_high_score(self):
        """Carga la puntuación máxima desde un archivo JSON."""
        try:
            with open("high_score.json", "r") as file:
                data = json.load(file)
                return data.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def save_high_score(self):
        """Guarda la puntuación máxima en un archivo JSON."""
        if self.puntuacion.score > self.high_score:
            self.high_score = self.puntuacion.score
            with open("high_score.json", "w") as file:
                json.dump({"high_score": self.high_score}, file)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused  # Alternar el estado de pausa

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
                # Crear un nuevo ácaro en una posición aleatoria
                new_acaro = Acaro(random.randint(50, 750), random.randint(150, 600))
                self.acaros.append(new_acaro)

    def update_booms(self):
        for boom in self.booms[:]:
            boom.update()

    def draw(self):
        self.screen.fill(self.WHITE)
        self.roomba.draw(self.screen)
        for acaro in self.acaros:
            acaro.draw(self.screen)
        for boom in self.booms:
            boom.draw(self.screen)
        self.puntuacion.render(self.screen)
        pygame.display.flip()

    def create_booms(self):
        while self.running:
            x = random.randint(50, 750)
            y = 0
            self.booms.append(Boom(x, y, self))
            pygame.time.wait(150)  # Esperar 1 segundo antes de crear otro explosivo

    def remove_boom(self, boom):
        if boom in self.booms:
            self.booms.remove(boom)

    def run(self):
        self.executor.submit(self.create_booms)
        while self.running:
            self.handle_events()
            if not self.paused:  # Solo actualizar y dibujar si el juego no está en pausa
                self.handle_keys()
                self.update_roomba()
                self.update_acaros()
                self.update_booms()  # Actualizar la posición de los explosivos
                self.draw()
            self.clock.tick(30)
        
        self.save_high_score()  # Guardar la puntuación máxima al finalizar el juego
        self.stop_all_booms()
        self.executor.shutdown(wait=True)
        pygame.quit()

    def stop_all_booms(self):
        for boom in self.booms:
            boom.running = False
