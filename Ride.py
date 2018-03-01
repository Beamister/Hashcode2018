class Ride:
    start = {'x': None, 'y': None}
    end = {'x': None, 'y': None}
    earliestStart = None
    latestFinish = None

    def __init__(self, name, startX, startY, endX, endY, earliest, finish):
        self.name = name
        self.setStart(startX, startY)
        self.setEnd(endX, endY)
        self.earliestStart = earliest
        self.latestFinish = finish

    def __str__(self):
        return ("\n"+self.name + " starts @ ("+self.startX() + ","+self.startY()
                + "), " + "\nends @ ("+self.endX() + ","+self.endY() + ") and "
                        + " must finish before " + self.latestFinish + ".")

    def distance(self):
        return abs(self.startX()-self.endX()) + abs(self.startY()-self.endY())

    def startX(self):
        return self.start["x"]

    def startY(self):
        return self.start["y"]

    def endX(self):
        return self.end["x"]

    def endY(self):
        return self.end["y"]

    def setStart(self, x, y):
        self.start["x"] = x
        self.start["y"] = y

    def setEnd(self, x, y):
        self.end["x"] = x
        self.end["y"] = y
