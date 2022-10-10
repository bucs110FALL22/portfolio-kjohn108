def star_pyramid():
  print("pick a number")
  num = int(input(":"))
  
  star = 1
  
  for i in range(num):
    print ("*"*star)
    star = star+1

def rstar_pyramid():
  print("pick a number")
  num = int(input(":"))
  
  for i in range(num):
    print("*"*num)
    num = num-1

star_pyramid()