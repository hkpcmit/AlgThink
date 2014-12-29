#!/usr/bin/python

import App2
import collections
import matplotlib.pyplot as plt
import time


INITIAL_NODES = 5


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def fast_targeted_order(ugraph):
    graph = copy_graph(ugraph)
    degree_sets = collections.defaultdict(set)
    for node in graph:
        degree = len(graph[node])
        degree_sets[degree].add(node)
    result = []
    for degree in xrange(len(graph) - 1, -1, -1):
        while degree_sets[degree]:
            node = degree_sets[degree].pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                neighbor_degree = len(graph[neighbor])
                degree_sets[neighbor_degree].remove(neighbor)
                degree_sets[neighbor_degree-1].add(neighbor)
                graph[neighbor].remove(node)
            result.append(node)
            graph.pop(node)
    return result


def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def main():
    xvals = range(10, 1000, 10)
    yvals_to = []
    yvals_fto = []
    for n in xvals:
        upa_graph = App2.make_upa_graph(INITIAL_NODES, n)
        start_time = time.time()
        to = targeted_order(upa_graph)
        yvals_to.append(time.time() - start_time)
        start_time = time.time()
        fto = fast_targeted_order(upa_graph)
        yvals_fto.append(time.time() - start_time)
    plt.plot(xvals, yvals_to, '-b', label='targeted_order')
    plt.plot(xvals, yvals_fto, '-r', label='fast_targeted_order')
    plt.legend(loc='upper right')
    plt.ylabel('Running Time (sec.)')
    plt.xlabel('Number of Nodes')
    plt.title('Comparison Of Running Times Of\ntargeted_order vs fast_targeted_order\n'
              'Using Desktop Python')
    plt.show()
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
