from collections import defaultdict
from typing import Any


class Graph:

    def __init__(self, adjacency_dict=None, edges=None):
        if adjacency_dict is None:
            adjacency_dict = defaultdict(dict)
        self._adjacency_dict = adjacency_dict

        if edges is None:
            edges = []
        self._edges = edges

    def add_edge(self, first_node: Any, second_node: Any, weight: Any):
        """
        https://wiki.python.org/moin/TimeComplexity

        :param first_node:
        :param second_node:
        :param weight:
        :return:
        """

        self._adjacency_dict[first_node][second_node] = weight
        self._adjacency_dict[second_node][first_node] = weight

        self._edges.append([first_node, second_node, weight])

    def remove_edge(self, first_node: Any, second_node: Any):
        del self._adjacency_dict[first_node][second_node]
        del self._adjacency_dict[second_node][first_node]

    @property
    def adjacency_dict(self):
        return self._adjacency_dict

    @property
    def edges(self):
        return self._edges

    def add_node(self, node: Any):
        self._adjacency_dict[node] = {}

    def __iter__(self):
        return iter(self._adjacency_dict)

    def connected(self) -> bool:

        visited_nodes = set()

        self.__traverse_nodes__(next(iter(self)), visited_nodes)
        if len(visited_nodes) == len(self._adjacency_dict):
            return True
        else:
            return False

    def __traverse_nodes__(self, node, visited_nodes):
        if node not in visited_nodes:
            visited_nodes.add(node)

            for child_node in self._adjacency_dict[node]:
                self.__traverse_nodes__(child_node, visited_nodes)

    def __traverse_edges__(self, node, parent_node, visited_nodes) -> bool:
        if node not in visited_nodes:
            visited_nodes.add(node)

            for child_node in self._adjacency_dict[node]:
                if child_node != parent_node:
                    if self.__traverse_edges__(child_node, node, visited_nodes):
                        return True

            return False
        else:
            return True

    def contains_circle(self) -> bool:
        visited_nodes = set()

        node = next(iter(self))

        if node is None:
            return False

        return self.__traverse_edges__(node, None, visited_nodes)

    def __str__(self):
        output = ""

        printed_edges = set()

        for node in self:
            for child_node, weight in self._adjacency_dict[node].items():
                if (node, child_node) not in printed_edges and (child_node, node) not in printed_edges:
                    output += "{} {} {}\n".format(node, child_node, weight)
                    printed_edges.add((node, child_node))

        return output
