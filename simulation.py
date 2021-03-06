#!/usr/bin/env python3

import io
import sys
from TheMatrix import TheMatrix
from Car import Car
from Ride import Ride


class Grid:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return (self.__class__.__name__ +
                '(' + str(self.r) + ', ' + str(self.c) + ')')


class Simulation:
    def __init__(self, grid, bonus, num_of_steps, rides, vehicles):
        self.grid = grid
        self.vehicles = vehicles
        self.bonus = bonus
        self.num_of_steps = num_of_steps
        self.curStep = 0
        self.rides = rides
        self.matrix = TheMatrix(len(vehicles), len(rides))

    def __str__(self):
        return (self.__class__.__name__ + ':\n' +
                "grid: " + str(self.grid) +
                "\nbonus: " + str(self.bonus) +
                "\n# of steps: " + str(self.num_of_steps) +
                "\nvehicles: " + str(self.vehicles) +
                "\nrides: " + str(self.rides))

    def moveCars(self):
        for car in self.vehicles:
            car.updatePos()

    def assignments(self):
        carI = 0
        rideI = 0
        for ride in self.rides:
            rideI += 1
            for car in self.vehicles:
                if(not car.hasRide):
                    carI += 1
                    currentPointValue = self.calculatePoints(car, ride)
                    self.matrix.setValue(carI, rideI, currentPointValue)
        for car in self.vehicles: 
            if(not car.hasRide):
                (carI, rideI) = self.matrix.returnLargest()
                self.vehicles[carI].assignRide(self.rides[rideI])

    def calculatePoints(self, car, ride):
        timeToRide = car.timeTo(ride.startX(), ride.startY())

        # if the car will arrive after finish, return -1 score
        if((timeToRide + self.curStep) > ride.latestFinish):
            return -1
        elif((timeToRide + self.curStep + ride.distance()) > ride.latestFinish):
            return -1

        score = 0

        # add bonus if car will arrive on time
        if((timeToRide + self.curStep) == ride.earliestStart):
            score += 2

        # add distance of the ride and length of ride
        score += timeToRide + ride.distance()

        # reduce score by number of steps to start of ride
        if((timeToRide + self.curStep) < ride.earliestStart):
            score -= (ride.earliestStart - (timeToRide + self.curStep))

        return score

    @staticmethod
    def from_file(filepath):
        with io.open(filepath) as f:
            # Get simulation metadata
            meta = list(map(int, f.readline().split(' ')))
            grid = Grid(meta[0], meta[1])
            num_of_vehicles = meta[2]
            num_of_rides = meta[3]
            bonus = meta[4]
            num_of_steps = meta[5]

            # Get rides
            rides = []
            for i in range(0, num_of_rides):
                ride_data = list(map(int, f.readline().split(' ')))
                x0 = ride_data[0]
                y0 = ride_data[1]
                x1 = ride_data[2]
                y1 = ride_data[3]
                earliest_start = ride_data[4]
                latest_finish = ride_data[5]
                rides.append(
                    Ride(i, x0, x1, y0, y1, earliest_start, latest_finish))

            # Get vehicles
            vehicles = []
            for i in range(0, num_of_vehicles):
                vehicles.append(Car(i))

            return Simulation(grid, bonus, num_of_steps, rides, vehicles)


def output(filepath, num_lists):
    with io.open(filepath) as f:
        f.write(str(len(num_lists)))
        for num_list in num_lists:
            for i in range(0, len(num_list) - 1):
                f.write(str(num_list[i] + ' '))
            if len(num_list) > 0:
                f.write(str(num_list[len(num_list) - 1]))
            f.write('\n')


def main():
    simulation = Simulation.from_file(sys.argv[1])
    print(simulation)
    # Time loop here
    for currentStep in range(simulation.num_of_steps):
        simulation.curStep = currentStep
        simulation.assignments()
        simulation.moveCars()
    outputList = []
    for car in simulation.vehicles:
        outputList.append(car.pastRides)
    output("Output.txt", outputList)


if __name__ == '__main__':
    main()
