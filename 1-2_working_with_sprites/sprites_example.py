# Pygame.template - skeleton for a new project

#!/bin/bash

import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50)) #cria uma superficie
        self.image.fill(GREEN) # define uma cor
        self.rect = self.image.get_rect() # pega a área retângular da superficie (a partir daqui, se tronou um retângulo, tendo acesso a todos os métodos do módulo rect do pygame)
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # o centro do retângulo ficará no centro da tela
        
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# inicializa o pygame e cria a janela    
pygame.init() 
pygame.mixer.init() # inicializa os métodos para audio
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # cria a largura e altura da janela do jogo
pygame.display.set_caption("My Game") # define o nome na aba da janela
clock = pygame.time.Clock() # armazena a classe Clock (relogio) a variáve clock

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


# game loop 
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # checagem caso feche a janela 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    #update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen) # desenha todas as sprites do grupo
    # *after* drawing everything, flip de display
    pygame.display.flip()