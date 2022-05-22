import pygame
from os import walk
from random import randint
from pygame.locals import *

from Core.game import *
from Sprite.cosmo import background
from Sprite.tile import tiles
from VoDMap.map_config import map_list as map_list
from Sprite.merchant import merchant, shelf

start_time = None
g = Game()  #!!Ne pas supprimer ce bloc de code!!
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

#surface = pygame.display.get_surface()  #Obtenir la surface de l'écran actuel
DISPLAY_W, DISPLAY_H = 1200, 465

win = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))


picture = pygame.transform.scale(background, (DISPLAY_W, DISPLAY_H))
tile_size = 42  #Taille des tiles (carreaux) pour les niveaux
maplen = map_list[0]
Map_Change = 0
heart = 6
merch_font =  pygame.font.Font(None, 26)
power_font =  pygame.font.Font(None, 38)
click = False


##------------------------------------##
##------------------------------------##
##--------SCRIPT POUR LE PERSO--------##
##------------------------------------##
##------------------------------------##

def import_folder(path):  #fonction qui prend les sprite correspondant au touches
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite): #class du player
    speed = 11 #la vitesse su player 
    gravity = 1.6 #la gravité du player qui influence sur la hauteur de son saut
    
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.80 # à quelle vitesse les animation du personnage vont défiler 
        self.image = self.animations['Sprite_Cosmo_R'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        #player movement
        self.speed = self.speed #la vitesse su player 
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = self.gravity
        self.jump_speed = -19 #la vitesse du saut de player
        self.double = 0

        #player staus
        self.status = 'idle'
        self.on_ground = False


    def import_character_assets(self):
        character_path = 'Sprite/Sprite_png/'
        self.animations = { #on créer un dictionnaire de liste avec toutes les sprites qui vont devoir etre animé
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
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground: #on vérifie si le joueur est bien sur le sol et appuie sur saut
                        self.jump()
                        
        if keys[pygame.K_DOWN]:
            self.direction.y = 25

    def get_status(self): #fonction qui vérifie l'orientation du sprite pour activer les animations qui suivent 
            if self.direction.y < 0 and self.direction.x == 0:
                self.status = 'Stand'
            elif self.direction.x > 0:
                self.status = 'Sprite_Cosmo_R'
            elif self.direction.x < 0:
                self.status = 'Sprite_Cosmo_L'
            elif self.direction.y > 1:
                self.status = 'Stand'
            elif self.direction.x == 0 and self.direction.x == 1:
                self.status = 'Sprite_Cosmo_L'
            elif self.direction.y == 0.1:
                self.status = 'Crouch'
    
            else:
                if self.direction.x != 0:
                    self.status = 'Sprite_Cosmo_R'
                    
                else:
                    self.status = 'Stand'
            
            if self.direction.y == 0:
                self.onGround = 0

    def apply_gravity(self): #fonction de la gravité
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self): #fonction du saut
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()


##--------------------------------##
##--------------------------------##
##----SCRIPT POUR LES ENNEMIS-----##
##--------------------------------##
##--------------------------------##




class Spikes(pygame.sprite.Sprite): #class qui créer les spikes dans le jeu
    def __init__(self, pos, size, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y + 7, 64, 92)

        self.image = pygame.image.load(
            'Sprite/Enemy_png/spike2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
    
        
class HiddenSpike(pygame.sprite.Sprite): #la class qui créer les spikes caché dans le jeu
    def __init__(self, pos, size, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y + 7, 64, 92)

        self.image = pygame.image.load(
            'Sprite/Enemy_png/hidden_spike.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

class Champ(pygame.sprite.Sprite): #focntion de l'énemie champignon, qui est en mouvement
    def __init__(self, pos, size, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y + 7, 64, 92)
        self.speed = randint(3, 7)
        self.walkcount = 0
        self.player = pygame.sprite.GroupSingle()
        self.image = pygame.image.load(
            'Sprite/Champ/Champ 1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)      
        self.walkLeft = [pygame.image.load(
            'Sprite/Champ/Champ 1.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 2.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 3.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 4.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 5.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 6.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 7.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 8.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 9.png').convert_alpha(), pygame.image.load(
            'Sprite/Champ/Champ 10.png').convert_alpha()]
            
    def move(self):
        self.rect.x += self.speed
         
        if Level_Champ == 1:
            self.speed *= -1
        
    def reverse(self): #fonction qui change le sens du champigon apres des conditions
        for return_index in Level_Champ:
            if self.rect.colliderect(return_index): #on verifie si il y a une collision entre l'énemie est l'objet qui le fait changer de sens pour que l'enemie change de sens 
                self.speed *= -1 #change de sens
                
            if self.walkcount >= 30: #compteur pour les animations de l'enemie
                self.walkcount = 0
                
            if self.speed < 0: #si la vitesse est inférieure on flip l'animation
                self.image = self.walkLeft[self.walkcount//3] #animation de l'enemie
                self.walkcount += 1

            else:
                self.image = pygame.transform.flip(self.walkLeft[self.walkcount//3], True, False) #on renverse son image si il y a collision
                self.walkcount += 1
                    

    def collide(self): #on vérifie si il y a collision entre le personnage et un énemie 
        if Level_Player.colliderect(self.rect):
            level.collide = 1

    def update(self):
        self.collide()
        self.reverse()
        self.move()

class Merchant(pygame.sprite.Sprite): #class qui créer le marchand
    def __init__(self, pos, size, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y + 7, 64, 92)
        self.image = pygame.image.load('Sprite/Merchant_png/merchant.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
    
class Shelf(pygame.sprite.Sprite): #class qui créer le l'armoir à coter du marchand
    def __init__(self, pos, size, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y + 7, 64, 92)
        self.image = pygame.image.load('Sprite/Merchant_png/shelf.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        
        
        
        
##--------------------------------##
##--------------------------------##
##---------Menu Marchand----------##
##--------------------------------##
##--------------------------------##


def draw_text(text, font, color, surface, x, y): #fonction qui permet de créer du text
    textobj = font.render(text, 90, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
    
def merchant_menu(): #fonction du menu du marchand pour avoir des superpouvoirs
        Index = 0 #index pour dire qu'elle superpouvoir à été choisi

        mBackground = pygame.Rect(270,10, 700, 440)
         
        button_1 = pygame.Rect(495, 50, 270, 50) #on creer toutes les boites dans lequelles on pourra choisir les pouvoirs
        button_2 = pygame.Rect(460, 155, 350, 50)
        button_3 = pygame.Rect(460, 260, 350, 50)
        button_4 = pygame.Rect(455, 365, 360, 50)
        
        pygame.draw.rect(win, (48,48,48), mBackground)

        pygame.draw.rect(win, (48,48,48), button_1)
        draw_text('BOOST :   50 coins', power_font, (255, 255, 156), win, 510, 63)
        
        pygame.draw.rect(win, (48,48,48), button_2)
        draw_text('HIGHER JUMP :  140 coins ', power_font, (255, 255, 156), win, 470, 167)
        
        pygame.draw.rect(win, (48,48,48), button_3)
        draw_text('1 MORE LIFE :  250 coins', power_font, (255, 255, 156), win, 475, 272)

        
        draw_text('SOME POWERS MAY BE APPLIED NEXT LEVEL', merch_font, (255, 0, 0), win, 280, 430)
    
        if button_1.collidepoint((mx, my)): #on verifie si la souris est sur une boite
                pygame.draw.rect(win, (136, 88, 224), button_1)
                draw_text('BOOST :   50 coins', power_font, (255, 255, 156), win, 510, 63)
                if click and coin_sum >= 50: #on vérifie si on click sur la boite avec la souris
                    Index = 1
                
                
        if button_2.collidepoint((mx, my)):
                pygame.draw.rect(win, (136, 88, 224), button_2)
                draw_text('HIGHER JUMP :  140 coins ', power_font, (255, 255, 156), win, 470, 167)
                if click  and coin_sum >= 140:
                    Index = 2

                
        if button_3.collidepoint((mx, my)):
                pygame.draw.rect(win, (136, 88, 224), button_3)
                draw_text('1 MORE LIFE :  250 coins', power_font, (255, 255, 156), win, 475, 272)
                if click and coin_sum >= 250:
                    Index = 3
                    
        return Index




##---------------------------------##
##---------------------------------##
##-----SCRIPT POUR LES NIVEAUX-----##
##---------------------------------##
##---------------------------------##


class Tile(pygame.sprite.Sprite):  #creation du tile
    def __init__(self, pos, size):
        super().__init__()
        self.image = tiles[0]
        self.rect = self.image.get_rect(topleft=pos)


class Level:  # creation du niveau avec toutes les variables qui permet de faire marcher le jeu
    def __init__(self, level_data, surface):
        # Level setup
        self.N_hitbox_list = []
        self.hitbox_list = []
        self.back_list = []
        self.champignon_list = []
        self.hidden_spike_list = []
        self.nn = 0
        self.display_surface = surface
        self.setup_level(level_data)
        self.level_number = 0
        self.maplen = []
        self.N_count = 0
        self.keeps = 0
        self.menu_pop = 0
        self.turn = 0           
        self.keep_turn = 0
        self.timer = 0
        self.hidden_x = 0
        self.hidden_y = 0
        self.collide = 0
        

    def setup_level(self, layout):
        self.S_x = 0
        self.S_y = 0
        self.M_x = 0
        self.M_y = 0
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.spike = pygame.sprite.Group()
        self.champ = pygame.sprite.Group()
        self.merchant = pygame.sprite.Group()
        self.shelf = pygame.sprite.Group()
        self.hidden_spike = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size  # les coordonnée x du tile
                y = row_index * tile_size  # les coordonnée y du tile

                if cell == 'X': #création des tile
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                    
                if cell == 'P': #création des spikes
                    spike1 = Spikes((x, y - 8), tile_size, 23, 23)
                    self.spike.add(spike1)
                    self.hitbox_list.append(pygame.Rect(
                        x + 2, y + 2, 36,
                        42))  #creer une liste des hitbox pour tout les enemies, avec les quelles on vérifiera les collisions

                if cell == 'S': #ou le personnage va apparaitre dans le niveau
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                    self.S_x = x
                    self.S_y = y

                if cell == 'N': #pour identifier quand le joueur à atteind la fin du niveau
                    self.N_hitbox_list.append(pygame.Rect(x, y, 1, 1))
                    
                if cell == 'E': #l'énemie champignon
                    mush = Champ((x, y +10), tile_size, 23, 23)
                    self.champ.add(mush)
                    self.champignon_list.append(pygame.Rect(x - 7, y+2, 36, 42))
                    
                if cell == '-': #ce qui permet de changer le sens du champignon
                    self.back_list.append(pygame.Rect(x, y + 15, 1, 1)) 
                    
                if cell == 'M': #création du marchand
                    merchant = Merchant((x-75, y-34), tile_size, 23, 23)
                    self.merchant.add(merchant)
                    self.M_x = x
                    self.M_y = y
                    
                if cell == 'B': #création de l'armoire 
                    shelfs = Shelf((x-60, y-84), tile_size, 23, 23)
                    self.shelf.add(shelfs)
                    
                if cell == 'C':
                    hidden = HiddenSpike((x, y + 2), tile_size, 23, 23)
                    self.hidden_spike.add(hidden)
                    self.hidden_spike_list.append(pygame.Rect(x + 2, y + 2, 36,42))
                    
                    
    def horizontal_movement_collision(self): #fonction qui permet de vérifier les collision verticale avec les tiles
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

    def vertical_movement_collision(self): #fonction qui permet de vérifier les collision horizontale avec les tiles
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

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1: #ce qui permet de savoir si le joueur est sur le sol ou non
            player.on_ground = False



    def marchand(self): #fonction du marchand
        player = self.player.sprite
        keys = pygame.key.get_pressed()

        merchant_string = "Press [ O ] to access the Merchant goods!".format(coin_sum) #On creer le texte pour quand le joueur est au niveau du marchand
        text_merchant = merch_font.render(merchant_string, True, (255, 255, 255))
        if player.rect.y == self.M_y and player.rect.x < self.M_x + 80 and player.rect.x > self.M_x - 95 : #on verifie quand le joueur est au niveau du marchant pour la création de text
            win.blit(text_merchant, [self.M_x - 170 , self.M_y-85])    
            if keys[pygame.K_o]: #on vérifie si le joueur appuie sur la touche o pour ouvrir le menu du marchand
                self.menu_pop = 1
            
        if self.menu_pop == 1: 
            merchant_menu() #on ouvre le menu
            if player.rect.x > self.M_x + 80 or player.rect.x < self.M_x - 95 or keys[pygame.K_m]: #ce qui vérifie si le personnage quitte une certaine zone pour partir du menu ou appuie sur la touche p 
                self.menu_pop = 0
                
        return self.menu_pop
        
        
    def show(self): #fonction qui permet de  tout aficher sur l'écran
        player = self.player.sprite
        
        #les tiles du niveau
        self.tiles.draw(self.display_surface)
        
        #enemy
        self.champ.draw(self.display_surface)
        self.champ.update()
        self.spike.draw(self.display_surface)
        
        #merchant
        self.merchant.draw(self.display_surface)
        self.shelf.draw(self.display_surface)
        self.marchand()

        # player
        self.player.draw(self.display_surface)
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()


    def game_count(self):  #Fonction qui vérifie si le jouer à atteint la fin du niveau
        player = self.player.sprite

        for N_hitboxes in self.N_hitbox_list:
            if player.rect.colliderect(N_hitboxes):
                self.N_count = 1 #si oui on change de niveau

        return self.N_count
        
    def champ_reverse(self):
        return self.back_list #on retounre les coordonné des points ou les champignons vont devoir changer de sens
        
    def player_return(self):  #on retourne les coordoonée du joueur pour vérifier les collision
        player = self.player.sprite
        return player.rect
        
    def colliding(self): #fonction qui verifie si le joueur a toucher un ennemis
        player = self.player.sprite
        
        if player.rect.y > 400:
            self.keeps = 1
            player.rect.x = self.S_x
            player.rect.y = self.S_y
            
               
        # Fonction si le joueur touche un énemie 
        for hitboxes in self.hitbox_list:  #on prend chaque element de la list est creer sa hitbox sur la fenetre
            if player.rect.colliderect(hitboxes) == True: #si oui, le joueur retourne au coordonées de S
                player.rect.x = self.S_x
                player.rect.y = self.S_y
                self.keeps = 1 #et on lui enlève une vie
            
        if self.collide == 1: #si le joueur touche un champignon il recommence au début du niveau
            player.rect.x = self.S_x
            player.rect.y = self.S_y
            self.collide = 0
            self.keeps = 1
        
        for hidden_hitboxes in self.hidden_spike_list:  #on prend chaque element de la list est creer sa hitbox sur la fenetre
            #pygame.draw.rect(win, (255,0,0), hitboxes,2)
            if player.rect.colliderect(hidden_hitboxes) == True:
                player.rect.x = self.S_x
                player.rect.y = self.S_y
                self.hidden_x = hidden_hitboxes[0] #donne les coordonnées du spike que l'on a toucher
                self.hidden_y = hidden_hitboxes[1]
                self.timer = 25
                self.keeps = 1
                    

        if self.timer > 0:
            win.blit(pygame.image.load('Sprite/Enemy_png/hidden_spike.png').convert_alpha(), (self.hidden_x, self.hidden_y))#affiche le spike caché duquelle on vient de mourir
            player.speed = 0 #on enlève la vitesse du joueur pendant quelque seconde pour pas que le joueur soit surpris
            self.timer -= 1
        else:
            player.speed = Player.speed
        
                
        return self.keeps



level = Level(
    map_list[0],
    win)  # maplen = le layout de la carte ; level = Level(maplen, win)

##----------------------------------##
##----------------------------------##
##-----BOUCLE PRINCIPALE DU JEU-----##
##----------------------------------##
##----------------------------------##

run = True  #Boucle principale
movement = []
clock = pygame.time.Clock()
frame_count = 0
frame_rate = 60
coin_sum = 0
font = pygame.font.Font(None, 27)
coinTotal = 0
endBackground = pygame.Rect(0,0, 1400, 770)
buttonEnd = pygame.Rect(685, 275, 310, 50)
levelNumber = 1
while run:
    Level_Change = level.game_count() #on accorde içi a plusieurs fonction la valeurs de tout les return dans la class Level, pour vérifier des états
    Level_collision = level.colliding()
    Level_Marchand = level.marchand()
    Level_Champ = level.champ_reverse()
    Level_Player = level.player_return()
    mx, my = pygame.mouse.get_pos() #ce qui donne les coordonnées de la souris, pour choisir le superpouvoirs du marchand


    #--------------------------#
    #-----COMPTE A REBOURS-----#
    #--------------------------#

    total_seconds = frame_count // frame_rate

    minutes = total_seconds // 60  #pour avoir les minutes totale

    seconds = total_seconds % 60  #avoir les secondes totales

    output_string = "Time: {0:02}:{1:02}".format(minutes,
                                                 seconds)  #format du compteur
    text_timer = font.render(output_string, True, (255, 255, 255))
    win.blit(text_timer, [10, 85])
    frame_count += 2

    #------------------------------#
    #-----CHANGEMENT DE NIVEAU-----#
    #------------------------------#

    if Level_Change == 1:  #On vérifie si le joueur a atteint la fin du niveau
        level.N_count = 0
        Map_Change += 1  #si oui le niveau change
        levelNumber += 1
        level = Level(map_list[Map_Change], win)
        coin()
        coin_sum += coin()
        coinTotal += coin_sum
        frame_count = 0  #reset le compteur
    
    
    draw_text('Level: ' + str(levelNumber),font, (255, 255, 156), win, 960, 20) #quelle niveau le joueur est
    
        
    if heart == 0: #si le joueur n'a plus de vie, on reset tout sans revenir au menu principal
        Player.speed = 11
        Player.gravity = 1.6
        level = Level(map_list[0], win)
        coin_sum = 0
        Map_Change = 0
        heart = 6      
        frame_count = 0
        coinTotal = 0
        levelNumber = 0
                     
                            
    coin_string = "Coins: {0}".format(coin_sum)
    text_coin = font.render(coin_string, True, (255, 255, 255))
    win.blit(text_coin, [1100, 20])
    win.blit(pygame.image.load('Sprite/Merchant_png/Coin.png').convert_alpha(),[1070, 15])

    #---------------------------#
    #-----SYSTEME DE PIECES-----#
    #---------------------------#


    def coin(): #le systeme de pièce
        coin_add = 2 / frame_count * (Map_Change / 0.95 * 1000) #plus le joueur passe du temps dans le niveau, moins il gagnera de pièce, plus il avance dans les niveaux plus il gagnera de pièce par niveau
        money = round(coin_add)
        return money

    #---------------------------#
    #-----SYSTEME DE COEURS-----#
    #---------------------------#
    
    if Level_collision == 1:
        level.keeps = 0
        heart -= 1
    
    if heart == 7:
        win.blit(pygame.image.load('Sprite/Heart/heart_blue.png').convert_alpha(),[10, 20])
    if heart == 6:
      win.blit(pygame.image.load('Sprite/Heart/Heart_Full.png').convert_alpha(),[10, 20])

    elif heart == 5:
      win.blit(pygame.image.load('Sprite/Heart/Heart_5.png').convert_alpha(),[10, 20])

    elif heart == 4:
      win.blit(pygame.image.load('Sprite/Heart/Heart_4.png').convert_alpha(),[10, 20])

    elif heart == 3:
      win.blit(pygame.image.load('Sprite/Heart/Heart_3.png').convert_alpha(),[10, 20])

    elif heart == 2:
      win.blit(pygame.image.load('Sprite/Heart/Heart_2.png').convert_alpha(),[10, 20])
    elif heart == 1:
      win.blit(pygame.image.load('Sprite/Heart/Heart_1.png').convert_alpha(),[10, 20])
    elif heart == 0:
      win.blit(pygame.image.load('Sprite/Heart/Heart_0.png').convert_alpha(),[10, 20])
    

    #---------------------------#
    #----------Marchant---------#
    #---------------------------# 
    
    if Level_Marchand == 1: #on vérifie içi quelle superpouvoirs le joueur à chosis
        if merchant_menu() == 1:
            coin_sum -= 50
            Player.speed = 13
            
    if Level_Marchand == 1:
        if merchant_menu() == 2:
            coin_sum -= 140
            Player.gravity = 1.2
            
    if Level_Marchand == 1:
        if merchant_menu() == 3:
            coin_sum -= 250
            heart +=1
            
    #---------------------------#
    #----Ecran de fin de jeu----#
    #---------------------------# 

    if Map_Change == 18: #quand le joueur arrive à la fin du jeu, un écran de fin de jeu est affiché, il est ensuite enmenner au menu principal
        stTotal = str(coinTotal) + ' coins'
        pygame.draw.rect(win, (0, 0, 0), endBackground)
        draw_text('YOU WON THIS DELICIOUS PIZZA !!', power_font, (255, 255, 243), win, 350, 50)
        win.blit( pygame.transform.scale(pygame.image.load('Sprite/Heart/pizza.png').convert_alpha(), (150, 150)),[850, 15])
        draw_text('YOU HAVE GAINED A TOTAL OF ' +  stTotal , power_font, (255, 255, 156), win, 350, 232)
        draw_text('YOU DID REALLY GOOD', power_font, (255, 255, 243), win, 350, 265)
        pygame.draw.rect(win, (48,48,48), buttonEnd)
        draw_text('COME BACK TO THE MAIN MENU', font, (255, 255, 243), win, 690, 290)        
        if buttonEnd.collidepoint((mx, my)):
            pygame.draw.rect(win, (136, 88, 224), buttonEnd)
            draw_text('COME BACK TO THE MAIN MENU', font, (255, 255, 243), win, 690, 290)
            if click:
                heart = 0
                g.curr_menu.display_menu()
                g.game_loop()
                

                
            
        
    #-------------------------------#
    #-----INITIALISATION DU JEU-----#
    #-------------------------------#
    pygame.display.flip() 

    clock.tick(30)  #fps

    win.blit(
        picture,
        (0, 0))  # initialisation du background ; win.blit(picture, (0, 0))
    level.show()  #montre le niveau dans la fenetre

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Si la fenetre se ferme ou pas
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN: #si le joueur appuie sur la souris
            if event.button == 1:
                click = True
        else:
            click = False

pygame.display.quit()
