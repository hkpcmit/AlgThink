#!/usr/bin/python

import matplotlib.pyplot as plt
import proj1
import urllib2


CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def main():
    citation_graph = load_graph(CITATION_URL)
    dist = proj1.in_degree_distribution(citation_graph)
    total = sum(dist.values())
    dist = {key: float(val)/total for key, val in dist.iteritems()}
    pairs = [(key, dist[key]) for key in sorted(dist)]
    x, y = zip(*pairs)
    plt.loglog(x, y, 'o')
    plt.ylabel('Normalized Distribution')
    plt.xlabel('In-Degrees')
    plt.title('LogLog Plot Of In-Degree Distribution For Citation Graph (Base 10)')
    plt.show()
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
