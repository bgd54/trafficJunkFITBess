import * from reader

class Schedule(NamedTuple):
  idx: int # intersect id
  streets: List[Street]
  times: List[int] # timing lengths
  


def print_output(schedule: List[Schedule]) -> None:
  print(len(schedule))
  for intersect in schedule:
    print(intersect.idx)
    print(len(intersect.schedule))
    for sched in intersect.schedule:
      print("{} {}".format(sched.streetname, sched.time))



def main(fname: str) -> None:
  world = read_file(fname);
  sched = []
  for i in range(world.num_intersections):
    streets = []
    times = []
    for s in world.streets:
      if s.end == i:
        streets.append(s)
        sched.append(1)
    sched.append(Schedule(i, streets, times)
  print_output(sched)


