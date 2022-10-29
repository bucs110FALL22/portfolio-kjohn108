import turtle

window = turtle.Screen()
window.bgcolor('white')
turt = turtle.Turtle()
turt.ht()
radius = 50 

def head(radius=0):    
  turt.color("black", "bisque")
  turt.begin_fill()
  turt.circle(radius)
  turt.end_fill()

def beard(radius=0):
  beard_angle = 80
  turt.circle(radius,beard_angle)
  turt.color("black","grey")
  turt.begin_fill()
  turt.right(180)
  turt.circle(-1*radius,2*beard_angle)
  turt.end_fill()

def mouth(radius=0):
  dis_a = radius // 2.5
  dis_b = radius // 4.5
  turn_angle = 60
  turt.up()
  turt.seth(0)
  turt.forward(dis_a)
  turt.right(turn_angle)
  turt.forward(dis_b)
  turt.down()
  turt.color('black','pink')
  turt.begin_fill()
  turt.circle(radius//2, 2*turn_angle)
  turt.end_fill()

def size(radius=0): 
  len_size = radius//3
  return(len_size)

def lense(radius=0):    
  len_size = size(radius) #used return value from another function
  turn_angle = 90
  turt.left(turn_angle)
  turt.forward(len_size)
  for i in range(3):
    turt.right(turn_angle)
    turt.forward(len_size) 
  turt.right(2*turn_angle)
  turt.forward(2*len_size)
  
def label(message): # function takes a parameter
  turt.up()
  turt.setpos(0,-40)
  turt.write(message, move=False, align="center", font=("Comic Sans", 12,"normal")) 

def main(radius=0):
  head(radius)
  beard(radius)
  mouth(radius)
  
  turt.up()
  turt.forward(radius)
  turt.down()
  turt.seth(180)
  turt.forward(radius//3)
  
  lense(radius)
  lense(radius)
  label("Prof Moore")

main(radius)




window.exitonclick()

