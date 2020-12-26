import argparse
import random
import time

from efficient_kruskal.kruskal.kruskal import kruskal, kruskal_slow
from efficient_kruskal.util import Graph


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("nodes", type=int, help="Number of unique nodes in the graph.")

    args = parser.parse_args()

    n_nodes = args.nodes

    assert n_nodes > 0

    g = Graph()

    for _ in range(n_nodes):
        node_one = node_two = 0
        while node_one == node_two:
            node_one = random.randint(0, n_nodes)
            node_two = random.randint(0, n_nodes)
        weight = random.randint(0, 20)
        g.add_edge(node_one, node_two, weight)

    # basic test with one benchmark pass
    start_time = time.time()
    kruskal(g)
    fast_time = time.time() - start_time
    print("kruskal: {:.3f}s".format(fast_time))

    start_time = time.time()
    kruskal_slow(g)
    slow_time = time.time() - start_time
    print("slow kruskal: {:.3f}s".format(slow_time))

    print("{:.3f} times faster".format(slow_time / fast_time))


if __name__ == '__main__':
    main()
