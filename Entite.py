import pygame
entites = []
class Entite():
    def __init__(self,pointDeVie:int,vitesse:int,image,coordonnes:tuple,fenetre) -> None:
        # Les attributs de la classs Entite
        self.fenetre = fenetre
        self.coordonnes = coordonnes
        self.corps = pygame.image.load(image).convert()
        self.rect = self.corps.get_rect()
        self.rect.topleft = (50,50)
        # Infos joueur
        self.vie = pointDeVie
        self.vitesse = vitesse
        # On ajoute a la grande liste de toute les entités
        entites.append(self)
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
  
    def move_right(self):
        self.rect.x+= self.velocity
    def move_left(self):
        self.rect.x-= self.velocity
    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity

    def checkMouvement(key):
        if (key == pygame.K_q or key == pygame.K_LEFT):
            # On bouge à gauche
            self.move_left()
        if (key == pygame.K_d or key == pygame.K_RIGHT):
            # On bouge à droite
            self.move_right()
        if (key == pygame.K_z or key == pygame.K_UP):
            self.move_up()
        if (key == pygame.K_s or key == pygame.K_DOWN):
            self.move_down()

        
    def onMort():
        
        pass
    def checkVie():
        if self.vie <= 0:
            self.onMort()
            return False
        return True
