class Ride:
  Start = [0,0]
  End = [0,0]
  Earliest_Start = 0
  Latest_Finish = 0

  def __init__(self, name, start, end, earliest, finish):
    self.name = name
    self.Start = start
    self.End = end 
    self.Earliest_Start = earliest 
    self.Latest_Finish = finish
