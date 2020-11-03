from efficient_kruskal.kruskal.kruskal import kruskal
from efficient_kruskal.util import Graph


def main():
    g = Graph()

    # first subgraph
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 2)
    g.add_edge("A", "D", 3)
    g.add_edge("B", "D", 1)

    # second subgraph
    g.add_edge("E", "F", 1)
    g.add_edge("F", "G", 5)
    g.add_edge("F", "H", 2)
    g.add_edge("H", "I", 3)
    g.add_edge("H", "E", 4)
    g.add_edge("I", "G", 1)

    print("connected: {}".format(g.connected()))

    min_span_tree = kruskal(g)

    print(min_span_tree)


if __name__ == '__main__':
    main()
