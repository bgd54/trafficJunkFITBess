import reader
import numpy as np


def street_usage(cars, streets):
    for car in cars:
        for street in car.streets:
            streets[street].number_of_cars_uses_it += 1


