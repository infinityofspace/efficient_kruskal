import argparse
import pickle
import random
import time

from efficient_kruskal.kruskal.kruskal import kruskal, kruskal_slow
from efficient_kruskal.util import Graph
from efficient_kruskal.util.merge_sort import parallel_mergesort, mergesort


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", "-n", type=int, help="Number of unique nodes in the graph.")
    parser.add_argument("--save", "-s", help="Store the random generated graph to the provided file path.")
    parser.add_argument("--graph", "-g", help="Load the graph from the provided file path.")

    args = parser.parse_args()

    n_nodes = args.nodes

    if args.graph is None:
        g = Graph()

        for _ in range(n_nodes):
            node_one = node_two = 0
            while node_one == node_two:
                node_one = random.randint(0, n_nodes)
                node_two = random.randint(0, n_nodes)
            weight = random.randint(0, 20)
            g.add_edge(node_one, node_two, weight)
    else:
        with open(args.graph, "rb") as f:
            g = pickle.load(f)

    if args.save is not None:
        with open(args.save, "wb") as f:
            pickle.dump(g, f)

    ###################################
    # test data structure performance #
    ###################################

    start_time = time.time()
    kruskal(g, mergesort)
    fast_time = time.time() - start_time
    print("kruskal with disjoint set: {:.3f}s".format(fast_time))

    start_time = time.time()
    kruskal_slow(g, mergesort)
    slow_time = time.time() - start_time
    print("kruskal with simple graph: {:.3f}s".format(slow_time))

    print("disjoint set is {:.1f} times faster than simple graph\n".format(slow_time / fast_time))

    ###################################
    # test sort algorithm performance #
    ###################################

    start_time = time.time()
    kruskal(g, mergesort)
    mergesort_time = time.time() - start_time
    print("kruskal with mergesort: {:.3f}s".format(mergesort_time))

    start_time = time.time()
    kruskal(g, parallel_mergesort)
    parallel_mergesort_time = time.time() - start_time
    print("kruskal with parallel mergesort: {:.3f}s".format(parallel_mergesort_time))

    print("parallel mergesort is {:.1f} times faster than mergesort\n".format(mergesort_time / parallel_mergesort_time))

    start_time = time.time()
    kruskal(g)
    std_sort_time = time.time() - start_time
    print("kruskal with std sort: {:.3f}s".format(std_sort_time))

    print("std sort is {:.1f} times faster than parallel mergesort\n".format(parallel_mergesort_time / std_sort_time))


if __name__ == '__main__':
    main()
