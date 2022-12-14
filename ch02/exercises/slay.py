import pygame

width = 500
height = int(width *0.8)
y = 50 

class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y,): 
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(("assets/5.png"))
    self.image = pygame.transform.scale(self.image, (50,25 ))
    self.image = pygame. transform. rotate(self.image, 180)
    self.rect = self.image.get_rect()
    self.scale = 5
    self.counter = 0

  def update(self):
    if (self.rect.x == 0):
       self.rect.x = width
    else:
      self.counter = self.counter +1
    if (self.counter >= self.scale): 
      self.rect.x = self.rect.x - 1 
      self.counter = 0 

class Controller:

    def __init__(self):
        # we need to setup all our data for our program
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = "Orange"

        number_of_enemies = 1
        self.ems = pygame.sprite.Group()
        xpos = 0
        ypos = 0
        for i in range(number_of_enemies):
            s = Enemy(xpos, ypos)
            self.ems.add(s)

    def mainloop(self):
      while True:
        self.ems.update()
        self.screen.fill(self.background)
        self.ems.draw(self.screen)
        
        pygame.display.flip()



def main():
    controller = Controller()
    controller.mainloop()

main()

    
