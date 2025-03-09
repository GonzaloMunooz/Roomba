import pygame

class Puntuacion:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def incrementar(self):
        self.score += 1

    def render(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
