class Point:
  def __init__(self, x=0, y=0, color=[255, 0, 0]):
    self.x = x
    self.y = y
    if color == "green":
      print("You are a bad person")
      color = "blue"
    self.color = color

  def set_to_comp_color(self):
    red_comp = 255 - self.color[0]
    blue_comp = 255 - self.color[1]
    green_comp = 255 - self.color[2]
    self.color = [red_comp, blue_comp, green_comp]

  def halfway(self, target):
    mx = (self.x + target.x) / 2
    my = (self.y + target.y) / 2
    self.set_to_comp_color()
    return Point(mx, my, self.color)

def main():
  p1 = Point()
  print(p1.x, p1.y, p1.color)
  p1.set_to_comp_color() # == set_to_comp_color(p1)
  print(p1.x, p1.y, p1.color)
  p2 = Point(6, 6, [0,255, 0])

  p3 = p1.halfway(p2)
  print(p3.x, p3.y, p3.color)
  p4 = Point(500, 20, [150, 0, 0])
  print(p4.x, p4.y, p4.color)
  p4.set_to_comp_color()
  print(p4.x, p4.y, p4.color)
main()