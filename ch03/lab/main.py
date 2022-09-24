import turtle #1. import modules
import random
import pygame
import math 
pygame.init()

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

## 5. Your PART A code goes here
for i in range(10): 
  leonardo.forward(random.randrange(0,10))
  michelangelo.forward(random.randrange(0,10))
pygame.time.wait(2000)
# PART B - complete part B here

window = pygame.display.set_mode()
pygame.Color((0,0,255))
for i in range(5):
  coords = []
  num_sides = int(input("how many sides?"))
  sidelength = int(input("how long are the sides?"))
  offset = int(input("how far from top corner?"))
  theta = (2.0 * math.pi * i) / num_sides
  
  for a in range(num_sides):
    theta = (2.0 * math.pi * i) / num_sides
    x = sidelength * math.cos(theta) + offset
    y = sidelength * math.sin(theta) + offset
    coords.append([x,y])
  pygame.draw.polygon
shape= pygame.draw.polygon(window, "white", [coords])
print(shape)
pygame.display.flip()
pygame.time.wait(500)
window.fill



window.exitonclick()
