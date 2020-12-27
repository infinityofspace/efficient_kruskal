from efficient_kruskal.disjointset.disjointset import DisjointSet
from efficient_kruskal.util import Graph


def kruskal_slow(graph: Graph, sort_func=None) -> Graph:
    """
    Find the minimal spanning tree with the kruskal algorithm.
    The internal data structure is Graph object.

    :param graph: the graph to be used for the kruskal algorithm
    :param sort_func: [optional] the sort function which will be used to sort the edges. if not provided the default std
                      sort function will be used
    :return: minimal spanning tree found by kruskal algorithm
    """

    min_span_tree = Graph()

    edges = graph.edges
    if sort_func is None:
        # sorted uses Timsort (https://wiki.python.org/moin/HowTo/Sorting)
        edges = sorted(edges)
    else:
        edges = sort_func(edges)

    for edge in edges:
        min_span_tree.add_edge(*edge)

        if min_span_tree.contains_circle():
            min_span_tree.remove_edge(edge[0], edge[1])

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

    edges = graph.edges
    if sort_func is None:
        # sorted uses Timsort (https://wiki.python.org/moin/HowTo/Sorting)
        edges = sorted(edges)
    else:
        edges = sort_func(edges)

    disjoint_sets = {}

    for node in graph.nodes:
        disjoint_sets[node] = DisjointSet(node)

    for i in range(len(edges)):
        edge = edges[i]
        node_1, node_2, _ = edge

        node_1_set = disjoint_sets[node_1]
        node_2_set = disjoint_sets[node_2]

        if node_1_set.find() != node_2_set.find():
            node_1_set.union(node_2_set)

            # add edge to Graph object
            min_span_tree.add_edge(*edge)

    return min_span_tree
