class DisjointSet:
    """
    This class represents a disjoint set with size parameter.
    The find method uses the path compression.
    The union method uses the size parameter.
    """

    def __init__(self, item) -> None:
        """
        Initialise a new disjoint set with a single item and size param.

        :param item: the item in the disjoint set
        """

        self.item = item
        self.parent = self
        self.size = 1

    def find(self):
        """
        Find the parent (representative) of the set and use path compression.

        :return: parent (representative) for this set
        """

        # find the parent (representative) of this set
        set_parent = self
        while set_parent.parent != set_parent:
            set_parent = set_parent.parent

        # go back the path to the initial set and set each parent to the absolute set parent (path compression)
        item = self
        while item.parent != set_parent:
            i = item.parent
            item.parent = set_parent
            item = i

        return set_parent

    def union(self, second_set) -> None:
        """
        Unite this set and the provided disjoint set by size param.

        :param second_set:
        """

        parent_1 = self.find()
        parent_2 = second_set.find()

        if parent_1 == parent_2:
            return

        if parent_1.size < parent_2.size:
            parent_1.parent = parent_2
            parent_2.size += parent_1.size
        else:
            parent_2.parent = parent_1
            parent_1.size += parent_2.size
