from efficient_kruskal.kruskal.kruskal import kruskal, kruskal_slow
from efficient_kruskal.util import Graph


def main():
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 3)
    g.add_edge("A", "F", 2)
    g.add_edge("B", "D", 1)
    g.add_edge("B", "E", 7)
    g.add_edge("D", "C", 3)
    g.add_edge("C", "G", 5)
    g.add_edge("G", "E", 1)

    print("connected: {}".format(g.connected()))

    min_span_tree = kruskal(g)

    print(min_span_tree)


if __name__ == '__main__':
    main()
