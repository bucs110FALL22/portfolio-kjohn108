import pygame

#Part A
n = 101 
count = 0  # count variable added
while (n != 1):
  if ((n % 2) == 0):
    n = n//2
  else: 
    n = (n*3)+1
  count = count +1 

#part B  
upper_limit = 20
iters = {0:0}
start=range(2,upper_limit+1)
max_so_far = 0 

size = 250 
scale = size // upper_limit

for i in start: 
  n = i
  count = 0 
  while (n != 1):
    if ((n % 2) == 0):
      n = n//2
    else: 
      n = (n*3)+1
    count = count +1 
  iters[i*scale]= count*scale 
  if (count > max_so_far):
    max_so_far = count

print(iters)
print(max_so_far)

#Part C
pygame.init()
window = pygame.display.set_mode((size,size))
window.fill(('blue'))
scale = size / n 

coords = list(iters.items())
window.fill((0,100,0))
pygame.draw.lines(window, 'red', False,coords)
new_display = pygame.transform.flip(window, False, True)
window.blit(new_display , (0, 0))
font = pygame.font.Font(None,75)
message = font.render(str(max_so_far), True, 'black')
window.blit(message, (10,10))
pygame.display.update()
pygame.time.wait(500)


