import pygame
import random

class Juego:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Roomba en movimiento")
        self.WHITE = (255, 255, 255)
        self.acaros = [Acaro(random.randint(50, 750), random.randint(50, 550)) for _ in range(20)]
        self.roomba = Roomba(400, 300)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.roomba.target_x, self.roomba.target_y = event.pos

            self.roomba.update_position()
            self.screen.fill(self.WHITE)
            self.roomba.draw(self.screen)

            for acaro in self.acaros[:]:
                if acaro.is_touched(self.roomba.x, self.roomba.y, self.roomba.size):
                    self.acaros.remove(acaro)
                else:
                    acaro.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)
        
        pygame.quit()
