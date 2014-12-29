#!/usr/bin/python

import App2
import matplotlib.pyplot as plt
import proj2


INITIAL_NODES = 2


def main():
    network_graph = App2.load_graph(App2.NETWORK_FILE)
    num_nodes, edges = App2.count_graph(network_graph)
    probability = float(edges) / num_nodes / (num_nodes - 1) 
    print 'ER probability: {}'.format(probability)
    er_graph = App2.make_er_graph(num_nodes, probability)
    upa_graph = App2.make_upa_graph(INITIAL_NODES, num_nodes)
    xvals = range(num_nodes+1)
    yvals_network = proj2.compute_resilience(network_graph, App2.random_order(network_graph))
    yvals_er = proj2.compute_resilience(er_graph, App2.random_order(er_graph))
    yvals_upa = proj2.compute_resilience(upa_graph, App2.random_order(upa_graph))
    plt.plot(xvals, yvals_network, '-b', label='Computer Network Graph')
    plt.plot(xvals, yvals_er, '-r', label='ER Graph; p = 0.02')
    plt.plot(xvals, yvals_upa, '-g', label='UPA Graph; m = 2')
    plt.legend(loc='upper right')
    plt.ylabel('Size of Largest Connected Components')
    plt.xlabel('Number of Nodes Removed')
    plt.title('Comparison Of Resiliences Of 3 Graphs')
    plt.show()
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
