import os
import sys
import math
import pygame
import pygame.mixer
from pygame.locals import *
from world import World, lavasprites, doors
from level import world_data
from players import player
from sprites import mainplayer, hearts

pygame.init()
all_sprites = pygame.sprite.Group()


cloud_img = pygame.image.load('cloud.jpg')
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
tile_size = 25
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()

pygame.display.set_caption("platformer")


def draw_grid():
    for line in range(0, 16):
        pygame.draw.line(screen, (255, 255, 255), (0, line *
                                                   tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size,
                                                   0), (line * tile_size, screen_height))


world = World(world_data)
fallingvel = 3

dx = 0
dy = 0
def main():
    player = mainplayer(50, screen_height - 60)
    run = True
    gameover = False
    while run:
        clock.tick(20)
        screen.blit(cloud_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if player.rect.x == 0:
            player.rect.x = screen_width
        if player.rect.x == screen_width:
            player.rect.x = 0

        if gameover == False:
            world.draw(screen)
            lavasprites.update(screen)
            doors.update(screen)
            player.update(screen, world.tile_list, lavasprites)
            i = 0
            while i <= player.health:
                heart = hearts(30 + (i * 20), 40)
                heart.update(screen)
                i += 1
            if player.health == -1:
                gameover = True
        else:
            menu()

        pygame.display.flip()

    pygame.quit()

def menu():
    run = True
    while run:
        clock.tick(20)
        screen.blit(cloud_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
    pygame.quit()

main()
