
import pygame
import random
import math

pygame.init()
size = 300

screen = pygame.display.set_mode([size,size])
pygame.display.get_window_size()

#pick a player

for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
    




pygame.draw.rect(screen,'white', (0,0,size,size))
pygame.draw.circle(screen, 'orange',(150,150),150)
pygame.draw.line(screen, 'black', (150,0),(150,300))
pygame.draw.line(screen, 'black', (0,150),(300,150))

pygame.display.flip()
pygame.time.wait(1000)
p1score = 0
p2score = 0
for i in range(10):
  
  #team 1
  x_coord1 = random.randrange(0,300)
  y_coord1 = random.randrange(0,300)
  pygame.draw.circle(screen, 'red',(x_coord1,y_coord1),5)
  distance_from_center = math.hypot(150 - x_coord1, 150 - y_coord1)
  is_in_circle = distance_from_center <= 300/2 
  
  if (is_in_circle == True):
    p1score = p1score + 1
    pygame.draw.circle(screen, 'green',(x_coord1,y_coord1),5)
    
  else:
    pygame.draw.circle(screen, 'red',(x_coord1,y_coord1),5)
  
  #team 2
  pygame.time.wait(500)
  pygame.display.flip()
  x_coord2 = random.randrange(0,300)
  y_coord2 = random.randrange(0,300)
  
  distance_from_center = math.hypot(150 - x_coord2, 150 - y_coord2)
  is_in_circle = distance_from_center <= 300/2 
  

  if (is_in_circle == True): 
    p2score = p2score + 1
    pygame.draw.circle(screen, 'blue',(x_coord2,y_coord2),5)
  else:
    pygame.draw.circle(screen, 'black',(x_coord2,y_coord2),5)
  pygame.time.wait(500)
  pygame.display.flip()
  
pygame.display.flip()
pygame.time.wait(3000)
print(p1score)
print(p2score)

