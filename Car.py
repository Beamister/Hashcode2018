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

    # Returns the number of steps it will take to get to some location
    def timeTo(self, x, y):
      return abs(self.x - x) + abs(self.y - y)

    # Returns true if the destination matches the position
    def isAtDestination(self):
      return (self.x == self.destX) and (self.y == self.destY)
      
    # Once called, moves the Car one step towards its destination
    def updatePos(self):
      if(self.x != self.destX): 
        self.curPos["x"] = self.x+1 if (self.x < self.destX) else self.x-1
      else:
        self.curPos["y"] = self.y+1 if (self.y < self.destY) else self.y-1

    # Get x position
    def x(self):
      return self.curPos["x"]

    # Get y position
    def y(self):
      return self.curPos["y"]

    # Get destination x position
    def destX(self):
      return self.desPos["x"]

    # Get destination y position
    def destY(self):
      return self.desPos["y"]      

    # Given an x and y value, set x and y
    def setPos(self, x, y):
      self.curPos["x"] = x
      self.curPos["y"] = y

    # Given an x and y value, set x and y destination positions
    def setDest(self, x, y):
      self.desPos["x"] = x
      self.desPos["y"] = y
