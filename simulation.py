#!/usr/bin/env python3

import io
import sys
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
        self.rides = rides

    def __str__(self):
        return (self.__class__.__name__ + ':\n' +
                "grid: " + str(self.grid) +
                "\nbonus: " + str(self.bonus) +
                "\n# of steps: " + str(self.num_of_steps) +
                "\nvehicles: " + str(self.vehicles) +
                "\nrides: " + str(self.rides))

    def assignments(self):
        print("Make assignments of cars to rides")

    def calculatepoints(self, car, ride):
        print("Calculate those pointy bois")


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


def main():
    print(Simulation.from_file(sys.argv[1]))
    #Time loop here

if __name__ == '__main__':
    main()
