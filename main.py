import pygame
from pygame.locals import *  # noqa: F403

# Import des class du projet
import interfaces
import Joueur
import Monstre

if pygame.init() is False:
    print("Erreur la librairie Pygame n'a pas pu être initialisée")
# On définie les variables de la fenêtre
fenetreX = 1024
fenetreY = 768
fenetre = pygame.display.set_mode((fenetreX, fenetreY))
pygame.display.set_caption("One soul")
fenetre.fill("gray")
# Met en place l'horloge en jeu
clock = pygame.time.Clock()

ennemi = Monstre.Monstre(100, 10, "assets/joueur.png", (0, 0), fenetre)
joueur = Joueur.Joueur(100, 10, "assets/perso.png", (0, 0), fenetre)

icone = interfaces.Interfaces("assets/perso.png", (50, 100), fenetre)

# La boucle de jeu
while True:
    for event in pygame.event.get():
        # Vérifie si on quitte le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Vérifie si une touche est pressé
        if event.type == pygame.KEYDOWN:
            # La touche escape ?
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        # Quand une touche est relevé
        if event.type == pygame.KEYUP:
            joueur.checkMouvement(event.key)
    pygame.display.update()
