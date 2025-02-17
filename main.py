import pygame
import sys
from settings import *

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Définir le titre de la fenêtre
pygame.display.set_caption('Pacman @ Cap')


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mettre à jour l'affichage
    pygame.display.flip()