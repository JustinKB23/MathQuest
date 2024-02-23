
import pygame
from os import walk, getcwd

def import_folder(path):
    surface_list = []
    path = getcwd() + path
    
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
