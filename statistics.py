import numpy as np


def street_usage(cars, streets):
    for car in cars:
        for street in car.streets:
            streets[street.name].number_of_cars_uses_it += 1


def intersection_loader(intersections, streets):
    for street in streets.values():
        intersections[street.end].in_streets.append(street)
        intersections[street.begin].out_streets.append(street)


def ratio_of_streets(intersections):
    for intersection in intersections:
        summ = 0
        for street in intersection.in_streets:
            summ += street.number_of_cars_uses_it

        for index in range(len(intersection.in_street_ratios)):
            intersection.in_street_ratios[index] = summ / intersection.in_street[index]