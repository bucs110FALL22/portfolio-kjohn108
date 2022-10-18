import random
guessnum = 0
correctnum = random.randint(0,10)
for i in range(3):
  guessnum += 1
  guess = int(input("enter a guess"))
  if guess > correctnum:
    print("Too high")
  elif guess < correctnum: 
    print("too low")
  else:
    print("correct number")
    break
print("it took you",guessnum, "guesses to get it right!")