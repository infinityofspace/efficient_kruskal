from efficient_kruskal.util import Graph
from efficient_kruskal.util.sort import quick_sort


class DisjointSet:

    def __init__(self, item):
        """
        Initialise a new disjoint set with a single item.

        :param item: the item in the disjoint set
        """

        self.item = item
        self.parent = self
        self.size = 1

    def find(self):
        """
        Find the parent of the set.

        :return: parent for this set
        """

        i = self

        while i.parent != i:
            i.parent = i.parent.parent
            i = i.parent
        return i.parent

    def union(self, item):
        item_1 = self.find()
        item_2 = item.find()

        if item_1 == item_2:
            return

        if item_1.size < item_2.size:
            item_1.parent = item_2
            item_2.size += item_1.size
        else:
            item_2.parent = item_1
            item_1.size += item_2.size


def kruskal_slow(graph: Graph):
    min_span_tree = Graph()

    edges = graph.edges
    quick_sort(edges)

    for i in range(len(edges)):
        edge = edges[i]

        min_span_tree.add_edge(*edge)

        if min_span_tree.contains_circle():
            min_span_tree.remove_edge(edge[0], edge[1])

    return min_span_tree


def kruskal(graph: Graph):
    min_span_tree = Graph()

    edges = graph.edges
    quick_sort(edges)

    disjoint_sets = {}

    for i in range(len(edges)):
        edge = edges[i]
        node_1, node_2, _ = edge

        node_1_disjoint_set = disjoint_sets.setdefault(node_1, DisjointSet(node_1))
        node_2_disjoint_set = disjoint_sets.setdefault(node_2, DisjointSet(node_2))

        p_1 = node_1_disjoint_set.find()
        p_2 = node_2_disjoint_set.find()

        if p_1 != p_2:
            node_1_disjoint_set.union(node_2_disjoint_set)
            min_span_tree.add_edge(*edge)

    return min_span_tree
