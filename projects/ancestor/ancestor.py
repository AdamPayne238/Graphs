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

from util import Queue, Stack
from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    """
    Write a function that, given the dataset and the ID of an individual in the dataset,
    returns their earliest known ancestor – the one at the farthest distance from the input
    individual. If there is more than one ancestor tied for "earliest", return the one with
    the lowest numeric ID. If the input individual has no parents, the function should return -1.

    :param ancestors:
    :param starting_node:
    :return:
    """

    pass