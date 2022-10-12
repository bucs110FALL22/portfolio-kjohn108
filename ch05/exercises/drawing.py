import turtle

window = turtle.Screen()
window.bgcolor('lightblue')



def drawEqShape(kyle, num_sides, side_length):
  angle = (360 / num_sides)
  for i in range(num_sides):
      kyle.forward(side_length)
      kyle.right(angle)


kyle = turtle.Turtle()
kyle.color('blue')
kyle.shape('turtle')
num_sides = int(input("how many sides?"))
side_length = int(input("how long?"))

drawEqShape(kyle, num_sides, side_length)

window.exitonclick()
