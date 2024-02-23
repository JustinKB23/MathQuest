
import pygame

image_path = "graphics/level_images/tile.png"
image = pygame.image.load(image_path)

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(image, (size,size))
        self.rect = self.image.get_rect(topleft = pos)


    def update(self, x_shift):
        self.rect.x += x_shift
        