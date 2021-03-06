import numpy as np
from statistics import street_usage, intersection_loader, ratio_of_streets
from typing import NamedTuple, List, Dict
from dataclasses import dataclass


@dataclass
class Street:
    begin: int  # intersection
    end: int  # intersection
    name: str
    length: int  # duration in timesteps
    number_of_cars_uses_it: int
    sum_idx: int


class Car(NamedTuple):
    streets: List[Street]


@dataclass
class Intersection:
    id: int
    in_street_ratios: List[float]
    in_streets: List[Street]
    out_streets: List[Street]


class World(NamedTuple):
    duration: int  # duration of simulation
    num_intersections: int
    bonus_points: int  # given to every car thet reaches destination
    streets: Dict[str, Street]
    cars: List[Car]
    intersections: List[Intersection]


def read_file(fname: str) -> World:
    with open(fname, 'r') as f:
        D, I, S, V, F = [int(a) for a in f.readline().strip().split()]
        streets: Dict[str, Street] = dict()
        for _ in range(S):
            B, E, name, L = f.readline().strip().split()
            B = int(B)  # type: ignore
            E = int(E)  # type: ignore
            L = int(L)  # type: ignore
            assert name not in streets
            streets[name] = Street(B, E, name, L, 0, 0)  # type: ignore
        cars = []
        for _ in range(V):
            s = f.readline().strip().split()[1:]
            cars.append(Car([streets[street_name] for street_name in s]))
        intersections = [Intersection(i, [], [], []) for i in range(I)]
        intersection_loader(intersections, streets)
        street_usage(cars, streets)
        ratio_of_streets(intersections)
        return World(D, I, F, streets, cars, intersections)


class Schedule(NamedTuple):
    idx: int  # intersect id
    streets: List[Street]
    times: List[int]  # timing lengths


def print_output(schedule: List[Schedule]) -> None:
    print(len(schedule))
    for intersect in schedule:
        print(intersect.idx)
        print(len(intersect.streets))
        asd = sorted(zip(intersect.streets, intersect.times),
                     key=lambda x: x[0].sum_idx)
        for a, b in asd:
            print("{} {}".format(a.name, b))
