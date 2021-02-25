import numpy as np
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
