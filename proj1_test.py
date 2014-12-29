#!/usr/bin/python

import unittest
import proj1


class ComputeInDegreesTest(unittest.TestCase):

    def testEmptyGraph(self):
        self.assertDictEqual({}, proj1.compute_in_degrees({}))

    def testGraph1(self):
        digraph = {0: set()}
        expect = {0: 0}
        self.assertDictEqual(expect, proj1.compute_in_degrees(digraph))

    def testExGraph0(self):
        expect = {0: 0, 1: 1, 2: 1}
        self.assertDictEqual(expect, proj1.compute_in_degrees(proj1.EX_GRAPH0))

    def testExGraph1(self):
        expect = {0: 1, 1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1}
        self.assertDictEqual(expect, proj1.compute_in_degrees(proj1.EX_GRAPH1))

    def testExGraph2(self):
        expect = {0: 1, 1: 3, 2: 3, 3: 3, 4: 2, 5: 2, 6: 2, 7: 3, 8: 0, 9: 0}
        self.assertDictEqual(expect, proj1.compute_in_degrees(proj1.EX_GRAPH2))


class InDegreeDistributionTest(unittest.TestCase):

    def testEmptyGraph(self):
        self.assertDictEqual({}, proj1.in_degree_distribution({}))

    def testGraph1(self):
        digraph = {0: set()}
        expect = {0: 1}
        self.assertDictEqual(expect, proj1.in_degree_distribution(digraph))

    def testExGraph0(self):
        expect = {0: 1, 1: 2}
        self.assertDictEqual(expect, proj1.in_degree_distribution(proj1.EX_GRAPH0))

    def testExGraph1(self):
        expect = {1: 5, 2: 2}
        self.assertDictEqual(expect, proj1.in_degree_distribution(proj1.EX_GRAPH1))

    def testExGraph2(self):
        expect = {0: 2, 1: 1, 2: 3, 3: 4}
        self.assertDictEqual(expect, proj1.in_degree_distribution(proj1.EX_GRAPH2))


class MakeCompleteGraphTest(unittest.TestCase):

    def testEmptyGraph(self):
        self.assertDictEqual({}, proj1.make_complete_graph(0))

    def testGraph1(self):
        expect = {0: set()}
        self.assertDictEqual(expect, proj1.make_complete_graph(1))

    def testGraph2(self):
        expect = {0: set([1]), 1: set([0])}
        self.assertDictEqual(expect, proj1.make_complete_graph(2))

    def testGraph2(self):
        expect = {0: set([1, 2]), 1: set([0, 2]), 2: set([0, 1])}
        self.assertDictEqual(expect, proj1.make_complete_graph(3))

    def testGraph3(self):
        expect = {0: set([1, 2, 3]),
                  1: set([0, 2, 3]),
                  2: set([0, 1, 3]),
                  3: set([0, 1, 2])}
        self.assertDictEqual(expect, proj1.make_complete_graph(4))


if __name__ == '__main__':
    unittest.main()
