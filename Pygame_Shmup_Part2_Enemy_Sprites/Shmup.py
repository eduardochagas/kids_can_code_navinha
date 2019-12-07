# Smup game

#!/bin/bash

import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init() # inicializa o pygame e cria a janela
pygame.mixer.init() # inicializa os métodos para audio
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # cria a largura e altura da janela do jogo
pygame.display.set_caption("Smup") # define o nome na aba da janela
clock = pygame.time.Clock() # armazena a classe Clock (relogio) a variáve clock

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0 #faz o player parar ao despressionar a tecla do teclado
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        # não deixa que o player passe das laterais da tela.
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx # incrementa o valor da velocidade na posição x do player


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) # a posição x do retângulo aparecerá de forma aleatória somente entre 0 até a largura da tela.
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8) # define uma velocidade aleatória (velocidade entre 1 e 8) para os inimigos. 
        self.speedx = random.randrange(-3, 3) # define uma velocidade aleatória (velocidade entre -3 e 3) para os inimigos.
        # OBS: quando definimos velocidades para x e y, os objetos caem na tela em posição diagonal (pq ambos x e y possuem valor de velocidade).


    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20: # se o topo do retangulo do inimigo for MAIOR que a altura da tela + 10 OU se o lado esquerdo do retângulo for MENOR que -25 (que é -25 pixels a menos antes do inicio da largura da tela, que fica no lado esquerdo da tela) OU se o lado direito do retângulo do inimigo for MAIOR que 20 (que é 20 pixels a mais após a largura da tela, que fica no lado direito da tela).
            self.rect.x = random.randrange(WIDTH - self.rect.width) # a posição x do retângulo aparecerá de forma aleatória somente entre 0 até a largura da tela.
            self.rect.y = random.randrange(-100, -40) # a posição y do retângulo aparecerá de forma aleatória anterior a altura da tela ( a menos 100 pixels da altura da tela).
            self.speedy = random.randrange(1, 8) # define uma velocidade aleatória (velocidade entre 1 e 8) para os inimigos. 


all_sprites = pygame.sprite.Group() # define um grupo para inserção de imagens
mobs = pygame.sprite.Group() # define um grupo somente para os inimigos
player = Player() # cria o objeto Player()
all_sprites.add(player) # adiciona o objeto player ao agrupamento de sprites
for i in range(8): # para cada item de 0 a 8:
    m = Mob() # cria o inimigo
    all_sprites.add(m) # adiciona o inimigo criado ao grupo all_sprites
    mobs.add(m) # adiciona o inimigo criado ao grupo mobs

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
    all_sprites.update() #chama o método atualiza de cada objeto inserido em all_sprites ( que é um pygame.sprite.Group())

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen) #desenha as sprites armazenadas em um grupo na superficie (no caso, a tela do pygame)
    # *after* drawing everything, flip de display
    pygame.display.flip()
