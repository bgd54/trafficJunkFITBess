import numpy as np
import fire
from typing import NamedTuple, List

class Street(NamedTuple):
    begin: int  # intersection
    end: int  # intersection
    name: str
    length: int  # duration in timesteps

class Car(NamedTuple):
    streets: List[Street]

class World(NamedTuple):
    duration: int  # duration of simulation
    num_intersections: int
    bonus_points: int  # given to every car thet reaches destination
    streets: List[Street]
    cars: List[Car]

def read_file(fname: str) -> World:
    with open(fname, 'r') as f:
        D, I, S, V, F = [int(a) for a in f.readline().strip().split()]
        streets = []
        for _ in range(S):
            B, E, name, L = f.readline().strip().split()
            B = int(B)
            E = int(E)
            L = int(L)
            streets.append(Street(B, E, name, L))
        cars = []
        for _ in range(V):
            s = f.readline().strip().split()[1:]
            cars.append(Car(s))
        return World(D, I, F, streets, cars)

if __name__ == "__main__":
    fire.Fire({'read': read_file})
