import pygame
from Core.game import *

class Menu():
  def __init__(self, game):
    self.game = game
    self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
    self.run_display = True
    self.cursor_rect = pygame.Rect(0, 0, 20, 20)
    self.offset = -100
  
  def draw_cursor(self):
    self.game.draw_text('>>>', 25, self.cursor_rect.x - 20, self.cursor_rect.y - 4)

  def blit_screen(self):
    self.game.window.blit(self.game.display, (0, 0))
    pygame.display.update()
    self.game.reset_keys()

class MainMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)
    self.state = "START GAME"
    self.startx, self.starty = self.mid_w, self.mid_h
    self.rulesx, self.rulesy = self.mid_w, self.mid_h + 35
    self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
    self.quitx, self.quity = self.mid_w, self.mid_h + 105
    self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      self.check_input()
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('VOYAGE OF DEATH', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text("START GAME", 30, self.startx, self.starty)
      self.game.draw_text("RULES", 30, self.rulesx, self.rulesy)
      self.game.draw_text("CREDITS", 30, self.creditsx, self.creditsy)
      self.game.draw_text("QUIT", 30, self.quitx, self.quity)
      self.draw_cursor()
      self.blit_screen()
      
  def move_cursor(self):
    if self.game.DOWN_KEY:
      if self.state == 'START GAME':
        self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
        self.state = 'RULES'
      elif self.state == 'RULES':
        self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
        self.state = 'CREDITS'
      elif self.state == 'CREDITS':
        self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
        self.state = 'QUIT'
      elif self.state == 'QUIT':
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.state = 'START GAME'
    elif self.game.UP_KEY:
      if self.state == 'START GAME':
        self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
        self.state = 'QUIT'
      elif self.state == 'QUIT':
        self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
        self.state = 'CREDITS'
      elif self.state == 'CREDITS':
        self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
        self.state = 'RULES'
      elif self.state == 'RULES':
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.state = 'START GAME'
  
  def check_input(self):
    self.move_cursor()
    if self.game.START_KEY:
      if self.state == 'START GAME':
        MainMenu.display_menu.run_display = False
      elif self.state == 'RULES':
        self.game.curr_menu = self.game.rules
      elif self.state == 'CREDITS':
        self.game.curr_menu = self.game.credits
      elif self.state == 'QUIT':
        self.game.curr_menu = self.game.quit
      self.run_display = False
    if self.game.BACK_KEY:
      quit()

class RulesMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      if self.game.START_KEY or self.game.BACK_KEY:
        self.game.curr_menu = self.game.main_menu
        self.run_display = False
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('RULES', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text('You must reach the end of each level to finish the game.', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
      self.game.draw_text('Use the arrow keys and spacebar to move around.', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
      self.game.draw_text('You can also purchase power-ups from the merchant when interacting with him.', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 80)
      self.game.draw_text('Watch out for enemies, spikes and hidden spikes!', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 120)
      self.blit_screen()

class CreditsMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      if self.game.START_KEY or self.game.BACK_KEY:
        self.game.curr_menu = self.game.main_menu
        self.run_display = False
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('CREDITS', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text('Made by DADOUN Nathan and KILICOGLU-SAISON Rémi', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
      self.blit_screen()

class QuitMenu(Menu): 
  def __init__(self, game):
    Menu.__init__(self, game)
    self.state = 'YES'
    self.yesx, self.yesy = self.mid_w, self.mid_h
    self.nox, self.noy = self.mid_w, self.mid_h + 35
    self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      self.check_input()
      self.game.display.fill((0, 0, 0))
      self.game.draw_text('ARE YOU SURE YOU WANT TO QUIT?', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text('YES', 30, self.yesx, self.yesy)
      self.game.draw_text('NO', 30, self.nox, self.noy)
      self.draw_cursor()
      self.blit_screen()
      
  def check_input(self):
    if self.game.BACK_KEY:
      self.game.curr_menu = self.game.main_menu
      self.run_display = False
    elif self.game.UP_KEY or self.game.DOWN_KEY:
      if self.state == 'YES':
        self.state = 'NO'
        self.cursor_rect.midtop = (self.nox + self.offset, self.noy)
      elif self.state == 'NO':
        self.state = 'YES'
        self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)
    elif self.game.START_KEY:
      if self.state == 'YES':
        quit()
      if self.state == 'NO':
        self.game.curr_menu = self.game.main_menu
        self.run_display = False

#Tutos: Partie 1: https://www.youtube.com/watch?v=a5JWrd7Y_14  Partie 2: https://www.youtube.com/watch?v=bmRFi7-gy5Y
