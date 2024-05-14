interfaces = []
class Interfaces():
    def __init__(self, image, coordonnes: tuple, fenetre) -> None:
        self.cordonnes = coordonnes
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = coordonnes
        self.fenetre = fenetre
        fenetre.blit(self.image,coordonnes)
        icones.append(self)
    def dessiner(self):
        self.fenetre.blit(self.image,self.coordonnes)
    def onClick():
        print("Clic")
