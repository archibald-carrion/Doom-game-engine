from settings import *
import pygame
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pygame.time.get_ticks()
        self.new_game = False
        self.alive = True
        self.game_won = False

    def check_game_over(self):
        self.alive = self.health > 1
        if not self.alive:
            self.game.object_renderer.game_over()
            pygame.display.flip()
            if self.new_game:
                self.game.new_game()

    def check_game_won(self):
        self.game_won = True
        for npc in self.game.object_handler.npc_list:
            if npc.alive:
                self.game_won = False
                break
        if self.game_won:
            self.game.object_renderer.game_won()
            pygame.display.flip()
            if self.new_game:
                self.game.new_game()

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH and self.alive:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def get_damage(self, damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()

    def single_fire_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_shooting = event.button == 1 and not self.shot and not self.game.weapon.reloading
            if player_shooting:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        self.check_wall_collision(dx, dy)
        self.angle %= math.tau


    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        no_wall_x = self.check_wall(int(self.x + dx * scale), int(self.y))
        no_wall_y = self.check_wall(int(self.x), int(self.y + dy * scale))

        if no_wall_x:
            self.x += dx 
        if no_wall_y:
            self.y += dy

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()

        mouse_out_border = mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT
        if mouse_out_border:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])

        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()
        self.check_game_over()
        self.check_game_won()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)