import sys
import pygame

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    # dimensões da tela
    screen = pygame.display.set_mode((1200,800))
    # Titlulo da Janela
    pygame.display.set_caption("Alien Invasion")

    # Inicia o loop principal do jogo
    while True:
        #Observa eventos do teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()