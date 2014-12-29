#!/usr/bin/python

import alg_cluster
import alg_project3_viz
import matplotlib.pyplot as plt
import proj3


def main():
    data_table = alg_project3_viz.load_data_table(alg_project3_viz.DATA_111_URL)
    xvals = range(6, 21)
    yvals_hc, yvals_km = [], []
    for x in xvals:
        singleton_list = [alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4])
                          for line in data_table]
        cluster_list = proj3.hierarchical_clustering(singleton_list, x)
        distortion = sum(cluster.cluster_error(data_table) for cluster in cluster_list)
        yvals_hc.append(distortion)
        singleton_list = [alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4])
                          for line in data_table]
        cluster_list = proj3.kmeans_clustering(singleton_list, x, 5)
        distortion = sum(cluster.cluster_error(data_table) for cluster in cluster_list)
        yvals_km.append(distortion)
    plt.plot(xvals, yvals_hc, '-b', label='Hierarchical clustering')
    plt.plot(xvals, yvals_km, '-r', label='K-mean clustering (5 Iterations)')
    plt.legend(loc='upper right')
    plt.ylabel('Distortion')
    plt.xlabel('Number of Output Clusters')
    plt.title('Comparison Of Clustering Distortions On 111 Counties\n'
              'Using Desktop Python')
    plt.show()
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
