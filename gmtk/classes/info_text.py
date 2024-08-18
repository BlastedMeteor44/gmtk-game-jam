import pygame

class Info_text:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, win, player):
        text = self.font.render(f'Player x: {player.x}, Player y: {player.y}', True, (255, 255, 255))
        win.blit(text, (10, 10))
