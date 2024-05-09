import pygame
monstres = []
class Entite():
    def __init__(self,pointDeVie:int,vitesse:int,image,coordonnes:tuple,fenetre) -> None:
        # Les attributs de la classs Entite
        self.fenetre = fenetre
        self.coordonnes = coordonnes
        self.corps = pygame.image.load(image).convert()
        self.rect = self.corps.get_rect()
        self.rect.topleft = (50,50)
        # pas encore utile
        # self.vie = pointDeVie
        # self.vitesse = vitesse
        monstres.append(self)

        self.dessiner(fenetre,coordonnes[0],coordonnes[1])


    def dessiner(self,fenetre,positionX:float,positionY:float):
        fenetre.blit(self.corps,(positionX,positionY))
    # ça marche pas
    # Il faut blit chaque instance à la fin de la boucle
    def deplacer(self,fenetre,posX,posY):
        self.rect.move(posX,posY)
        fenetre.blit(self.corps,self.rect)