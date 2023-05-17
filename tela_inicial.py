import pygame
import time 
from config import WIDTH, HEIGHT
from funcoes import message, text_objects, game_intro

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')

pygame.display.update()

clock = pygame.time.Clock()

game_intro()