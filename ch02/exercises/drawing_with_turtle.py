import turtle
win = turtle.Screen()
chris = turtle.Turtle()

sides = int(input("How many sides?"))
length = int(input("Side Length?"))
degrees = 360
angle = (degrees)/(sides)

chris = turtle.color("red")
chris = turtle.shape("circle")

for i in range(sides):
  chris = turtle.forward(length)
  chris = turtle.left(angle)

win.exitonclick()