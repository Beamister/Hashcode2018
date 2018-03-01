#/usr/bin/env python3

import io
import sys


class Grid:
    def __init__(self, r, c):
        self.r = r
        self.c = c


class Simulation:
    def __init__(self, grid, num_of_vehicles, bonus, num_of_steps, rides):
        self.grid = grid
        self.num_of_vehicles = num_of_vehicles
        self.bonus = bonus
        self.num_of_steps = num_of_steps
        self.rides = rides

    @staticmethod
    def fromFile(path):
        with io.open(sys.argv[1]) as f:
            # Get simulation metadata
            l = f.readline()
            ctrl = l.split(' ')
            grid = Grid(ctrl[0], ctrl[1])
            num_of_vehicles = ctrl[2]
            num_of_rides = ctrl[3]
            bonus = ctrl[4]
            num_of_steps = ctrl[5]

            return Simulation(grid, num_of_vehicles, bonus, num_of_steps, [])
