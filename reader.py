import numpy as np
import fire
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


class Car(NamedTuple):
    streets: List[Street]


class Intersection(NamedTuple):
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
            streets[name] = Street(B, E, name, L, 0)  # type: ignore
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
        for i in range(len(intersect.streets)):
            print("{} {}".format(intersect.streets[i].name,
                                 intersect.times[i]))


def main(fname: str) -> None:
    world = read_file(fname)
    sched = []
    for i in range(world.num_intersections):
        streets = []
        times = []
        for s in world.streets.values():
            if s.end == i:
                streets.append(s)
                times.append(2)
        sched.append(Schedule(i, streets, times))
    print_output(sched)


if __name__ == "__main__":
    fire.Fire({'read': read_file, 'main': main})
