import argparse
import pickle
import random
import time
import statistics

from efficient_kruskal.kruskal.kruskal import kruskal, kruskal_slow
from efficient_kruskal.util import Graph
from efficient_kruskal.util.merge_sort import parallel_mergesort, mergesort


def random_int(lower, upper):
    return int(lower + (upper - lower) * random.random())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", "-n", type=int, help="Number of unique nodes in the graph.")
    parser.add_argument("--save", "-s", help="Store the random generated graph to the provided file path.")
    parser.add_argument("--graph", "-g", help="Load the graph from the provided file path.")
    parser.add_argument("--format", "-f", help="Number of digits formatted duration logging.", default=3)
    parser.add_argument("--seed", help="Seed to use for random init", default=42)
    parser.add_argument("--runs", "-r", type=int, help="Number of runs", default=1_000)

    args = parser.parse_args()

    random.seed(args.seed)

    if args.graph is None:
        g = Graph()

        n_nodes = args.nodes
        if not n_nodes:
            raise argparse.ArgumentTypeError("missing nodes, please specify number of nodes with --nodes argument")

        for _ in range(n_nodes):
            node_one = node_two = 0
            while node_one == node_two:
                node_one = random_int(0, n_nodes)
                node_two = random_int(0, n_nodes)
            weight = random_int(0, 100)
            g.add_edge(node_one, node_two, weight)
    else:
        with open(args.graph, "rb") as f:
            g = pickle.load(f)

    if args.save is not None:
        with open(args.save, "wb") as f:
            pickle.dump(g, f)

    print(f"test for {args.runs} runs")

    ###################################
    # test data structure performance #
    ###################################

    print("test data structure performance\n")

    disjoint_times = []
    for _ in range(args.runs):
        start_time = time.time()
        kruskal(g, mergesort)
        disjoint_times.append(time.time() - start_time)

    disjoint_mean = statistics.mean(disjoint_times)

    print("kruskal with disjoint set:")
    print(f"\t avg: {disjoint_mean:.{args.format}f}s")
    print(f"\t min: {min(disjoint_times):.{args.format}f}s")
    print(f"\t max: {max(disjoint_times):.{args.format}f}s")
    print(f"\t stdev: {statistics.stdev(disjoint_times):.{args.format}f}s")

    adjacency_times = []
    for _ in range(args.runs):
        start_time = time.time()
        kruskal_slow(g, mergesort)
        adjacency_times.append(time.time() - start_time)

    adjacency_mean = statistics.mean(adjacency_times)

    print(f"kruskal with adjacency matrix:")
    print(f"\t avg: {adjacency_mean:.{args.format}f}s")
    print(f"\t min: {min(adjacency_times):.{args.format}f}s")
    print(f"\t max: {max(adjacency_times):.{args.format}f}s")
    print(f"\t stdev: {statistics.stdev(adjacency_times):.{args.format}f}s")

    print()
    print(f"disjoint set is {disjoint_mean / adjacency_mean:.{args.format}f} times faster than adjacency matrix")

    ###################################
    # test sort algorithm performance #
    ###################################

    print("\n")
    print("test sort algorithm performance\n")

    mergesort_times = []
    for _ in range(args.runs):
        start_time = time.time()
        kruskal(g, mergesort)
        mergesort_times.append(time.time() - start_time)

    mergesort_mean = statistics.mean(mergesort_times)

    print(f"kruskal with mergesort:")
    print(f"\t avg: {mergesort_mean:.{args.format}f}s")
    print(f"\t min: {min(mergesort_times):.{args.format}f}s")
    print(f"\t max: {max(mergesort_times):.{args.format}f}s")
    print(f"\t stdev: {statistics.stdev(mergesort_times):.{args.format}f}s")


    parallel_mergesort_times = []
    for _ in range(args.runs):
        start_time = time.time()
        kruskal(g, parallel_mergesort)
        parallel_mergesort_times.append(time.time() - start_time)

    parallel_mergesort_mean = statistics.mean(parallel_mergesort_times)

    print(f"kruskal with parallel mergesort:")
    print(f"\t avg: {parallel_mergesort_mean:.{args.format}f}s")
    print(f"\t min: {min(parallel_mergesort_times):.{args.format}f}s")
    print(f"\t max: {max(parallel_mergesort_times):.{args.format}f}s")
    print(f"\t stdev: {statistics.stdev(parallel_mergesort_times):.{args.format}f}s")

    standard_sort_times = []
    for _ in range(args.runs):
        start_time = time.time()
        kruskal(g)
        standard_sort_times.append(time.time() - start_time)

    standard_sort__mean = statistics.mean(standard_sort_times)

    print(f"kruskal with standard sort:")
    print(f"\t avg: {standard_sort__mean:.{args.format}f}s")
    print(f"\t min: {min(standard_sort_times):.{args.format}f}s")
    print(f"\t max: {max(standard_sort_times):.{args.format}f}s")
    print(f"\t stdev: {statistics.stdev(standard_sort_times):.{args.format}f}s")

    print()
    print(f"parallel mergesort is {mergesort_mean / parallel_mergesort_mean:.{args.format}f} times faster than mergesort")
    print(f"standard sort is {parallel_mergesort_mean / standard_sort__mean:.{args.format}f} times faster than parallel mergesort")
    print(f"mergesort is {standard_sort__mean / mergesort_mean:.{args.format}f} times faster than standard sort")


if __name__ == '__main__':
    main()
