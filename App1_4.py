#!/usr/bin/python

import matplotlib.pyplot as plt
import proj1
import random


INITIAL_NODES = 50
MAX_NODES = 27770


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def main():
    graph = proj1.make_complete_graph(INITIAL_NODES)
    trial = DPATrial(INITIAL_NODES)
    for i in xrange(INITIAL_NODES, MAX_NODES):
        graph[i] = trial.run_trial(i)
    dist = proj1.in_degree_distribution(graph)
    total = sum(dist.values())
    dist = {key: float(val)/total for key, val in dist.iteritems()}
    pairs = [(key, dist[key]) for key in sorted(dist)]
    x, y = zip(*pairs)
    plt.loglog(x, y, 'o')
    plt.ylabel('Normalized Distribution')
    plt.xlabel('In-Degrees')
    plt.title('LogLog Plot Of In-Degree Distribution For DPA (Base 10)')
    plt.show()
    import pdb; pdb.set_trace()



if __name__ == '__main__':
    main()
