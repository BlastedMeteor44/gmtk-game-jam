import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 5
        self.health = 100
        self.width = 50
        self.height = 50

    def draw(self, win, camera):
        pygame.draw.rect(win, (255, 255, 255), (self.x - camera.x, self.y - camera.y, self.width, self.height))
