import argparse
import random
import time

from efficient_kruskal.kruskal.kruskal import kruskal, kruskal_slow
from efficient_kruskal.util import Graph


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("nodes", type=int, help="Number of unique nodes in the graph.")
    # parser.add_argument("weights", type=int, default=5e2, help="Number of unique nodes in the graph.")

    args = parser.parse_args()

    n_nodes = args.nodes

    assert n_nodes > 0

    g = Graph()

    for _ in range(n_nodes):
        node_one = random.randint(0, n_nodes)
        node_two = random.randint(0, n_nodes)
        weight = random.randint(0, 20)
        g.add_edge(node_one, node_two, weight)

    start_time = time.time()
    kruskal(g)
    print("{:.3f}s".format(time.time() - start_time))

    start_time = time.time()
    kruskal_slow(g)
    print("{:.3f}s".format(time.time() - start_time))


if __name__ == '__main__':
    main()
