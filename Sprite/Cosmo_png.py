import pygame
win = pygame.display.set_mode((1700, 904))

walkRight = [pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_R/R1 Cosmo.png').convert_alpha(), pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_R/R2 Cosmo.png').convert_alpha(), pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_R/R3 Cosmo.png').convert_alpha(), pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_R/R4 Cosmo.png').convert_alpha()]
walkLeft = [pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_L/L1 Cosmo.png').convert_alpha(), pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_L/L2 Cosmo.png').convert_alpha(), pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_L/L3 Cosmo.png').convert_alpha(), pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_L/L4 Cosmo.png').convert_alpha()]
down = pygame.image.load('Sprite/Sprite_png/Crouch/crouch.png').convert_alpha()
background = pygame.image.load('Sprite/Sprite_png/Background/background.png').convert_alpha()
charR = pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_R/R1 Cosmo.png').convert_alpha()
charL = pygame.image.load('Sprite/Sprite_png/Sprite_Cosmo_L/L1 Cosmo.png').convert_alpha()