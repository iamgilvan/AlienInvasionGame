import sys
import pygame

from Settings.settings import Settings


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    # dimensões da tela
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    # Títlulo da Janela
    pygame.display.set_caption("Alien Invasion")

    # Define a cor de fundo no formato rgb
    pg_color = (ai_settings.bg_color)

    # Inicia o loop principal do jogo
    while True:
        # Observa eventos do teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço
        screen.fill(pg_color)

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()