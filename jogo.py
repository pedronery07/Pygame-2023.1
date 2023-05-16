import pygame
from config import WIDTH, HEIGHT

#Inicia o pygame
pygame.init()

#Configuração de tela e nome do jogo
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tetris')
