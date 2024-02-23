
import pygame


class Math(pygame.sprite.Sprite):

    def __init__(self, pos, grade_lvl = "1st", is_prompt = 0):
        super().__init__()
        self.is_dummy = False
        self.taken = False
        self.grade_lvl = grade_lvl
        self.problems = self.get_problems()
        self.answer = ""

        # sprite
        if is_prompt:
            bird_image_path = "graphics/level_images/bird.png"
            self.image = pygame.image.load(bird_image_path)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            apple_image_path = "graphics/level_images/apple.png"
            self.image = pygame.image.load(apple_image_path)
            self.image = pygame.transform.scale(self.image, (130, 90))

        self.rect = self.image.get_rect(topleft = pos)
    

    def update(self, x_shift):
        self.rect.x += x_shift


    def get_problems(self):
        math_problems = {
            "1st": ["3 + 4", "8 - 2", "5 x 2"],
            "8th": ["2x + 5 = 17", "3y - 7 = 14", "5(2x + 3) = 45"],
            "12th": ["Find the derivative of: f(x) = 2x^2 + 5x - 7",
                     "Find the derivative of: e^x * sin(x)",
                     "Find the derivative of: 2x^2 - 4x"]
        }

        return math_problems[self.grade_lvl]
    
    
    def get_answers(self):
        math_answers = {
            "1st": ["7", "6", "10"],
            "8th": ["x = 6", "y = 7", "x = 3"],
            "12th": ["f(x)' = 4x + 5", "f(x)' = e^x * cos(x) + e^x * sin(x)", "f(x)' = 4x - 4"]
        }

        return math_answers[self.grade_lvl]


    def get_value(self):
        answer = ""
        if self.is_dummy:
            answer = "Dummy"
        else:
            answer = self.get_answers()
        
        return answer
