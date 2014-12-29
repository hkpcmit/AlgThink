"""
Template for Project 3
Student will implement four functions:

slow_closest_pairs(cluster_list)
fast_closest_pair(cluster_list) - implement fast_helper()
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a list of clusters in the plane
"""

import math
import alg_cluster



def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2
    
    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), idx1, idx2)


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm
    
    Returns the set of all tuples of the form (dist, idx1, idx2) 
    where the cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.   
    
    """
    min_tuple = (float('inf'), -1, -1)
    result = set([min_tuple])
    cluster_length = len(cluster_list)
    for idx1 in xrange(cluster_length):
        for idx2 in xrange(idx1+1, cluster_length):
            dist = pair_distance(cluster_list, idx1, idx2)
            if dist[0] < min_tuple[0]:
                min_tuple = dist
                result = set([dist])
            elif dist[0] == min_tuple[0]:
                result.add(dist)
    return result


def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm
    
    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """

    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))
        
        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically
        
        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters
    
        """
        
        # base case
        tot_length = len(horiz_order)
        if tot_length <= 3:
            slist = [cluster_list[idx] for idx in horiz_order]
            result = slow_closest_pairs(slist).pop()
            return (result[0], horiz_order[result[1]], horiz_order[result[2]])

        # divide
        mid_idx = tot_length / 2
        if 2 * mid_idx != tot_length:
            mid_idx += 1
        mid = (cluster_list[horiz_order[mid_idx-1]].horiz_center() +
               cluster_list[horiz_order[mid_idx]].horiz_center()) / 2.0
        horiz_l, horiz_r = horiz_order[:mid_idx], horiz_order[mid_idx:]
        horiz_l_set = set(horiz_l)
        vert_l, vert_r = [], []
        for idx in vert_order:
            if idx in horiz_l_set:
                vert_l.append(idx)
            else:
                vert_r.append(idx)
        result = min(fast_helper(cluster_list, horiz_l, vert_l),
                     fast_helper(cluster_list, horiz_r, vert_r))

        # conquer
        slist = [idx for idx in vert_order
                 if abs(cluster_list[idx].horiz_center() - mid) < result[0]]
        tot_length = len(slist)
        for idx1 in xrange(tot_length-1):
            for idx2 in xrange(idx1+1, min(idx1+4, tot_length)):
                result = min(result,
                             pair_distance(cluster_list, slist[idx1], slist[idx2]))
        return result
            
    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx) 
                        for idx in range(len(cluster_list))]    
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]
     
    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx) 
                        for idx in range(len(cluster_list))]    
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order) 
    return (answer[0], min(answer[1:]), max(answer[1:]))

    

def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list
    
    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        result = fast_closest_pair(cluster_list)
        other_cluster = cluster_list[result[2]]
        cluster_list[result[1]].merge_clusters(other_cluster)
        cluster_list.remove(other_cluster)
    return cluster_list



    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function mutates cluster_list
    
    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """
    # initialize k-means clusters to be initial clusters with largest populations
    centers = sorted(cluster_list, reverse=True,
                     key=lambda cluster: cluster.total_population()
                     )[:num_clusters]
    for _ in xrange(num_iterations):
        working_clusters = [alg_cluster.Cluster(set(), 0, 0, 0, 0)
                            for _ in xrange(num_clusters)]
        for cluster in cluster_list:
            min_dist, min_center_idx = float('inf'), -1
            # Find the min center.
            for idx, center in enumerate(centers):
                dist = fast_closest_pair([cluster, center])[0]
                if dist < min_dist:
                    min_dist, min_center_idx = dist, idx
            # Merge cluster to the working cluster for the min center.
            working_clusters[min_center_idx].merge_clusters(cluster)
        centers = working_clusters
    return working_clusters
