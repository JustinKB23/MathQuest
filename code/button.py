# Helper class to create the buttons 
import pygame

class Button:
    def __init__(self, text, x, y, width=200, height=60):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spacing = 20  # Adjust the spacing between buttons
        self.gap = 10
        self.cornerRadius = 10  # Adjust the corner radius

    def draw(self, screen):
        # Button color
        button_rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        button_color = pygame.Color(0, 0, 255)  # Blue color for demonstration
        pygame.draw.rect(screen, button_color, button_rect, border_radius=self.cornerRadius)

        # Button text
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(self.x, self.y))
        screen.blit(text_render, text_rect.topleft)

    def clicked(self, pos):
        rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        return rect.collidepoint(pos)