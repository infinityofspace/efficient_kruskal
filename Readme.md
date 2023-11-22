## Kruskal

The Kruskal algorithm defined in the kruskal module computes the minimal spanning tree of a provided Graph object in O(|E| log |V|) time.
This implementation compares the efficiency (runtime) of the algorithm in different implementation variants. For the results consider 
the [Benchmark](#benchmark) section.

### Usage:

Go into the project directory (the directory which contains this Readme file). You can run the different example with
the following command:

```commandline
python -m efficient_kruskal.examples.<the-example-name>
```

Replace the <the-example-name> the specific name.

For example, to start the graph_1 example the run command is:

```commandline
python -m efficient_kruskal.examples.graph_1
```

### Modules:

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

## Benchmark

You can test the performance of different sort and data structure implementations with the graph_random.py script.
The script allows you to generate a random graph and perform several performance benchmarks.

Example benchmark with 100 runs and 500 nodes:
```commandline
python -m efficient_kruskal.examples.graph_random --nodes 500 --runs 100
```

All options:
```commandline
python -m efficient_kruskal.examples.graph_random --help
```

```commandline
usage: graph_random.py [-h] [--nodes NODES] [--save SAVE] [--graph GRAPH] [--format FORMAT] [--seed SEED] [--runs RUNS]

options:
  -h, --help            show this help message and exit
  --nodes NODES, -n NODES
                        Number of unique nodes in the graph.
  --save SAVE, -s SAVE  Store the random generated graph to the provided file path.
  --graph GRAPH, -g GRAPH
                        Load the graph from the provided file path.
  --format FORMAT, -f FORMAT
                        Number of digits formatted duration logging.
  --seed SEED           Seed to use for random init
  --runs RUNS, -r RUNS  Number of runs
```

You can find some results in the `results_*.txt` files calculate on an 6 core 3.8GHz CPU.

## License

[MIT](License) - Copyright (c) 2023 Marvin Heptner
