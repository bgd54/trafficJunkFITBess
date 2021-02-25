#!python3

import json
import numpy as np
import fire

from reader import read_file, print_output, Schedule
from statistics import route_length_stats

def main(fname: str) -> None:
    world = read_file(fname)
    sched = []
    for intersection in world.intersections:
        streets = []
        times = []
        period = len(intersection.in_streets)
        for (s, r) in zip(intersection.in_streets,
                          intersection.in_street_ratios):
            streets.append(s)
            times.append(max(1, int(np.round(period * r))))
        sched.append(Schedule(intersection.id, streets, times))
    print_output(sched)

def stat(fname: str) -> None:
    world = read_file(fname)
    stats = route_length_stats(world)
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    fire.Fire({'read': read_file, 'main': main, 'stat': stat})
