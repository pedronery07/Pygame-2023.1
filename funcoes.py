import pygame
import time
import random
from config import WIDTH, HEIGHT, cores, background_color, title_font, txt_font, formas,topo_esquerdo_x,topo_esquerdo_y,play_height,play_width,tam_bloco, Peça, s_height, s_width 
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
                if event.key == pygame.K_RETURN:
                    intro = False
                if event.key == pygame.K_SPACE:
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

def valida_posicao():
    pass

#Funções que criam o grid do jogo
def cria_grid(posicao_fixa = {}):
    grid = []
    for a in range(20):
        linha = []
        for b in range(10):
            bloco = (0,0,0)
            linha.append(bloco)
        grid.append(linha)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in posicao_fixa:
                c = posicao_fixa[(j, i)]
                grid[i][j] = c
    
    return grid

def seleciona_forma():
    escolha = Peça(5,0,random.choice(formas))
    return escolha

def desenha_grid(superficie, grid):
    pass

def desenha_janela(superficie,grid):
    superficie.fill(background_color)
    
    pygame.font.init()
    
    titulo = title_font.render('Tetris',1,(255,255,255))

    superficie.blit(titulo,(topo_esquerdo_x + play_width/2 - titulo.get_width()/2,30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(superficie, grid[i][j], (topo_esquerdo_x + j*tam_bloco, topo_esquerdo_y + i*tam_bloco, tam_bloco, tam_bloco), 0)

    pygame.draw.rect(superficie, (255,0,0), (topo_esquerdo_x, topo_esquerdo_y, play_width, play_height), 4)

    desenha_grid(superficie,grid)

    pygame.display.update()

def principal():

    posicao_fixa = {}

    grid = cria_grid(posicao_fixa)

    muda_peça = False
    jogo_aberto = True
    peça = seleciona_forma()
    proxima_peça = seleciona_forma()
    relogio = pygame.time.Clock()
    queda = 0 

    while jogo_aberto:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                jogo_aberto = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    peça.x -= 1
                    if not(valida_posicao(peça,grid)):
                        peça.x += 1
                if e.key == pygame.K_RIGHT:
                    peça.x += 1
                    if not (valida_posicao(peça,grid)):
                        peça.x -= 1
                if e.key == pygame.K_DOWN:
                    peça.y -= 1
                    if not (valida_posicao(peça,grid)):
                        peça.y += 1
                if e.key == pygame.K_UP:
                    peça.rotação += 1
                    if not(valida_posicao(peça,grid)):
                        peça -= 1
        desenha_janela(win,grid)              


def menu_principal(win):
    principal(win)
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
menu_principal(win)