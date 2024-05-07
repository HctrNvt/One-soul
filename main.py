import pygame
from pygame.locals import *
# Import des class du projet
import monstre
if (pygame.init() == False):
    print ("Erreur la librairie Pygame n'a pas pu être initialisée")
# On définie les variables de la fenêtre
fenetre = pygame.display.set_mode((1024,768))
pygame.display.set_caption("One soul")

# Met en place l'horloge en jeu
clock = pygame.time.Clock()

ennemi = monstre.Monstre(100,10,"assets/Perso.png")
ennemi.dessiner(fenetre,0,0)


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
                ennemi.deplacer(fenetre,100,10)
                print("Touche Q")
    for monstre in monstre.monstres:
        monstre.dessiner(fenetre,0,0)
    pygame.display.update()