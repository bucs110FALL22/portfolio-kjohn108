import requests

req = requests.get('http://www.google.com')
print(req.status_code)
result = req.json()


fptr = open("pra.json",'w')
fptr.write(result)
fptr.close()






































# import random
# import pygame 
# pygame.init()

# fptr = open("yes.txt")
# data = fptr.read()
# fptr.close()
# print(data, type(data))

# biggest = 0 



# for i in range(10000): 
#   rand = random.randint(0,1000000000)
#   if rand > biggest: 
#     biggest = rand
#     fptr = open("yes.txt",'w')
#     fptr.write(str(rand))
#     fptr.close()
    
#   pygame.time.wait(1)
