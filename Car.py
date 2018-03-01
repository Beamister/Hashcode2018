class Car:
    # Models a car's state
    curPos = {'x': None, 'y': None}
    desPos = {'x': None, 'y': None}
    hasRide = False

    def __init__(self, name):
      self.name = name

    # String output of Car for debug
    def __str__(self):
      toOutput = "\n" + self.name + " is at ("+self.x()+","+self.y()+ ") and "
      if(self.hasRide): toOutput += " has a ride."
      else: toOutput += " doesn't have a ride."
      if(self.desPos["x"] != None):
        toOutput += "\nIts headed towards ("+self.destX()+","+self.destY()+")."
      return toOutput

    def timeTo(self, x, y):
      return abs(self.x - x) + abs(self.y - y)

    def x(self):
      return self.curPos["x"]

    def y(self):
      return self.curPos["y"]

    def destX(self):
      return self.desPos["x"]

    def destY(self):
      return self.desPos["y"]      

    def setPos(self, x, y):
      self.curPos["x"] = x
      self.curPos["y"] = y

    def setDest(self, x, y):
      self.desPos["x"] = x
      self.desPos["y"] = y