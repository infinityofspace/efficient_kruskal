from efficient_kruskal.util.disjointset import DisjointSet
from efficient_kruskal.util import Graph


def kruskal_slow(graph: Graph, sort_func=None) -> Graph:
    """
    Find the minimal spanning tree with the kruskal algorithm.
    The internal data structure is Graph object.

    Time complexity: O(|E| log |E|) + O(|E| * (|E| + |V|))
                     = O(|E| log |E|) + O(|E| * (|E| + |V|))
                     = O(|E| log |E| + |E| * (|E| + |V|))
                     = O(|E| log |E| + |E|^2 + |E||V|)
                     = O(|E|^2)

    :param graph: the graph to be used for the kruskal algorithm
    :param sort_func: [optional] the sort function which will be used to sort the edges. if not provided the default std
                      sort function will be used
    :return: minimal spanning tree found by kruskal algorithm
    """

    min_span_tree = Graph()

    # sort the edges in ascending order
    # Time complexity: O(|E| log |E|)
    edges = graph.edges
    if sort_func is None:
        # sorted uses Timsort (https://wiki.python.org/moin/HowTo/Sorting)
        edges = sorted(edges, key=lambda x: x[2])
    else:
        edges = sort_func(edges)

    # iterate over each edge
    for edge in edges:
        # add the edge to the minimum spanning tree
        min_span_tree.add_edge(*edge)  # O(1)

        # check if the new minimum spanning tree contains a cycle
        if min_span_tree.contains_cycle():  # O(|V| + |E|)
            min_span_tree.remove_edge(edge[0], edge[1])  # O(1)

    return min_span_tree


def kruskal(graph: Graph, sort_func=None):
    """
    Find the minimal spanning tree with the kruskal algorithm.
    The internal data structure is a disjoint set.

    :param graph: the graph to be used for the kruskal algorithm
    :param sort_func: [optional] the sort function which will be used to sort the edges. if not provided the default std
                      sort function will be used
    :return: minimal spanning tree found by kruskal algorithm
    """

    min_span_tree = Graph()

    # sort the edges in ascending order
    edges = graph.edges
    if sort_func is None:
        # sorted uses Timsort (https://wiki.python.org/moin/HowTo/Sorting)
        edges = sorted(edges, key=lambda x: x[2])
    else:
        edges = sort_func(edges)

    disjoint_sets = {}

    # initialize the disjoint set for each node
    for node in graph.nodes:
        disjoint_sets[node] = DisjointSet(node)

    # iterate over all sorted edges
    for i in range(len(edges)):
        edge = edges[i]
        node_1, node_2, _ = edge

        node_1_set = disjoint_sets[node_1]
        node_2_set = disjoint_sets[node_2]

        # find the representative of each node of the edge
        # if they are different, the graph with this edge contains no cycle
        if node_1_set.find() != node_2_set.find():
            # unite both disjoint sets
            node_1_set.union(node_2_set)

            # add edge to Graph object
            min_span_tree.add_edge(*edge)

    return min_span_tree
