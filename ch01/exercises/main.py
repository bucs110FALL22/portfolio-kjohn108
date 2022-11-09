import pygame
import random




#like an import for classes instead of modules
class Player(pygame.sprite.Sprite): 
  def __init__(self):
    super().__init(self)   #super makes sure everything initiates, only place magic methods are ever called. Just the first line you have ti put in the sprite class init
    self.health = 3
    self.direction = 3 
    #self.image is required br sprite
    self.image = pygame.image.load("assets/hero.pg") #hero.pg imported from folder assets 
    #self.rect also required by sprite
    self.rect = self.image.get_rect()
    self.speed = 1

  def move_up(self):
    self.rect.y -= self.speed
  def move_down(self):
    self.rect.y += self.speed
  def move_left(self):
    self.rect.x -= self.speed
  def move_right(self):
    self.rect.x += self.speed

  def fight(self, opponent):
    return random.ranrange(3) #0 will return false, 1 & 2 will return true