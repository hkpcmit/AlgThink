#!/usr/bin/python

import unittest
import proj2


class BfsTest(unittest.TestCase):

    def testSingleNode(self):
        start_node = 1
        ugraph = {start_node: set()}
        self.assertEqual(set([start_node]), proj2.bfs_visited(ugraph, start_node))

    def testUgraph1(self):
        node1 = 1
        node2 = 2
        ugraph = {node1: set([node2]),
                  node2: set([node1])}
        self.assertEqual(set([node1, node2]), proj2.bfs_visited(ugraph, node1))

    def testUgraph2(self):
        node1 = 1
        node2 = 2
        node3 = 3
        ugraph = {node1: set([node2]),
                  node2: set([node1]),
                  node3: set()}
        self.assertEqual(set([node1, node2]), proj2.bfs_visited(ugraph, node1))


class ConnCompTest(unittest.TestCase):

    def testSingleNode(self):
        node1 = 1
        ugraph = {node1: set()}
        expect = [set([node1])]
        self.assertEqual(expect, proj2.cc_visited(ugraph))

    def testUgraph1(self):
        node1 = 1
        node2 = 2
        ugraph = {node1: set([node2]),
                  node2: set([node1])}
        expect = [set([node1, node2])]
        self.assertEqual(expect, proj2.cc_visited(ugraph))

    def testUgraph2(self):
        node1 = 1
        node2 = 2
        node3 = 3
        ugraph = {node1: set([node2]),
                  node2: set([node1]),
                  node3: set()}
        expect = [set([node1, node2]), set([node3])]
        self.assertEqual(expect, proj2.cc_visited(ugraph))


if __name__ == '__main__':
    unittest.main()
