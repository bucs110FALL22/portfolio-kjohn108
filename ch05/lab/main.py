import pygame
#Part A
n = 101 
count = 0 
while (n != 1):
  if ((n % 2) == 0):
    n = n//2
  else: 
    n = (n*3)+1
  count = count +1 

#part B + C
upper_limit = 20

iters = {}
max_so_far = 0
for i in range(2,upper_limit+1):
  count = 0 
  n = i
  while (n != 1):
    if ((n % 2) == 0):
      n = n//2
    else: 
      n = (n*3)+1
    count = count +1 
  if (count > max_so_far):
    max_so_far = count
  iters[i]=count

print(iters)
print(max_so_far)
pygame.font.init

display = pygame.display.set_mode()
coord=[]
for i in range(2,upper_limit+1):
  x = i 
  pygame.draw.lines(display, "red", False, coord)