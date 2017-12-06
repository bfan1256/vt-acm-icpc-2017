from collections import defaultdict
from heapq import *
from itertools import chain

def dijkstra(edges, f, t):
    '''implementation of dijkstra's algorithm utilizing heapq'''
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, f, ())], set()
    while q: # while q exists
        print('Before Pop Q: {0}'.format(q))
        (cost, v1, path) = heappop(q) # gets last value in heap
        print('After Pop Q: {0}'.format(q))
        print('Popped Data: {0}'.format((cost, v1, path)))
        if v1 not in seen:
            seen.add(v1)
            path = (v1, list(chain(*path)))
            if v1 == t:
                return (cost, list(chain(*path)))

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return float("inf") # return inf if no optimal path is found


if __name__ == "__main__":
    test_edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("=== Dijkstra ===")
    print(test_edges)
    print("A -> E:")
    print(dijkstra(test_edges, "A", "E"))
    # print("F -> G:")
    # print(dijkstra(test_edges, "F", "G"))
