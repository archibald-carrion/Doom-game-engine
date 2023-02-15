from algorithms import *
from button import *
from map import *
from object import *
from object_handler import *
from object_renderer import *
# from pathfinding import *
from player import *
import pygame
# from raycasting import *
from settings import *
from sound import *
import sys


class Game:
    def __init__(self):
        self.game_stage = 'start_screen' # game stage is either "start_ screen", "main_menu", or "game"
        pygame.init()

        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.global_trigger = False 
        self.global_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.global_event, 40)
        self.new_game()
    
    def new_game(self):
        if not self.game_stage == 'start_screen' and not self.game_stage == 'main_menu':
            self.game_stage = 'main_menu'
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pygame.mixer.music.play(-1)

        self.start_screen = pygame.image.load('resources/textures/start_screen.png').convert_alpha()
        self.start_screen = pygame.transform.scale(self.start_screen, (WIDTH, HEIGHT))
        self.main_menu = pygame.image.load('resources/textures/main_menu.png').convert_alpha()
        self.main_menu = pygame.transform.scale(self.main_menu, (WIDTH, HEIGHT))

        self.start_button = Button(BLACK, 1100, 350, 350.0, 80.0, "start game")
        self.quit_button = Button(BLACK, 1100, 500, 350.0, 80.0, "leave game")


    def update(self):
        if self.game_stage == "main_menu":
            pygame.mouse.set_visible(True)
            start_button_hovered = self.start_button.is_hovered(pygame.mouse.get_pos()) 
            if start_button_hovered:
                self.start_button.color = (10, 10, 10)
                if pygame.mouse.get_pressed()[0]:
                    self.game_stage = "game"
            else:
                self.start_button.color = BLACK

            quit_button_hovered = self.quit_button.is_hovered(pygame.mouse.get_pos()) 
            if quit_button_hovered:
                self.quit_button.color = (10, 10, 10)
                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    sys.exit()
            else:
                self.quit_button.color = BLACK

        elif self.game_stage == "game" and self.player.alive:
            pygame.mouse.set_visible(False)
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()
        self.player.update()

        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        if self.game_stage == "start_screen":
            self.screen.blit(self.start_screen, (0, 0))
        elif self.game_stage == "main_menu":
            self.screen.blit(self.main_menu, (0, 0))
            self.start_button.draw(self.screen)
            self.quit_button.draw(self.screen)
        else:
            if self.player.alive and not self.player.game_won:
                self.object_renderer.draw()
                self.weapon.draw()

    def check_events(self):
        self.global_trigger = False

        if self.game_stage == "start_screen":
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_stage = "main_menu"

        elif self.game_stage == "main_menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

        else: # in game
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == self.global_event:
                    self.global_trigger = True

                if self.player.alive and not self.player.game_won:
                    self.player.single_fire_event(event)

                if (not self.player.alive or self.player.game_won) and (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    self.player.new_game = True


    def run(self):
        while True:
                self.check_events()
                self.update()
                self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
