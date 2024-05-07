import pygame
from pygame.locals import *
# Import des class du projet
import monstre
if (pygame.init() == False):
    print ("Erreur la librairie Pygame n'a pas pu être initialisée")

fenetre = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()

ennemi = monstre.Monstre(100,10,"assets/Perso.png")
ennemi.dessiner(fenetre,0,0)
ennemi.deplacer(fenetre,1000,10)

# La boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_q:
                print("Touche Q")

    pygame.display.update()