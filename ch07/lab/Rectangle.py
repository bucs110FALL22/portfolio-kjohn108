class Rectangle:
  def __init__(self, x=0, y=0, height = 0, width = 0):
    self.x = x
    if self.x < 0:
      self.x = 0
    self.y = y
    if self.y < 0:
      self.y = 0
    self.height = height
    if self.height < 0:
      self.height = 0
    self.width = width
    if self.width < 0:
      self.width = 0

  def __str__(self):
    return str("x =",self.x, "y =", self.y,"Height =",self.height, "Width =",self.width)
