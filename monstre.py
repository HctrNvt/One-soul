import pygame
monstres = []
class Monstre():
    def __init__(self,pointDeVie,vitesse,image) -> None:
        # Les attributs de la classe Monstre
        self.corps = pygame.image.load(image).convert()
        self.rect = self.corps.get_rect()
        self.rect.topleft = (50,50)
        self.vie = pointDeVie
        self.vitesse = vitesse

    def dessiner(self,fenetre,positionX,positionY):
        fenetre.blit(self.corps,(positionX,positionY))
    # ça marche pas
    # Il faut blit chaque instance à la fin de la boucle
    def deplacer(self,fenetre,posX,posY):
        self.rect.move(posX,posY)
        fenetre.blit(self.corps,self.rect)
