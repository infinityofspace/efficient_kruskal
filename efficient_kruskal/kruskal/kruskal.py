from efficient_kruskal.util import Graph


def kruskal(graph: Graph, min=True):
    min_span_tree = Graph()

    edges = sorted(graph.edges, key=lambda edge: edge[2], reverse=not min)

    # edges = graph.edges
    # quick_sort(edges, 0, len(edges) - 1)

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


def quick_sort(l, left: int, right: int):
    if len(l) == 1:
        return l

    if left < right:
        split_idx = split(l, left, right)
        quick_sort(l, left, split_idx - 1)
        quick_sort(l, split_idx + 1, right)
