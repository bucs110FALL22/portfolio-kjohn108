import pygame
import random

class Snowman(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.color = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]
        self.speed = 5
        #makes background transparent pygame.SRCALPHA
        self.image = pygame.Surface( (40, 70) , pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        # Draw the snowman on the model surface
        
        head_radius = 5
        head = pygame.draw.circle(self.image, self.color, (self.rect.width/2, head_radius), head_radius)
        
        body_radius = 10
        body = pygame.draw.circle(self.image, self.color, (self.rect.width/2, head.bottom+body_radius), body_radius)
        
        bottom_radius = 20
        bottom = pygame.draw.circle(self.image, self.color, (self.rect.width/2, body.bottom+bottom_radius), bottom_radius)
 
    def update(self):
        """
        We can have an update method to call for updates that should happen every frame
        This often contains the movement updates for the AI/NPC objects
        """
        size = pygame.display.get_window_size()
        
        if self.rect.y <  10:
            self.direction = "DOWN"
        elif self.rect.bottom > size[1]:
            self.direction = "UP"
        if self.direction == "UP":
            self.rect.y = self.rect.y - 1 
        else:
            self.rect.y = self.rect.y + 1

        if self.rect.x < 0:
            self.rect.x += random.randint(0, self.speed)
        elif self.rect.right > size[0] :
            self.rect.x += random.randint(-self.speed, 0)
        else:
            self.rect.x += random.randint(-self.speed, self.speed)
            
            
# Controller
class Controller:

    def __init__(self):
        # we need to setup all our data for our program
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = "Orange"

        number_of_snowpeople = 3
        size = pygame.display.get_window_size() #(w,h)
        width = size[0] / number_of_snowpeople

        self.snowpeoples = pygame.sprite.Group()
        xpos = 0
        for i in range(number_of_snowpeople):
            s = Snowman(xpos, 0)
            self.snowpeoples.add(s)
            xpos += width

        

    def mainloop(self):
        while True: #one time through this loop is one picture frame
            #1. respond to events, but no events - no event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                        #reset the screen
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #respond to mouse
                    for s in self.snowpeoples:
                        if s.rect.collidepoint(event.pos):
                            s.kill()

            #2. Update Models not based on events
            for s in self.snowpeoples:
                result = pygame.sprite.spritecollide(s, self.snowpeoples, False)
                if len(result) > 1 and len(self.snowpeoples) < 20:
                    self.snowpeoples.add(Snowman(s.rect.x, s.rect.y))
                
            self.snowpeoples.update()


            # 3. Redraw the display
            self.screen.fill(self.background)

            self.snowpeoples.draw(self.screen)

            # 4. Display the updated frame
                
            pygame.display.flip()
            
            


def main():
    controller = Controller()
    controller.mainloop()

main()