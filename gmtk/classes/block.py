import pygame

class Block:
    def __init__(self, mode, x, y, size=50):
        self.mode = mode
        self.x = x
        self.y = y
        self.size = size
        self.original_size = size

    def draw(self, win, camera):
        if self.mode == 0:
            colour = (0, 0, 255)
            self.size = self.original_size * 2
        elif self.mode == 1:
            colour = (255, 0, 0)
            self.size = self.original_size
        pygame.draw.rect(win, colour, (self.x - camera.x, self.y - camera.y, self.size, self.size))
