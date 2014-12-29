#!/usr/bin/python

import proj1
import proj2
import random


INITIAL_NODES = 2
NETWORK_FILE = 'alg_rf7.txt'


random.seed(123)


class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def count_graph(graph):
    edges = 0
    for node, neighbors in graph.iteritems():
        for neighbor in neighbors:
            if node < neighbor:
                edges += 1
    return len(graph), edges


def load_graph(graph_file):
    graph = {}
    with open(graph_file, 'r') as fd:
        for line in fd:
            line = line.strip()
            neighbors = line.split(' ')
            neighbors = [int(neighbor) for neighbor in neighbors]
            graph[neighbors[0]] = set(neighbors[1:])
    return graph


def make_er_graph(num_nodes, probability):
    graph = {node: set() for node in xrange(num_nodes)}
    for node in xrange(num_nodes):
        for neighbor in xrange(num_nodes):
            if node == neighbor:
                continue
            if random.random() < probability:
                graph[node].add(neighbor)
                graph[neighbor].add(node)
    return graph


def make_upa_graph(initial_nodes, num_nodes):
    graph = proj1.make_complete_graph(initial_nodes)
    trial = UPATrial(initial_nodes)
    graph.update({node: set() for node in xrange(initial_nodes, num_nodes)})
    for i in xrange(initial_nodes, num_nodes):
        new_neighbors = trial.run_trial(initial_nodes)
        graph[i] = new_neighbors
        for neighbor in new_neighbors:
            graph[neighbor].add(i)
    return graph


def random_order(graph):
    order = graph.keys()
    random.shuffle(order)
    return order


def main():
    network_graph = load_graph(NETWORK_FILE)
    num_nodes, edges = count_graph(network_graph)
    probability = float(edges) / num_nodes / (num_nodes - 1)
    er_graph = make_er_graph(num_nodes, probability)
    print 'ER graph: {}'.format(count_graph(er_graph))
    upa_graph = make_upa_graph(INITIAL_NODES, num_nodes)


if __name__ == '__main__':
    main()

