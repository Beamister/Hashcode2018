#!/usr/bin/env python3

import io
import sys
import Ride


class Grid:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return (self.__class__.__name__ +
                '(' + str(self.r) + ', ' + str(self.c) + ')')


class Simulation:
    def __init__(self, grid, num_of_vehicles, bonus, num_of_steps, rides):
        self.grid = grid
        self.num_of_vehicles = num_of_vehicles
        self.bonus = bonus
        self.num_of_steps = num_of_steps
        self.rides = rides

    def __str__(self):
        return (self.__class__.__name__ + '(' +
                str(self.grid) + ', ' +
                str(self.num_of_vehicles) + ', ' +
                str(self.bonus) + ', ' +
                str(self.num_of_steps) + ', ' +
                str(self.rides) + ')')

    @staticmethod
    def fromFile(filepath):
        with io.open(filepath) as f:
            # Get simulation metadata
            meta = list(map(int, f.readline().split(' ')))
            grid = Grid(meta[0], meta[1])
            num_of_vehicles = meta[2]
            num_of_rides = meta[3]
            bonus = meta[4]
            num_of_steps = meta[5]

            # Get rides
            for _ in range(0, num_of_rides):
                ride_data = list(map(int, f.readline().split(' ')))
                # TODO: make parsing rides a thing

            return Simulation(grid, num_of_vehicles, bonus, num_of_steps, [])


def main():
    print(Simulation.fromFile(sys.argv[1]))


if __name__ == '__main__':
    main()
