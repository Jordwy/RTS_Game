import pygame

class Building:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (139,69,19)  # Brown-ish building

    def draw(self, surface, camera_x, camera_y):
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        pygame.draw.rect(surface, self.color, (screen_x, screen_y, self.width, self.height))
