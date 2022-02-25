import pygame
from os import walk

from Core.game import Game
from Sprite.cosmo import background
from VoDMap.map_config import world2_lvl2 as maplen
from Sprite.merchant import merchant, shelf

start_time = None
g = Game()  #!!Ne pas supprimer ce bloc de code!!
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

  
surface = pygame.display.get_surface()  #Obtenir la surface de l'écran actuel
ScreenWidth = 1200  #Largeur de la fenetre, pour les bords ; Valeur de base: 900 ; Sinon, remplacer avec: surface.get_width()
ScreenHeight = 462  #Hauter de la fenetre ; Valeur de base 495 ; Sinon, remplacer avec: surface.get_height()

win = pygame.display.set_mode((900, 495))  #Ajouter pygame.FULLSCREEN après (ScreenWidth, ScreenHeight)

picture = pygame.transform.scale(background, (ScreenWidth, ScreenHeight))
tile_size = 42  #Taille des tiles (carreaux) pour les niveaux

##----------------------------------------------##
##----------------------------------------------##
##-----------SCRIPT POUR LE PERSO---------------##
##----------------------------------------------##
##----------------------------------------------##


def import_folder(
        path):  #fonction qui prend les srpite correspondant au touches
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.3
        self.image = self.animations['Sprite_Cosmo_R'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        #player movement
        self.speed = 9
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 1.2
        self.jump_speed = -16

        #player staus
        self.status = 'idle'

    def import_character_assets(self):
        character_path = 'Sprite/Sprite_png/'
        self.animations = {
            'Sprite_Cosmo_R': [],
            'Sprite_Cosmo_L': [],
            'Crouch': [],
            'Stand': []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_DOWN]:
            self.direction.y = -0.5

    def get_status(self):
        if self.direction.y < 0 and self.direction.x == 0:
            self.status = 'Stand'
        elif self.direction.x > 0:
            self.status = 'Sprite_Cosmo_R'
        elif self.direction.x < 0:
            self.status = 'Sprite_Cosmo_L'
        elif self.direction.y > 1:
            self.status = 'Stand'
        elif self.direction.y == -0.5:
            self.status = 'Crouch'
        else:
            if self.direction.x != 0:
                self.status = 'Sprite_Cosmo_R'
            else:
                self.status = 'Stand'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()


##------------------------------------##
##------------------------------------##
##------SCRIPT POUR LES Enemies-------##
##------------------------------------##
##------------------------------------##


class Enemy(object):
    from Sprite.enemies import base_spike1, base_spike2

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [y, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y + 7, 64, 92)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 3:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.base_spike1[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.base_spike2[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x, self.y + 7, 64, 92)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.y - self.vel > self.path[0]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0


spike1 = Enemy(505, 501, 64, 64, 402)


class Spikes(pygame.sprite.Sprite):
    def __init__(self, pos, size, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y + 7, 64, 92)

        self.image = pygame.image.load(
            'Sprite/Enemy_png/spike2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


##------------------------------------##
##------------------------------------##
##------SCRIPT POUR LES NIVEAUX-------##
##------------------------------------##
##------------------------------------##


class Tile(pygame.sprite.Sprite):  #creation du tile
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')  #la couleur du tile
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Level:  # creation du niveau
    def __init__(self, level_data, surface):
        # Level setup
        self.hitbox_list = []
        self.nn = 0
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.spike = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size  # les coordonnée x du tile
                y = row_index * tile_size  # les coordonnée y du tile

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    spike1 = Spikes((x - 20, y - 35), tile_size, 23, 23)
                    self.spike.add(spike1)
                    self.hitbox_list.append(pygame.Rect(
                        x - 8, y - 23, 75,
                        92))  #creer une liste des hitbox de tout les enemies
                if cell == 'C':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

    def show(self):
        player = self.player.sprite

        #les tiles du niveau
        self.tiles.draw(self.display_surface)

        #enemy
        self.spike.draw(self.display_surface)
        for hitboxes in self.hitbox_list:  #on prend chaque element de la list est creer sa hitbox sur la fenetre
            if player.rect.y - player.rect[3] < hitboxes[1] + hitboxes[
                    3] and player.rect.y + player.rect[3] > hitboxes[1]:
                if player.rect.x + player.rect[3] > hitboxes[
                        0] and player.rect.x < hitboxes[0] + hitboxes[2]:
                    player.rect.x = 45
                    player.rect.y = 25

        # player
        self.player.draw(self.display_surface)
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()


level = Level(maplen, win)  # maplen = le layout de la carte ; level = Level(maplen, win)


def redrawGameWindow():  #ouvre la fenetre win avec le sprite
    #spike1.draw(win)
    pygame.display.update()


##------------------------------------##
##------------------------------------##
##------BOUCLE PRINCIPALE DU JEU------##
##------------------------------------##
##------------------------------------##

run = True  #Boucle principale
movement = []
while run:
    clock.tick(30)  #fps
    win.blit(picture, (0, 0))  # initialisation du background ; win.blit(picture, (0, 0))
    level.show()  #montre le niveau dans la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Si la fenetre se ferme ou pas
            run = False

    redrawGameWindow()

pygame.quit()