import argparse
import random

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

    # if not g.connected():


if __name__ == '__main__':
    main()
