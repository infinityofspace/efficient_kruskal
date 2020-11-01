from efficient_kruskal.util import Graph


def kruskal(graph: Graph, min=True):
    min_span_tree = Graph()

    edges = graph.edges
    quick_sort(edges)

    for i in range(len(edges)):
        edge = edges[i]

        min_span_tree.add_edge(*edge)

        if min_span_tree.contains_circle():
            min_span_tree.remove_edge(edge[0], edge[1])

    return min_span_tree


def split(l, left, right):
    i = left
    piv = l[right][2]

    for j in range(left, right):
        if l[j][2] < piv:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1

    temp = l[i]
    l[i] = l[right]
    l[right] = temp

    return i


def quick_sort(l, left: int = None, right: int = None):
    if left is None:
        left = 0

    if right is None:
        right = len(l) - 1

    if len(l) == 1:
        return l

    if left < right:
        split_idx = split(l, left, right)
        quick_sort(l, left, split_idx - 1)
        quick_sort(l, split_idx + 1, right)
