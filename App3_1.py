#!/usr/bin/python

import alg_cluster
import matplotlib.pyplot as plt
import proj3
import random
import time


def GetRandomClusters(num_clusters):
    return [alg_cluster.Cluster(set(),
                                random.uniform(-1, 1),
                                random.uniform(-1, 1),
                                0,
                                0)
            for _ in xrange(num_clusters)]


def main():
    random.seed(123)
    xvals = range(2, 200)
    yvals_fast, yvals_slow = [], []
    for i in xvals:
        cluster_list = GetRandomClusters(i)
        start_time = time.time()
        proj3.slow_closest_pairs(cluster_list)
        yvals_slow.append(time.time() - start_time)
        start_time = time.time()
        proj3.fast_closest_pair(cluster_list)
        yvals_fast.append(time.time() - start_time)
    plt.plot(xvals, yvals_fast, '-b', label='fast_closest_pair')
    plt.plot(xvals, yvals_slow, '-r', label='slow_closest_pairs')
    plt.legend(loc='upper right')
    plt.ylabel('Running Time (sec.)')
    plt.xlabel('Number of Initial Clusters')
    plt.title('Comparison Of Running Times Of\nfast_closest_pairs vs slow_closest_pairs\n'
              'Using Desktop Python')
    plt.show()
    import pdb; pdb.set_trace()
    


if __name__ == '__main__':
    main()
