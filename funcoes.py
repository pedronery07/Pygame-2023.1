import pygame
import time
from config import WIDTH, HEIGHT, cores, background_color, title_font, txt_font
from assets import theme_song

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

#Funções para colocar texto na tela
def text_objects(text,color,size):
    if size == "small":
        textSurface = txt_font.render(text,True,color)
    elif size == "medium":
        textSurface = txt_font.render(text,True,color)
    elif size == "large":
        textSurface = txt_font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message(msg,color,gameDisplay,y_displace = 0, size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#Função da tela inicial
clock = pygame.time.Clock()
def game_intro():
    
    intro = True

    pygame.mixer.music.play(-1)

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(background_color)
        message("Bem-vindo ao Tetris !!!", cores['VD'], gameDisplay, -100,  "large")
        
        message("O objetivo do jogo é obter máxima pontuação por meio do posicionamento de blocos na tela", cores['R'], gameDisplay, -30)
        
        message("Cada linha completada será liberada, sendo possível liberar mais de uma linha ao mesmo tempo.", cores['AZ'], gameDisplay ,10)
        
        message("Se não for mais possível inserir blocos na tela, a rodada e contagem de pontos irá acabar.", cores['AM'], gameDisplay,  50)
        
        message("Pressione ENTER para iniciar ou ESPAÇO para sair", cores['VM'], gameDisplay,80)

        pygame.display.update()
        clock.tick(5)

