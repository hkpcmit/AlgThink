"""Algorithm Thinking: Project 2."""

from collections import deque
import copy


def bfs_visited(ugraph, start_node):
    """Return set of nodes visited from start_node."""
    visited = set([start_node])
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def cc_visited(ugraph):
    """Return list of set of connected components."""
    remain = set(ugraph.keys())
    conn_comp = []
    while remain:
        node = remain.pop()
        visited = bfs_visited(ugraph, node)
        conn_comp.append(visited)
        remain = remain.difference(visited)
    return conn_comp


def largest_cc_size(ugraph):
    """Return size of largest connected connected components."""
    if not ugraph:
        return 0
    return max(len(cc) for cc in cc_visited(ugraph))


def remove_node_from_graph(ugraph, node):
    """Remove the given node from the graph."""
    neighbors = ugraph[node]
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    ugraph.pop(node)
    return ugraph


def compute_resilience(ugraph, attack_order):
    """Return resilience of the graph."""
    graph = copy.deepcopy(ugraph)
    result = [largest_cc_size(graph)]
    for node in attack_order:
        graph = remove_node_from_graph(graph, node)
        result.append(largest_cc_size(graph))
    return result
