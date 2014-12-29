"""Algorithm Thinking: Project 1."""

from collections import Counter

EX_GRAPH0 = {
    0: set([1, 2]),
    1: set(),
    2: set(),
}
EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set(),
}
EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set(),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7]),
}


class Error(Exception):
    """Base error class."""


def compute_in_degrees(digraph):
    """Calculate in-degrees of digraph."""
    in_degrees = {node: 0 for node in digraph}
    for adj in digraph.values():
        for head in adj:
            in_degrees[head] += 1
    return in_degrees


def in_degree_distribution(digraph):
    """Return in-degree distribution of digraph."""
    dist = Counter()
    in_degrees = compute_in_degrees(digraph)
    for count in in_degrees.values():
        dist[count] += 1
    return dist


def make_complete_graph(num_nodes):
    """Return complete digraph for the given number of nodaaes."""
    if num_nodes < 0:
        raise Error('Invalid number of nodes: {}.'.format(num_nodes))
    return {i: make_graph_adj(i, num_nodes)
            for i in xrange(num_nodes)}


def make_graph_adj(node, num_nodes):
    """Return adjacency set for node i in the digraph."""
    return set(j for j in xrange(num_nodes) if j != node)
