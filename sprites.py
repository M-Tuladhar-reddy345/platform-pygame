import pygame
from spriteloader import *
import time

class mainplayer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('maincharacter/mainnew.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.vel = 5
        self.framecount = 0
        self.right = False
        self.left = False
        self.jump = False
        self.jump_count = 10
        self.health = 2
        self.stop = False
        self.loast_count = 0
        self.gameover = True
        self.in_air = True

    def update(self, window, data, lava):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if self.gameover:
            self.image = pygame.image.load('maincharacter/mainnew.png')
            if keys[pygame.K_UP] and self.jump == False and self.in_air == False:
                self.vel_y = -12
                self.jump = True
                self.left = False
                self.right = False
            if keys[pygame.K_UP] == False:
                self.jump = False
            if keys[pygame.K_RIGHT]:
                dx += 5
                self.left = False
                self.right = True
                self.image = pygame.image.load('maincharacter/mainnew.png')
            if keys[pygame.K_LEFT]:
                dx -= 5
                self.left = True
                self.right = False
                self.image = pygame.image.load('maincharacter/mainnewleft.png')

            if keys[pygame.K_RIGHT] == False and keys[pygame.K_LEFT] == False:
                self.right = False
                self.left = False


            self.vel_y += 1
            if self.vel_y > 12:
                self.vel_y = 12
            dy += self.vel_y

            #colliderect
            self.in_air =True
            for tile in data:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            #collide with lava
            if pygame.sprite.spritecollide(self, lava, False):
                self.gameover = False
                self.health -= 1

            self.rect.x += dx
            self.rect.y += dy
            window.blit(self.image,(self.rect.x, self.rect.y + 5))

        if self.gameover == False:
            self.image = pygame.image.load('maincharacter/deadmainnew.png')
            window.blit(self.image,(self.rect.x, self.rect.y))
            self.gameover = True
            self.rect.x = self.x
            self.rect.y = self.y




class lavasprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('lava.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self, window):
        window.blit(self.img,(self.rect.x, self.rect.y))

class flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('flag.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self, window):
        window.blit(self.img,(self.rect.x, self.rect.y))

class hearts():
    def __init__(self, x, y):
        self.img = pygame.image.load('life.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, window):
        window.blit(self.img,(self.rect.x, self.rect.y))
