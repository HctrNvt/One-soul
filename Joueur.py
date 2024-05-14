import pygame

import Entite


class Joueur(Entite):
    def __init__(
        self, pointDeVie: int, vitesse: int, image, coordonnes: tuple, fenetre
    ) -> None:
        super().__init__(pointDeVie, vitesse, image, coordonnes, fenetre)

    def move_right(self):
        self.rect.x += super().vitesse

    def move_left(self):
        self.rect.x -= super().vitesse

    def move_up(self):
        self.rect.y -= super().vitesse

    def move_down(self):
        self.rect.y += super().vitesse

    def checkMouvement(self, key):
        if key == pygame.K_q or key == pygame.K_LEFT:
            # On bouge à gauche
            self.move_left()
        if key == pygame.K_d or key == pygame.K_RIGHT:
            # On bouge à droite
            self.move_right()
        if key == pygame.K_z or key == pygame.K_UP:
            self.move_up()
        if key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
