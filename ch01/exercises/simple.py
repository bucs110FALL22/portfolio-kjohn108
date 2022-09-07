print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15) #this is a rounded value so not technically correct 

rate = input("what is the conversion rate")
amount = input("how much money would you like to convert?")
rate = int(rate)
amount = int(amount)
total = rate*amount
result = total - 3
print(result)