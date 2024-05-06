import pygame

if (pygame.init() ==False):
    print ("Erreur")
pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
input()