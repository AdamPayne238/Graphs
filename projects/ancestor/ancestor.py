# Clarifications:

# The input will not be empty.
# There are no cycles in the input.
# There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# IDs will always be positive integers.
# A parent may have any number of children.

"""
Suppose we have some input data describing a graph of relationships between parents and children
over multiple generations. The data is formatted as a list of (parent, child) pairs, where each
individual is assigned a unique integer identifier.
"""

from util import Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    """
    Write a function that, given the dataset and the ID of an individual in the dataset,
    returns their earliest known ancestor – the one at the farthest distance from the input
    individual.
    If there is more than one ancestor tied for "earliest", return the one with
    the lowest numeric ID. If the input individual has no parents, the function should return -1.
    """
    print("Ancestors:", ancestors)
    print("Starting Node:", starting_node)

    # Create a graph
    ancestor_graph = Graph()
    # print(ancestor_graph)
    # Populate graph with ancestors
    for ancestor in ancestors:
        # print('Ancestor:', ancestor)
        ancestor_graph.add_vertex(ancestor[0])
        ancestor_graph.add_vertex(ancestor[1])
        ancestor_graph.add_edge(ancestor[1], ancestor[0])  # fixed by reversing ancestor[0], ancestor[1]
        # print("Graph Vertices", ancestor_graph.vertices)

    # BFS (use queue) Create a queue
    q = Queue()
    # Enqueue starting node
    q.enqueue([starting_node])

    longest_path = 1
    # earliest ancestor default to -1
    earliest_ancestor = -1

    # Loop through as long as Queue is > 0
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()
        # print("Path:", path)
        # Grab vertex from end of PATH
        last_vertex = path[-1]
        # print("Last Vertex:", last_vertex)

        # If there is more than one ancestor, return one with lowest numeric ID
        if len(path) == longest_path and last_vertex < earliest_ancestor:
            earliest_ancestor = last_vertex
            longest_path = len(path)
        if len(path) > longest_path:
            earliest_ancestor = last_vertex
            longest_path = len(path)
        neighbors = ancestor_graph.get_neighbors(last_vertex)
        for neighbor in neighbors:
            path_copy = path.copy()
            path_copy.append(neighbor)
            print(path_copy)
            q.enqueue(path_copy)

    print("Earliest Ancestor:", earliest_ancestor)
    return earliest_ancestor
