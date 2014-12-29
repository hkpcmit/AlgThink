#!/usr/bin/python

import unittest
import alg_cluster
import proj3


class FastClosestPairsTest(unittest.TestCase):

    def testTwoPoints(self):
        cluster_list = [alg_cluster.Cluster(set([]), 0, 0, 1, 0),
                        alg_cluster.Cluster(set([]), 1, 0, 1, 0)]
        self.assertEqual(proj3.fast_closest_pair(cluster_list),
                         (1.0, 0, 1))

    def testData1(self):
        cluster_list = [
            alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0),
            alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0),
            alg_cluster.Cluster(set([]), 4, 0, 1, 0), alg_cluster.Cluster(set([]), 5, 0, 1, 0),
            alg_cluster.Cluster(set([]), 6, 0, 1, 0), alg_cluster.Cluster(set([]), 7, 0, 1, 0),
            alg_cluster.Cluster(set([]), 8, 0, 1, 0), alg_cluster.Cluster(set([]), 9, 0, 1, 0),
            alg_cluster.Cluster(set([]), 10, 0, 1, 0), alg_cluster.Cluster(set([]), 11, 0, 1, 0),
            alg_cluster.Cluster(set([]), 12, 0, 1, 0), alg_cluster.Cluster(set([]), 13, 0, 1, 0),
            alg_cluster.Cluster(set([]), 14, 0, 1, 0), alg_cluster.Cluster(set([]), 15, 0, 1, 0),
            alg_cluster.Cluster(set([]), 16, 0, 1, 0), alg_cluster.Cluster(set([]), 17, 0, 1, 0),
            alg_cluster.Cluster(set([]), 18, 0, 1, 0), alg_cluster.Cluster(set([]), 19, 0, 1, 0)]
        expect = set([(1.0, 9, 10), (1.0, 2, 3), (1.0, 15, 16), (1.0, 11, 12),
                      (1.0, 13, 14), (1.0, 16, 17), (1.0, 14, 15), (1.0, 12, 13),
                      (1.0, 4, 5), (1.0, 18, 19), (1.0, 3, 4), (1.0, 8, 9),
                      (1.0, 17, 18), (1.0, 6, 7), (1.0, 7, 8), (1.0, 5, 6),
                      (1.0, 10, 11), (1.0, 0, 1), (1.0, 1, 2)])
        self.assertIn(proj3.fast_closest_pair(cluster_list), expect)

    def testData2(self):
        cluster_list = [
            alg_cluster.Cluster(set([]), 90.9548590217, -17.089022585, 1, 0),
            alg_cluster.Cluster(set([]), 90.2536656675, -70.5911544718, 1, 0),
            alg_cluster.Cluster(set([]), -57.5872347006, 99.7124028905, 1, 0),
            alg_cluster.Cluster(set([]), -15.9338519877, 5.91547495626, 1, 0),
            alg_cluster.Cluster(set([]), 19.1869055492, -28.0681513017, 1, 0),
            alg_cluster.Cluster(set([]), -23.0752410653, -42.1353490324, 1, 0),
            alg_cluster.Cluster(set([]), -65.1732261872, 19.675582646, 1, 0),
            alg_cluster.Cluster(set([]), 99.7789872101, -11.2619165604, 1, 0),
            alg_cluster.Cluster(set([]), -43.3699854405, -94.7349852817, 1, 0),
            alg_cluster.Cluster(set([]), 48.2281912402, -53.3441788034, 1, 0)]
        expect = (10.5745166749, 0, 7)
        self.assertEqual(proj3.fast_closest_pair(cluster_list), expect)


if __name__ == '__main__':
    unittest.main()

