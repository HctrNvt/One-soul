import pygame
from pygame.locals import *
# Import des class du projet
import monstre
import interfaces

if (pygame.init() == False):
    print ("Erreur la librairie Pygame n'a pas pu être initialisée")
# On définie les variables de la fenêtre
fenetreX = 1024
fenetreY = 768
fenetre = pygame.display.set_mode((fenetreX,fenetreY))
pygame.display.set_caption("One soul")
fenetre.fill('gray')
# Met en place l'horloge en jeu
clock = pygame.time.Clock()

ennemi = Entite.Entite(100,10,"assets/Perso.png",(0,0),fenetre)
joueur = Entite.Joueur(100,10,"assets/joueur.png",(0,0),fenetre)

icone = Icone("assets/bourse.png",(0,0),fenetre)

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
        for icone in interfaces.icones:
            if event.type == pygame.MOUSEBUTTONDOWN:
                xSouris,ySouris = pygame.mouse.get_pos()
                # Voir quand on clic sur un icone
    pygame.display.update()
