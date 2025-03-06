class Roomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 0, 0)
        self.target_x = x
        self.target_y = y

    def update_position(self):
        self.x = lerp(self.x, self.target_x, 0.1)
        self.y = lerp(self.y, self.target_y, 0.1)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
