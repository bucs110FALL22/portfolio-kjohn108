import pygame
from Player import Player
from enemy import Enemy

class Controller():
  def __init__(self):
    pygame.init()
    #Screen creation
    self.width = 500
    self.height = int(self.width * 0.8)
    self.screen = pygame.display.set_mode((self.width, self.height))

#frame control
    clock = pygame.time.Clock()
    FPS = 30
  
#movement start 
    moving_right = False
    moving_left = False

#Any colors 
    BG = pygame.image.load('Mountains.webp')
    BG = pygame.transform.scale(BG, (400,300))
    avatar = Player(200, 200, 2)
    scroll = 0
    tiles = math.ceil(width / 400) + 1 
  def bg_fill():#Background fill and image stuff  
    pygame.draw.line(screen, 'Black', (0,250), (width,250), 20)


  def mainloop(self):
    run = True
    while run:
      pygame.clock.tick(FPS)

      for i in range(0, tiles):
        screen.blit(BG, (i * 400 + scroll , 0))
  
      scroll-= 5
      if abs(scroll) > 400:
        scroll = 0
      bg_fill()
      avatar = Player()
      
      avatar.display()
  
      avatar.movement(moving_right, moving_left)


  

      for event in pygame.event.get():

         if event.type == pygame.QUIT:
           run = False
      #Key presses down
         if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
             moving_left = True
        
           if event.key == pygame.K_d:
             moving_right = True

           if event.key == pygame.K_ESCAPE:
             run = False
     #key releases
         if event.type == pygame.KEYUP:
      
           if event.key == pygame.K_a:
             moving_left = False

           if pygame.key == pygame.K_d:
             moving_right = False

         
            
      pygame.display.update()

pygame.quit()