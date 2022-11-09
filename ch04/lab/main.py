import pygame
import random
import math

pygame.init()
size = 300

screen = pygame.display.set_mode([size,size])

print("Predict the winner by clicking a box")

#pick a player
green_choice = (0, 0, size/2, size)
blue_choice = (size/2, 0, size, size)
mouse_x, mouse_y = pygame.mouse.get_pos()
blue_box = pygame.draw.rect(screen,'blue', blue_choice)
green_box = pygame.draw.rect(screen,'green', green_choice)
chose = True

while chose == True:
  x,y = pygame.mouse.get_pos()
  blue_choice = pygame.draw.rect(screen, 'blue', blue_box)
  green_choice = pygame.draw.rect(screen, 'green', green_box)
  pygame.display.flip()
  
  for event in pygame.event.get():
   if event.type == pygame.MOUSEBUTTONDOWN:
    if blue_choice.collidepoint(x,y):
      prediction = 1
      print("you chose blue")    
      chose = False
    
    else:
      prediction = 2
      print("you chose green")
      chose = False

pygame.draw.rect(screen,'white', (0,0,size,size))
pygame.draw.circle(screen, 'orange',(150,150),150)
pygame.draw.line(screen, 'black', (150,0),(150,300))
pygame.draw.line(screen, 'black', (0,150),(300,150))

pygame.display.flip()
pygame.time.wait(1000)
green_score = 0
blue_score = 0
for i in range(10):
  
  #team 1
  x_coord1 = random.randrange(0,300)
  y_coord1 = random.randrange(0,300)
  pygame.draw.circle(screen, 'red',(x_coord1,y_coord1),5)
  distance_from_center = math.hypot(150 - x_coord1, 150 - y_coord1)
  is_in_circle = distance_from_center <= 300/2 
  
  if (is_in_circle == True):
    green_score = green_score + 1
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
    blue_score = blue_score + 1
    pygame.draw.circle(screen, 'blue',(x_coord2,y_coord2),5)
  else:
    pygame.draw.circle(screen, 'black',(x_coord2,y_coord2),5)
  pygame.time.wait(500)
  pygame.display.flip()
  
pygame.display.flip()
pygame.time.wait(3000)
print("Green had",green_score)
print("Blue had",blue_score)

if (green_score>blue_score):
  print("Green wins")
  if (prediction == 2):
    print("correct guess")
  else:
    print("wrong guess")
elif(blue_score>green_score):
  print("Blue wins")
  if (prediction == 1):
    print("correct guess")
  else:
    print("wrong guess")
elif(blue_score == green_score):
  print("Tie")