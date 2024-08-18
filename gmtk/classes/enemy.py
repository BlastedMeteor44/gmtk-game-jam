import pygame
import math

class Enemy:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.alive = True
        self.width = width
        self.height = height
        self.speed = 2

    def move(self, player):
        direction_x = player.x - self.x
        direction_y = player.y - self.y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance
        self.x += direction_x * self.speed
        self.y += direction_y * self.speed

    def draw(self, win, camera, bullets, touching_function):
        if self.alive:
            pygame.draw.rect(win, (255, 0, 0), (self.x - camera.x, self.y - camera.y, self.width, self.height))
        
        for bullet in bullets:
            if (touching_function(self.x, self.x + self.width, bullet.x, bullet.x + bullet.width) and
                touching_function(self.y, self.y + self.height, bullet.y, bullet.y + bullet.height)):
                self.alive = False
                bullets.remove(bullet)
                break
