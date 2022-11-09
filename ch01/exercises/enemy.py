import pygame
import random 

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load("assets/enemy.png")
    self.rect = self.image.get_rect()
    self.speed = 1





class Projectile(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load("assets/projectile.png")
    self.rect = self.image.get_rect()
    self.speed = 1

  def update(self):
    self.rect.x += 

