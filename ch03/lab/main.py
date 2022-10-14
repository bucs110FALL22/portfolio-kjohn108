import turtle #1. import modules
import random
import pygame
import math 

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
pygame.time.wait(500)

## 5. Your PART A code goes here

#method 1
michelangelo.forward(random.randrange(0,100))
leonardo.forward(random.randrange(0,100))

pygame.time.wait(2000)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#method 2
for i in range(10): 
  leonardo.forward(random.randrange(0,10))
  michelangelo.forward(random.randrange(0,10))
pygame.time.wait(2000)


# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
pygame.display.flip()
pygame.time.wait(500)
#triangle
coords = []
num_sides = 3
side_length = 100
offset = 150
for i in range(num_sides):
  theta = 2.0*math.pi * i /num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
pygame.time.wait(2000)
window.fill('black')

#square
coords = []
num_sides = 4
for i in range(num_sides):
  theta = 2.0*math.pi * i /num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
pygame.time.wait(2000)
window.fill('black')

#hexagon
coords = []
num_sides = 6
for i in range(num_sides):
  theta = 2.0*math.pi * i /num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
pygame.time.wait(2000)
window.fill('black')

#nonagon
coords = []
num_sides = 9
for i in range(num_sides):
  theta = 2.0*math.pi * i /num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
pygame.time.wait(2000)
window.fill('black')

#circle
coords = []
num_sides = 260
for i in range(num_sides):
  theta = 2.0*math.pi * i /num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
pygame.time.wait(2000)
window.fill('black')










