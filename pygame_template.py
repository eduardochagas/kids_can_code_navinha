#!/bin/bash

import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init() # inicializa o pygame e cria a janela
pygame.mixer.init() # inicializa os métodos para audio
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # cria a largura e altura da janela do jogo
pygame.display.set_caption("My Game") # define o nome na aba da janela
clock = pygame.time.Clock() # armazena a classe Clock (relogio) a variáve clock


running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # checagem caso feche a janela 
        if event.type == pygame.QUIT:
            running = false
            pygame.quit()

    #update

    # Draw / render
    screen.fill(BLACK)

    pygame.display.flip()
