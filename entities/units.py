import pygame
import math

class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 255)   # Blue unit
        self.size = 10
        self.speed = 2
        self.target_pos = None     # (x, y) target if moving

    def update(self):
        if self.target_pos is not None:
            tx, ty = self.target_pos
            dx = tx - self.x
            dy = ty - self.y
            dist = math.sqrt(dx*dx + dy*dy)
            if dist > 1:
                self.x += (dx/dist) * self.speed
                self.y += (dy/dist) * self.speed
            else:
                self.x, self.y = tx, ty
                self.target_pos = None

    def draw(self, surface, camera_x, camera_y):
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        pygame.draw.circle(surface, self.color, (screen_x, screen_y), self.size)
