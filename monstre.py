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
        self.dessiner(fenetre,coordonnes)

    def dessiner(self,fenetre,position:tuple):
        fenetre.blit(self.corps,(position[0],position[1]))

class Monstre(Entite):
    def __init__(self, pointDeVie: int, vitesse: int, image, coordonnes: tuple, fenetre) -> None:
        super().__init__(pointDeVie, vitesse, image, coordonnes, fenetre)
    def attaque(self,cible):
        if cible is Joueur:
            cible.vie -= 10
        # à faire
    def deplacer(self,fenetre,posX,posY):
        # à faire
        pass
    def deplacerVers(self,position:tuple):
        # à faire
        pass

class Joueur(Entite):
    def __init__(self, pointDeVie: int, vitesse: int, image, coordonnes: tuple, fenetre) -> None:
        super().__init__(pointDeVie, vitesse, image, coordonnes, fenetre)
    def onMort():
        # à faire
        pass
    def checkVie():
        if self.vie <= 0:
            self.onMort()
            return False
        return True