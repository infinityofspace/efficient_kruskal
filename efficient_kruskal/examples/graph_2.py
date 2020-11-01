from efficient_kruskal.kruskal.kruskal import kruskal
from efficient_kruskal.util import Graph


def main():
    g = Graph()
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 3)
    g.add_edge("A", "E", 4)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 4)
    g.add_edge("B", "E", 3)
    g.add_edge("C", "D", 2)

    print(g.connected())

    print(g.contains_circle())

    min_span_tree = kruskal(g)

    print(min_span_tree)


if __name__ == '__main__':
    main()
