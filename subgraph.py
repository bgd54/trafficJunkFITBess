#!python3

from typing import List
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

# def has_isolated(nodes: List[Intersection]) -> bool:
#     visited_intersections = set()
#
#     Q = nodes[0]
#
#     for neighbor in next_node.out_streets:
#
#
#     return False

if __name__ == '__main__':
    for name in ['a', 'b', 'c', 'd', 'e', 'f']:
        world = read_file('data/{}.txt'.format(name))
        nodes = make_graph(world)
        print('MaxIndegree({}) = {}'.format(name, max_indegree(nodes)))