import pygame

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0        
        self.width, self.height = pygame.display.get_surface().get_size()

    def ease_camera(self, strength, player):
        self.width, self.height = pygame.display.get_surface().get_size()
        target_x = player.x - (self.width // 2 - player.width // 2)
        target_y = player.y - (self.height // 2 - player.height // 2)
        self.x += (target_x - self.x) * strength
        self.y += (target_y - self.y) * strength
