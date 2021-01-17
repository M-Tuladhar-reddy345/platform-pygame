import pygame
from pygame.locals import *
import os

os.environ['SDL_VIDEODRIVER'] = 'dummy'

pygame.init()

screen_height = 1000
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('platformer')

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.quit():
            run = False
    