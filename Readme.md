## Kruskal

The Kruskal algorithm defined in the kruskal module computes the minimal spanning tree of a provided Graph object in O(
|E| log |V|).

### Modules

The module efficient_kruskal consists of multiple modules.

#### examples

This module consists of 3 predefined graphs and an image of the graph. The Python script graph_random.py allows you to
generate a random graph and perform several performance benchmarks. It takes the number of nodes to generate in the
graph and allows you to store the generated graph or load a previous generated graph. There is also a file called
benchmark_results.txt which contains a simple overview of a benchmark with different node numbers.

#### kruskal

There are 2 different implementations for the algorithm. The first called kruskal_slow uses a simple adjacency matrix as
data structure and perform a depth first search to check if a cycle was created. The second implementation is called
kruskal and uses the disjoint data structure implemented in the util module.

#### util

This module contains the Graph object which provides some simple methods to print or add new edges. Also in this module
the mergesort algorithm is implemented. This exists in a parallel and non-parallel implementation. In addition, the
module contains the implementation of the disjoint data set.
