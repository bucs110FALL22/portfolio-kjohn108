import turtle
import random

fred = turtle.Turtle()
fred.shape("turtle")
fred.color("red")
window = turtle.Screen()
fred.goto(0,0)

while fred.xcor()<=200 and fred.xcor()>= -200 and fred.ycor()<= 200 and fred.ycor()>= -200:
  num = random.randrange(1,3)

  if num == 1:
    fred.left(90)
    fred.forward(50)

  elif num == 2:
    fred.right(90)
    fred.forward(50)
break

window.exitonclick()
  