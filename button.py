import pygame
from settings import *

class Button():
    def __init__(self, color, x, y, width, height,text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text !='':
            font = pygame.font.SysFont('Constantia', 60)
            text = font.render(self.text, 1, WHITE)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def is_hovered(self, position):
        if position[0] > self.x and position[0] < self.x+self.width:
            if position[1] > self.y and position[1] < self.y+self.height:
                return True
        return False