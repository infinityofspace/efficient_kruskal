from collections import defaultdict
from typing import Any


class Graph:

    def __init__(self, adjacency_dict=None, edges=None, nodes=None):
        if adjacency_dict is None:
            adjacency_dict = defaultdict(dict)
        self._adjacency_dict = adjacency_dict

        if edges is None:
            edges = []
        self._edges = edges

        if nodes is None:
            nodes = set()
        self._nodes = nodes

    def add_edge(self, first_node: Any, second_node: Any, weight: Any):
        """

        :param first_node:
        :param second_node:
        :param weight:
        :return:
        """

        self._adjacency_dict[first_node][second_node] = weight
        self._adjacency_dict[second_node][first_node] = weight

        self._edges.append([first_node, second_node, weight])

        self._nodes.add(first_node)
        self._nodes.add(second_node)

    def remove_edge(self, first_node: Any, second_node: Any):
        del self._adjacency_dict[first_node][second_node]
        del self._adjacency_dict[second_node][first_node]

    @property
    def adjacency_dict(self):
        return self._adjacency_dict

    @property
    def edges(self):
        return self._edges

    @property
    def nodes(self):
        return self._nodes

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

    def __search_circle__(self, node, parent_node, visited_nodes):
        if node not in visited_nodes:
            visited_nodes.add(node)

            for child_node in self._adjacency_dict[node]:
                if child_node != parent_node:
                    if self.__search_circle__(child_node, node, visited_nodes):
                        return True

            return False
        else:
            return True

    def contains_circle(self) -> bool:
        visited_nodes = set()

        for node in self:
            if node not in visited_nodes:
                if self.__search_circle__(node, None, visited_nodes):
                    return True

        return False

    def __str__(self):
        output = ""

        printed_edges = set()

        for node in self:
            for child_node, weight in self._adjacency_dict[node].items():
                if (node, child_node) not in printed_edges and (child_node, node) not in printed_edges:
                    output += "{} {} {}\n".format(node, child_node, weight)
                    printed_edges.add((node, child_node))

        return output
