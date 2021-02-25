#!python3

from typing import List
from queue import SimpleQueue
from reader import World, Street, Intersection, read_file


def make_graph(world: World) -> List[Intersection]:
    nodes: List[Intersection] = [
        Intersection(in_streets=[], out_streets=[])
        for i in range(world.num_intersections)
    ]

    for street in world.streets.values():
        nodes[street.end].in_streets.append(street)
        nodes[street.begin].out_streets.append(street)

    return nodes

def max_indegree(nodes: List[Intersection]) -> int:
    return max(len(node.in_streets) for node in nodes)

def has_isolated(nodes: List[Intersection]) -> bool:
    visited_intersections = set()

    Q = SimpleQueue()
    Q.put(nodes[0])

    while not Q.empty():
        next_node = Q.get()
        visited_intersections.add(next_node.id)

        for street in next_node.out_streets:
            Q.put(nodes[street.end])

    return len(visited_intersections) < len(nodes)

if __name__ == '__main__':
    world = read_file('data/a.txt')
    nodes = make_graph(world)
    print(has_isolated(nodes))

    # for name in ['a', 'b', 'c', 'd', 'e', 'f']:
    #     world = read_file('data/{}.txt'.format(name))
    #     nodes = make_graph(world)
    #     print('MaxIndegree({}) = {}'.format(name, max_indegree(nodes)))
