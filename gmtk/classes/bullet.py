import pygame
import math

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = math.radians(direction)
        self.width = 5
        self.height = 5

    def update(self):
        self.x += self.speed * math.cos(self.direction)
        self.y -= self.speed * math.sin(self.direction)

    def draw(self, win, camera):
        pygame.draw.rect(win, (0, 255, 0), (self.x - camera.x, self.y - camera.y, self.width, self.height))
