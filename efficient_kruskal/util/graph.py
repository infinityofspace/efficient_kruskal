from collections import defaultdict
from typing import Any


class Graph:
    """
    This class represents a undirected weighted graph.
    """

    def __init__(self, adjacency_dict=None, edges=None, nodes=None) -> None:
        """
        Init a new graph.

        :param adjacency_dict: adjacency matrix as dict
        :param edges: list of edges
        :param nodes: list of nodes
        """

        if adjacency_dict is None:
            adjacency_dict = defaultdict(dict)
        self._adjacency_dict = adjacency_dict

        if edges is None:
            edges = []
        self._edges = edges

        if nodes is None:
            nodes = set()
        self._nodes = nodes

    def add_edge(self, first_node: Any, second_node: Any, weight: Any) -> None:
        """
        Add a new weighted edge to the graph.

        :param first_node: the first node of the edge
        :param second_node: the second node of the edge
        :param weight: the weight of the edge, have to be comparable
        """

        self._adjacency_dict[first_node][second_node] = weight
        self._adjacency_dict[second_node][first_node] = weight

        self._edges.append([first_node, second_node, weight])

        self._nodes.add(first_node)
        self._nodes.add(second_node)

    def remove_edge(self, first_node: Any, second_node: Any) -> None:
        """
        Remove an edge by first node and second node from edges list and adjacency_dict.

        :param first_node: first node of edge
        :param second_node: second node of edge
        """

        # remove edge from the edges list
        for e in self._edges:
            if e[0] == first_node and e[1] == second_node or e[0] == second_node and e[1] == first_node:
                self._edges.remove(e)
                break

        # remove edge from adjacency matrix
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

    def add_node(self, node: Any) -> None:
        """
        Add a new node to the graph

        :param node: the new node to be added
        """

        self._adjacency_dict[node] = {}

    def __iter__(self):
        return iter(self._adjacency_dict)

    def connected(self) -> bool:
        """
        Check if the graph is connected.

        :return: boolean if the graph is connected
        """

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
        """
        Check if the graph contains a circle

        :return: boolean if the graph contains a circle
        """

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
