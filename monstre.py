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
        self.dessiner(coordonnes)

    def dessiner(self,coordonnees:tuple):
        self.fenetre.blit(self.corps,(coordonnees[0],coordonnees[1]))

class Monstre(Entite):
    def __init__(self, pointDeVie: int, vitesse: int, image, coordonnes: tuple, fenetre, attaque:int) -> None:
        super().__init__(pointDeVie, vitesse, image, coordonnes, fenetre)
        self.attaque = attaque
    def attaqueJoueur(self,cible:Joueur):
        cible.vie -= self.attaque
        # à faire
    def deplacer(self,fenetre,newPosition:tuple):
        # à faire
        pass
    def deplacerVers(self,coordonnees:tuple):
        # à faire
        pass

class Joueur(Entite):
    def __init__(self, pointDeVie: int, vitesse: int, image, coordonnes: tuple, fenetre) -> None:
        super().__init__(pointDeVie, vitesse, image, coordonnes, fenetre)
    def mouvementJoueur(self):
        # à faire
        pass
    def onMort():
        
        pass
    def checkVie():
        if self.vie <= 0:
            self.onMort()
            return False
        return True