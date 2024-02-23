# How to play screen
# Teaches the user how to play by giving a text 
# Also includes a back to menu button when user wants to go back to menu
import pygame
from button import Button

class HowToPlay:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()

        #Back to menu button
        self.back_button = Button("Back", self.screen_width // 2, self.screen_height // 2 + 90)
        
        #Background Image
        background_image_path = "graphics/menu/MenuBackground.gif"
        self.background_image = pygame.image.load(background_image_path)
        # Scale the image to fit the screen size
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

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

            self.draw()

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

    def draw(self):
        #Background image
        self.screen.blit(self.background_image, (0, 0))

        # Create a font
        font = pygame.font.Font(None, 36)

        # Render text
        text_lines = [
            "How to Play",
            "",
            "1. Answer math questions to win",
            "2. Use the arrow keys to move your character",
            "3. Use SPACE to jump through the level",
            "4. Pick up apples with the up arrow key",
            "5. Return it to the bird to check if answer is correct",
            "",
            "Press 'Back' to return to the main menu."
        ]

        text_y = 50  # Starting y-coordinate for text

        for line in text_lines:
            text_render = font.render(line, True, (0, 0, 0))  # Render text in black
            text_rect = text_render.get_rect(center=(self.screen_width // 2, text_y))
            self.screen.blit(text_render, text_rect.topleft)
            text_y += 40  # Adjust the spacing between lines

        # Create a back button
        self.back_button.draw(self.screen)
        
    def handle_click(self, pos):
        if self.back_button.clicked(pos):
            return "back_to_menu"
        return None

