class Rectangle:
  def __init__(self, x, y, h, w):
    #takes x, y, h, w as parameter and save them as instance variables
    self.x=max(0, x)
    self.y=max(0, y)
    self.height=max(0, h)
    self.width=max(0, w)
  def __str__(self):
    #s is a string which contains the x, y, width and height of the rectangle
    s="(x: {}, y: {}) width: {}, height: {}"
    return s.format(self.x, self.y, self.width, self.height)