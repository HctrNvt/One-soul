import pygame
class Monstre():
    def __init__(self,pointDeVie,vitesse,image) -> None:
        # Les attributs de la classe Monstre
        self.corps = pygame.image.load(image).convert()
        self.rect = self.corps.get_rect()
        self.rect.topleft = (10,10)
        self.vie = pointDeVie
        self.vitesse = vitesse
        pass

    def dessiner(self,fenetre,positionX,positionY):
        fenetre.blit(self.corps,(positionX,positionY))
        pass
    # ça marche pas
    def deplacer(self,fenetre,posX,posY):
        fenetre.blit(self.corps,(positionX,positionY))
        pass