import pygame

from Sprite.Cosmo_png import walkLeft 
from Sprite.Cosmo_png import walkRight
from Sprite.Cosmo_png import background
from Sprite.Cosmo_png import down
from Sprite.Cosmo_png import charR
from Sprite.Cosmo_png import charL
from VoDMap.map_config import world1_lvl3 as maplen
from Sprite.Merchant_png import merchant, shelf
from Sprite.Enemies import base_spike1




pygame.init()



surface = pygame.display.get_surface() #Obtenir la surface de l'écran actuel
ScreenWidth = 1700 #Largeur de la fenetre, pour les bords ; Valeur de base: 1700 ; Sinon, remplacer avec: surface.get_width()
ScreenHeight = 704 #Hauter de la fenetre ; Valeur de base 704 ; Sinon, remplacer avec: surface.get_height() 

win = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.FULLSCREEN) #Ajouter pygame.FULLSCREEN après (ScreenWidth, ScreenHeight)

picture = pygame.transform.scale(background, (ScreenWidth, ScreenHeight))
tile_size = 64 #Taille des tiles (carreaux) pour les niveaux





##----------------------------------------------##
##----------------------------------------------##
##-----------SCRIPT POUR LE PERSO---------------## 
##----------------------------------------------##
##----------------------------------------------##      

class player(object): #les fonction 
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = 9
    self.isJump = False
    self.jumpCount = 10
    self.left = False
    self.right = False
    self.crouch = False
    self.walkCount =  0
    self.hitbox = (self.x + 20, self.y + 7, 64, 92)
    
  def draw(self, win): #fonction pour le png du sprite
        if self.walkCount + 1 >= 10: #Dépends du nombre de photos du Sprite --> animation de marche du Sprite
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.crouch:
          win.blit(down, (self.x, self.y))
          self.walkCount += 1

        else:
          if self.vel > 0.1 :
            win.blit(charR, (self.x,self.y))

          else :
            win.blit(charL, (self.x,self.y))
        self.hitbox = (self.x + 20, self.y + 7, 64, 92)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

clock = pygame.time.Clock()
cosmo1 = player(45, 541, 64, 64) #coordonée et taille du sprite





##------------------------------------##
##------------------------------------##
##------SCRIPT POUR LES Enemies-------##
##------------------------------------##
##------------------------------------##

class enemy(pygame.sprite.Sprite):
  
  def __init__(self, x, y, width, height, end):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [y, end]
        self.walkCount = 0
        self.vel = 0
        self.hitbox = (self.x, self.y + 7, 64, 92)
        self.image = base_spike1
        self.rect = base_spike1[0]


        


  def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 3:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.image[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.image[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x, self.y + 7, 64, 92)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
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

  def hit(self): 
    print("hit")   


class spikes(enemy):
  def __init__(self,pos,size):
    super().__init__()
    #self.image = enemy(505, 501, 64, 64, 402)
    #self.rect = self.image.get_rect(topleft = pos)





##------------------------------------##
##------------------------------------##
##------SCRIPT POUR LES NIVEAUX-------##
##------------------------------------##
##------------------------------------##



class Tile(pygame.sprite.Sprite): #creation du tile
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill('grey') #la couleur du tile
		self.rect = self.image.get_rect(topleft = pos)
    

	def update(self,x_shift):
		self.rect.x += x_shift
    

class Level: # creation du niveau
  def __init__(self,level_data,surface):
    # Level setup
    self.display_surface = surface
    self.setup_level(level_data)
    self.world_shift = 0
  
  def setup_level(self,layout):
    win = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.FULLSCREEN)
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.spike = pygame.sprite.Group()
    for row_index,row in enumerate(layout):
      for col_index,cell in enumerate(row):
          x = col_index * tile_size # les coordonnée x du tile
          y = row_index * tile_size # les coordonnée y du tile

          if cell == 'X':          
            tile = Tile((x,y),tile_size) 
            self.tiles.add(tile)
          if cell =='P':
            spike1 = enemy(505, 501, 64, 64, 402)
            self.spike.add(spike1)


  def horizontal_movement_collision(self):
    player = self.player.sprite



  def show(self):
    #les tiles du niveau
    self.tiles.draw(self.display_surface)

    #enemy
    self.spike.draw(self.display_surface)
    
    # sprite
    self.player.draw(self.display_surface)
    self.horizontal_movement_collision()
  
level = Level(maplen, win) # maplen = le layout de la carte ; 

spike1 = enemy(505, 501, 64, 64, 402)
def redrawGameWindow() : #ouvre la fenetre win avec le sprite 
  cosmo1.draw(win)
  spike1.draw(win)
  pygame.display.update()

##------------------------------------##
##------------------------------------##
##------BOUCLE PRINCIPALE DU JEU------##
##------------------------------------##
##------------------------------------##


run = True #Boucle principale
movement = []
while run:
    clock.tick(30) #fps
    win.blit(picture, (0, 0)) # initialisation du background
    level.show() #montre le niveau dans la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si la fenetre se ferme ou pas
            run = False





    keys = pygame.key.get_pressed() #fonction qui recupere les touches appuyées

    

    if keys[pygame.K_LEFT] and cosmo1.x > cosmo1.vel: # quand la touche fleche gauche est appuyé
          cosmo1.x -= cosmo1.vel
          cosmo1.left = True 
          cosmo1.right = False

    elif keys[pygame.K_RIGHT] and cosmo1.x < ScreenWidth - cosmo1.width - cosmo1.vel: # quand la touche fleche droite est appuyé
          cosmo1.x += cosmo1.vel
          cosmo1.right = True
          cosmo1.left = False
          movement.append(1)

    else:
        cosmo1.right = False
        cosmo1.left = False
        cosmo1.walkCount = 0

    if keys[pygame.K_DOWN] and cosmo1.isJump == False: # quand la touch fleche du bas est appuyé
        cosmo1.vel = 0
        cosmo1.right = False
        cosmo1.left = False
        cosmo1.crouch = True

    else:
        cosmo1.vel = 9
        cosmo1.crouch = False

    if not(cosmo1.isJump): # quand la touche espace est appuyé
        if keys[pygame.K_SPACE]:
          cosmo1.isJump = True
          cosmo1.right = False 
          cosmo1.left = False
          cosmo1.walkCount = 0

    else: #fonction pour quand le personnage est dans les aires
        if cosmo1.jumpCount >= -10:
          neg = 1.5 #hauteur du saut
          if cosmo1.jumpCount <= 0: #temps dans les aires
            neg = -1.5
          cosmo1.y -= (cosmo1.jumpCount ** 2) * 0.3 * neg
          cosmo1.jumpCount -= 1

        else:
          cosmo1.isJump = False
          cosmo1.jumpCount = 10




    redrawGameWindow()


pygame.quit()