import pygame
import math

import random as rand

from classes.camera import Camera
from classes.player import Player
from classes.enemy import Enemy
from classes.block import Block
from classes.bullet import Bullet
from classes.info_text import Info_text
from classes.touching import is_touching

pygame.init()

pygame.display.set_caption("Game")
win = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

running = True

player = Player()
camera = Camera()
enemy = Enemy(100, 100)
clock = pygame.time.Clock()
info = Info_text()

blocks = [
    Block(1, 100, 100),
    Block(0, 300, 300),
    Block(1, 150, 400)
]

bullets = []

def get_direction_to_mouse(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    direction_x = mouse_x - x
    direction_y = mouse_y - y
    magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)
    if magnitude != 0:
        direction_x /= magnitude
        direction_y /= magnitude
    return direction_x, direction_y

def get_bullet_direction():
    direction_x, direction_y = get_direction_to_mouse(player.x - camera.x, player.y - camera.y)
    angle = math.degrees(math.atan2(-direction_y, direction_x))
    return angle

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                for block in blocks:
                    if block.mode == 0:
                        block.mode = 1
                    else:
                        block.mode = 0
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            direction = get_bullet_direction()
            if direction is not None:
                bullets.append(Bullet(player.x + player.width // 2, player.y + player.height // 2, direction))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player.y -= player.speed
    if keys[pygame.K_s]:
        player.y += player.speed
    if keys[pygame.K_a]:
        player.x -= player.speed
    if keys[pygame.K_d]:
        player.x += player.speed

    win.fill((0, 0, 0))

    player.draw(win, camera)

    for block in blocks:
        block.draw(win, camera)

    for bullet in bullets:
        bullet.update()
        bullet.draw(win, camera)

    camera.ease_camera(0.1, player)

    enemy.move(player)
    enemy.draw(win, camera, bullets, is_touching)

    info.draw(win, player)

    pygame.display.update()

pygame.quit()
