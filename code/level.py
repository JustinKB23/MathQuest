
import pygame
from pygame import mixer
from tiles import Tile
from settings import *
from player import Player
from game_math import Math
from random import randint

class Level:
    def __init__(self, level_data, surface, grade_lvl):

        # math
        self.grade_lvl = grade_lvl
        self.problem_num = randint(0,2)
        self.dummy_answers = self.get_dummy_answers()

        # level set up
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.curr_x = 0
        self.state = "playing"  

        # music
        mixer.music.load("sfx/theme.ogg")
        mixer.music.play(-1)

        # end screen
        self.win = False
        win_image_path = "graphics/end_screen/win_screen.jpg"
        self.win_image = pygame.image.load(win_image_path)
        self.win_image = pygame.transform.scale(self.win_image, (screen_width, screen_height+30))
        game_over_image_path = "graphics/end_screen/game_over_screen.jpg"
        self.game_over_image = pygame.image.load(game_over_image_path)
        self.game_over_image = pygame.transform.scale(self.game_over_image, (screen_width, screen_height))


    
    def setup_level(self, layout):
        # Creates level
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.math = pygame.sprite.GroupSingle()
        self.answers = pygame.sprite.Group()
        answer_count = 0


        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x, y = col_index * tile_size, row_index * tile_size

                # Creates tiles
                if cell == "X":
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

                # Creates player
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

                # Creates math prompt (aka the question prompt)
                if cell == "M":
                    math_sprite = Math((x,y), self.grade_lvl, 1)
                    self.math.add(math_sprite)
                        
                # Creates math answers
                if cell == "A":
                        
                    answer_sprite = Math((x,y), self.grade_lvl, 0)

                    # Randomizes correct answers position
                    if self.problem_num == answer_count:
                        answer_sprite.answer = answer_sprite.get_value()[self.problem_num]
                    
                    else:
                        answer_sprite.is_dummy = True
                        answer_sprite.answer = self.dummy_answers.pop(randint(0,1))
                    
                    answer_count += 1
                    self.answers.add(answer_sprite)
                


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx        
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        
        else:
            self.world_shift = 0
            player.speed = 8
    

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        math = self.math.sprite
        font = pygame.font.Font(None, 22)

        # collision with tiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.curr_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.curr_x = player.rect.right

         # tile collision
        if player.on_left and (player.rect.left < self.curr_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.curr_x or player.direction.x <= 0):
            player.on_right = False

        # collision with math
        for sprite in self.math.sprites():
            if sprite.rect.colliderect(player.rect):
                
                # draws question prompt
                pygame.draw.rect(self.display_surface, "white", (50, 50, 500, 70))
                pygame.draw.rect(self.display_surface, "blue", (50, 50, 500, 70), 3)

                text_surface = font.render("In order to beat this level solve the following math problem:", True, "black")
                equation = font.render(math.problems[self.problem_num], True, "black")
                self.display_surface.blit(text_surface, (60, 60))
                self.display_surface.blit(equation, (60, 90))

                # Checks if the player has anything in his inventory
                if player.inventory:

                    # if the answer in the players inventory is the correct answer
                    # the player wins
                    value = player.inventory.answer
                    answer = player.inventory.get_answers()[self.problem_num]

                    if value == answer:
                        self.win = True
                        self.state = "game_over"
                    
                    # else the players inventory becomes empty and the game continues
                    else:
                        player.inventory = None
                        player.inventory_full = False

        
        # collision with answers
        for sprite in self.answers.sprites():
            if sprite.rect.colliderect(player.rect) and not sprite.taken:
                pygame.draw.rect(self.display_surface, "white", (50, 50, 200, 70))
                pygame.draw.rect(self.display_surface, "blue", (50, 50, 200, 70), 3)

                text_surface = font.render("Answer:", True, "black")
                
                answer_text = font.render(sprite.answer, True, "black")
                
                self.display_surface.blit(text_surface, (60, 60))
                self.display_surface.blit(answer_text, (60, 90))
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and not player.inventory_full:
                    player.inventory = sprite
                    player.inventory_full = True
                    sprite.taken = True


    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        # collision with tiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


    def player_death(self):
        player = self.player.sprite
        player_y = player.rect.centery

        if player_y > screen_height:
            self.state = "game_over"
    
    
    def death_state(self):
        mixer.music.pause()
        

        font = pygame.font.Font(None, 50)
        if self.win:
            self.display_surface.blit(self.win_image, (0, 0))
        else:
            self.display_surface.blit(self.game_over_image, (0,0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.state = "quit"


    def get_dummy_answers(self):
        dummy_answers = {
            "1st": [
                ["10", "5", "2"],
                ["5", "9", "3"],
                ["15", "8", "11"]
            ],
            "8th": [
                ["x = 3", "x = 5", "x = -2"],
                ["y = 4", "y = 2", "y = 8"],
                ["x = 9", "x = 6", "x = 2"]
            ],
            "12th": [
                ["f'(x) = 2x + 5", "f'(x) = 4x - 5", "f'(x) = 2x"],
                ["f'(x) = e^x * cos(x) - e^x * sin(x)", "f'(x) = e^x * cos(x)", "f'(x) = e^x"],
                ["f'(x) = 4x + 4", "f'(x) = 2x - 4", "f'(x) = 4x"]
            ]
        }

        return dummy_answers[self.grade_lvl][self.problem_num]


    def run(self):
        
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()


        # math
        self.math.update(self.world_shift)
        self.math.draw(self.display_surface)
        self.answers.update(self.world_shift)


        # Checks if answers have been picked up by player
        # If not it draws them, else it stops drawing them
        for sprite in self.answers:
            if not sprite.taken:
                self.display_surface.blit(sprite.image, sprite.rect)


        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.player_death()



        