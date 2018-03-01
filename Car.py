class Car:
    # Models a car's state
    curPos = {'x': 0, 'y': 0}
    hasRide = False

    def __init__(self, name):
      self.name = name

    def timeTo(self, x, y):
      return abs(self.x - x) + abs(self.y - y)

    def x(self):
      return self.curPos["x"]

    def y(self):
      return self.curPos["y"]

    def setX(self, x):
      self.curPos["x"] = x
    
    def setY(self, y):

      self.curPos["y"] = y
