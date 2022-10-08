
import pygame
import random
import math

pygame.init()
size = 300

aliceblue = [0,50,0]

screen = pygame.display.set_mode([size,size])
pygame.display.get_window_size()

pygame.draw.rect(screen,'white', (0,0,300,300))
pygame.draw.circle(screen, 'orange',(150,150),150)
pygame.draw.line(screen, 'black', (150,0),(150,300))
pygame.draw.line(screen, 'black', (0,150),(300,150))

pygame.display.flip()
pygame.time.wait(1000)
p1score = 0
p2score = 0
for i in range(10):
  x_coord = random.randrange(0,300)
  y_coord = random.randrange(0,300)
  pygame.draw.circle(screen, 'red',(x_coord,y_coord),5)
  distance_from_center = math.hypot(150 - x_coord, 150 - y_coord)
  is_in_circle = distance_from_center <= 300/2 
  
  if (is_in_circle == True): 
    p1score = p1score + 1

for i in range(10):
  x_coord = random.randrange(0,300)
  y_coord = random.randrange(0,300)
  pygame.draw.circle(screen, 'blue',(x_coord,y_coord),5)
  distance_from_center = math.hypot(150 - x_coord, 150 - y_coord)
  is_in_circle = distance_from_center <= 300/2 
  
  if (is_in_circle == True): 
    p2score = p2score + 1

    
pygame.display.flip()
pygame.time.wait(3000)
print(p1score)
print(p2score)
