def multiplier(num1,num2): 
  result = 0 
  for i in range(num1):
    result = result +num2
  print(result)

def exponent(num1,num2):
  result = 1
  for i in range(num1):
    result = result *num2 
  print(result)

def square(num2):
  exponent(2,num2)


num1 = int(input("num1?"))
num2 = int(input("num2?"))
multiplier(num1,num2)
exponent(num1,num2)
square(num2)