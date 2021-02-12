import pygame
import sprites
lavasprites = pygame.sprite.Group()
doors = pygame.sprite.Group()
tile_size = 25
class World():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt_img = pygame.image.load('dirt.png')
        grass_img = pygame.image.load('grass.png')
        water_img = pygame.image.load('water.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile ==1:
                    img = pygame.transform.scale(dirt_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 2:
                    img = pygame.transform.scale(grass_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 3:
                    tilelava = sprites.lavasprite(col_count * tile_size, row_count * tile_size)
                    lavasprites.add(tilelava)
                elif tile == 4:
                    tiledoor = sprites.flag(col_count * tile_size, row_count * tile_size)
                    doors.add(tiledoor)
                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
