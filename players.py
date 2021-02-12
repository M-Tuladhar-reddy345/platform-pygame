from pygame import *
from spriteloader import *


class player:
    def __init__(self, x, y, health=200):
        self.main = main_standing[0]
        self.x = x
        self.y = y
        self.vel_y = 0
        self.vel = 5
        self.framecount = 0
        self.right = False
        self.left = False
        self.jump = False
        self.jump_count = 10
        self.health = health
        self.stop = False
        self.loast_count = 0

    def draw(self, window):
        if self.framecount + 1 > 18:
            self.framecount = 0
        if self.right:
            window.blit(main_right[self.framecount // 3], (self.x , self.y))
            self.img = main_right[self.framecount // 3]
            self.framecount = self.framecount + 1

        elif self.left:
            window.blit(main_left[self.framecount // 3], (self.x , self.y))
            self.img = main_left[self.framecount // 3]
            self.framecount = self.framecount + 1
        else:
            window.blit(main_standing[self.framecount // 3], (self.x , self.y))
            self.img = main_standing[self.framecount // 3]
            self.framecount = self.framecount + 1
        self.rect = self.img.get_rect()
    def is_on(self, platform):
        return (pygame.rect(self.x, self.y,
                        32, 32)
            .colliderect(platform.rect))
