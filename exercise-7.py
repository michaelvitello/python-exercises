#Coordinate calculations
#Using comparison methods

class Coordinate(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def __str__(self):
    return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

  def __eq__(self):
    if self.getX() == self.getY():
      print("Coordinates are equal")
    else:
      print("Coordinates are NOT equal")

#---------------Quick test---------------#
#Creating a coordinate object to test the comparison method
#First test, equal
my_obj = Coordinate(50, 50)
my_obj.__eq__()

# SecondTest, not equal
my_obj2 = Coordinate(15, 18)
my_obj2.__eq__()
