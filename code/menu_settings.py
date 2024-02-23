# The settings screen from the menu 
# The screen lists multiple grade options that will change the difficulty of the 
# math questions
# After selecting a grade level a prompt will appear to confirm the level selected
# on the bottom of the screen
# The screen also has a back to menu button to bring the user back after selecting a grade

import pygame
from button import Button

class MenuSettings:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()

        # Add grade level buttons
        self.first_grade_button = Button("1st Grade", self.screen_width // 2, self.screen_height // 2 - 50)
        self.eighth_grade_button = Button("8th Grade", self.screen_width // 2, self.screen_height // 2 + 30)
        self.twelfth_grade_button = Button("12th Grade", self.screen_width // 2, self.screen_height // 2 + 110)

        # Blank text label for grade selection - label will pop up after selection is made
        self.grade_selected_label = ""

        #Back to Menu Button
        self.back_button = Button("Back to Menu", self.screen_width // 2, self.screen_height // 2 + 250)

        #Background Image
        background_image_path = "graphics/menu/MenuBackground.gif"
        self.background_image = pygame.image.load(background_image_path)

        # Scale the image to fit the screen size
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        # Selected grade level
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

                        if action == "back_to_menu":
                            return "back_to_menu"  # Return to the main menu
                        else:
                            self.grade_lvl = action

            self.draw()

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

    def draw(self):
       
        self.screen.blit(self.background_image, (0, 0))

        # Create a font
        font = pygame.font.Font(None, 36)

        # Render text
        text_lines = [
            "Settings:",
            "",
            "Please select a grade level.",
            "",
            "Press 'Back to Menu' to return to the main menu."
        ]

        text_y = 50  # Starting y-coordinate for text

        for line in text_lines:
            text_render = font.render(line, True, (0, 0, 0))  # Render text in black
            text_rect = text_render.get_rect(center=(self.screen_width // 2, text_y))
            self.screen.blit(text_render, text_rect.topleft)
            text_y += 40  # Adjust the spacing between lines

         # Draw grade level buttons
        self.first_grade_button.draw(self.screen)
        self.eighth_grade_button.draw(self.screen)
        self.twelfth_grade_button.draw(self.screen)

        # Draw grade selection label
        font = pygame.font.Font(None, 24)
        label_render = font.render(self.grade_selected_label, True, (0, 0, 0))  # Render text in black
        label_rect = label_render.get_rect(center=(self.screen_width // 2, self.screen_height - 20))
        self.screen.blit(label_render, label_rect.topleft)

        # Draw the back button
        self.back_button.draw(self.screen)

    #Different buttons when clicked on for grade level
    def handle_click(self, pos):
        selection = "1st"

        if self.first_grade_button.clicked(pos):
            self.grade_selected_label = "1st Grade was selected"
            selection = "1st"

        elif self.eighth_grade_button.clicked(pos):
            self.grade_selected_label = "8th Grade was selected"
            selection = "8th"

        elif self.twelfth_grade_button.clicked(pos):
            self.grade_selected_label = "12th Grade was selected"
            selection = "12th"
    
        elif self.back_button.clicked(pos):
            selection = "back_to_menu"
        
        return selection
        