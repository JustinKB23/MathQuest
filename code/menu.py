# The main menu of the game 
# Different options to choose from
# - Start game button that will start the game
# - Settings button that will take the user to the settings screen
# - How to play button that will take the user to the how to play screen
# - Quit game button that will close the app

import pygame
from button import Button
from howtoplay import HowToPlay
from menu_settings import MenuSettings

class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()

        #Different buttons
        self.start_button = Button("Start", self.screen_width // 2, self.screen_height // 2 - 150)
        self.settings_button = Button("Settings", self.screen_width // 2, self.screen_height // 2 - 60)
        self.how_to_play_button = Button("How to Play", self.screen_width // 2, self.screen_height // 2 + 30)
        self.quit_button = Button("Quit", self.screen_width // 2, self.screen_height // 2 + 120)


        #Background image
        background_image_path = "graphics/menu/MenuBackground.gif"
        self.background_image = pygame.image.load(background_image_path)
        # Scale the image to fit the screen size
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        #Game Logo
        logo_image_path = "graphics/menu/Math Quest.png"
        self.logo_image = pygame.image.load(logo_image_path)

        # Set the desired size for the logo
        logo_width, logo_height = 250, 250  # Adjust the desired size
        self.logo_image = pygame.transform.scale(self.logo_image, (int(logo_width), int(logo_height)))

        # Initial grade level
        self.grade_lvl = "1st"


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        action = self.handle_click(event.pos)
                        if action == "start_game":
                            return "start_game"
                        elif action == "how_to_play":
                            self.show_how_to_play()
                        elif action == "settings":
                            self.show_settings()
                        
            self.draw()

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

    def draw(self):
        #Background image
        self.screen.blit(self.background_image, (0, 0))

        #Logo image
        logo_image_rect = self.logo_image.get_rect(center=(self.screen_width // 2, 80))  # Adjust the y-coordinate as needed
        self.screen.blit(self.logo_image, logo_image_rect.topleft)

        # Draw buttons
        self.start_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.how_to_play_button.draw(self.screen)
        self.quit_button.draw(self.screen)
    
    def handle_click(self, pos):
        # Check if any button is clicked
        if self.start_button.clicked(pos):
            return "start_game"  
        elif self.settings_button.clicked(pos):
            return "settings"
        elif self.how_to_play_button.clicked(pos):
            return "how_to_play"
        elif self.quit_button.clicked(pos):
            pygame.quit()
    
    def show_how_to_play(self):
        how_to_play = HowToPlay(self.screen_width, self.screen_height)
        how_to_play.run()
    
    def show_settings(self):
        settings_screen = MenuSettings(self.screen_width, self.screen_height)
        settings_screen.run()
        self.grade_lvl = settings_screen.grade_lvl
    



