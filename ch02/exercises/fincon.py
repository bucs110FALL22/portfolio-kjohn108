import pygame
from Player import Player
from enemy import Enemy

class Controller:
  def __init__(self):
    pygame.init()
    self.width = 500
    self.height = int(self.width * 0.8)
    self.screen = pygame.display.set_mode((self.width, self.height))

    num_of_av = 1
    
    self.avatars = pygame.sprite.Group()
    for i in range(num_of_av):
      avatar = Player(200, 200)
      self.avatars.add(avatar)

    


def mainloop(self):
  clock = pygame.time.Clock()
  FPS = 30
  
#movement start 
  moving_right = False
  moving_left = False

  run = True
  while run:
    clock.tick(FPS)
    for i in range(0, tiles):
      self.screen.blit(BG, (i * 400 + scroll , 0))
  
    scroll-= 5
    if abs(scroll) > 400:
      scroll = 0
    bg_fill()
  self.avatar.display()
  self.avatar.movement(moving_right, moving_left)

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      run = False
      #Key presses down
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        moving_left = True
        
      if event.key == pygame.K_d:
        moving_right = True

      if event.key == pygame.K_w:
        self.avatar.jump = True
          
        
    
  #key releases
        
    if event.type == pygame.KEYUP:
      
      if event.key == pygame.K_a:
        moving_left = False

      if event.key == pygame.K_d:
        moving_right = False



    for avatar in self.avatars:
      avatar.update()
      self.screen.fill(self.background)
      self.avatars.draw(self.screen)

        
      pygame.display.flip()
            
