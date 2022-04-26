from Rectangle import Rectangle
class Surface:
  def __init__(self, filename, x, y, h, w):
    #it takes filename, x, y, h, w as a parameter and saves them as instance variables
    self.image=filename
    self.rect=Rectangle(x, y, h, w)
  def getRect(self):
    #getRect is a method which returns rectangle object 
    return self.rect