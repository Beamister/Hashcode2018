import numpy as np

class TheMatrix:
    cars = 0
    rides = 0
    matrix = np.zeros((0,0))

    def __init__(self, cars, rides):
        self.cars = cars
        self.rides = rides
        self.matrix = np.zeros((cars,rides))

    def returnLargest(self):
        maxIndex = np.argmax(self.matrix)
        carI = abs(maxIndex / self.rides)
        rideI = maxIndex % self.rides

        # set all values for ride and car to 0
        self.matrix[carI][:] = 0
        self.matrix[:][rideI] = 0

        # return tuple of car index and ride index
        return carI,rideI

    # set value of (carI,rideI) in matrix to value
    def setValue(self, carI, rideI, value):
        self.matrix[carI][rideI] = value
    