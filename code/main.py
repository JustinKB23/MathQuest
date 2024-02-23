
import pygame
import sys
from level import Level
from settings import *
from menu import MainMenu
from pygame import mixer


#Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Main menu
main_menu = MainMenu(screen_width,screen_height)
main_menu_activated = True

# Level
level_activated = False
grade_lvl = "1st"
level_background_image_path = "graphics/level_images/sky_background.jpg"
level_background_image = pygame.image.load(level_background_image_path)
level_background_image = pygame.transform.scale(level_background_image, (screen_width, screen_height))
mixer.music.load("sfx/main_menu.mp3")
mixer.music.play(-1)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()
      
    if main_menu_activated:
        main_menu.run()
        main_menu_activated = False
        grade_lvl = main_menu.grade_lvl
        
    else:
        if not level_activated:
            level = Level(level_map, screen, grade_lvl)
            level_activated = True

        if level.state == "playing":
            screen.blit(level_background_image, (0,0))
            level.run() 
        elif level.state == "game_over":
            level.death_state()
        else:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
    clock.tick(60)

