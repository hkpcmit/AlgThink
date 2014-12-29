#!/usr/bin/python

import unittest
import proj4


class BuildScoringMatrixTest(unittest.TestCase):

    def testData1(self):
        alphabet = 'ABC'
        diag_score, off_diag_score, dash_score = 10, 1, -5
        result = proj4.build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
        expect = {c: dash_score for c in alphabet + '-'}
        self.assertDictEqual(expect, result['-'])
        expect = {'A': diag_score, 'B': off_diag_score, 'C': off_diag_score, '-': dash_score}
        self.assertDictEqual(expect, result['A'])
        expect = {'A': off_diag_score, 'B': diag_score, 'C': off_diag_score, '-': dash_score}
        self.assertDictEqual(expect, result['B'])
        expect = {'A': off_diag_score, 'B': off_diag_score, 'C': diag_score, '-': dash_score}
        self.assertDictEqual(expect, result['C'])

    def testData2(self):
        alphabet = set('ACTG-')
        diag_score, off_diag_score, dash_score = 6, 2, -4
        result = proj4.build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
        expect = {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2},
                  'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2},
                  '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4},
                  'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2},
                  'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}
        self.assertDictEqual(expect, result)


class ComputeAlignmentMatrixTest(unittest.TestCase):

    def testData1(self):
        seq_x = 'AGC'
        seq_y = 'AAAC'
        diag_score, off_diag_score, dash_score = 1, -1, -2
        scoring_matrix = proj4.build_scoring_matrix(set(
                seq_x+seq_y), diag_score, off_diag_score, dash_score)
        result = proj4.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
        expect = [[0, -2, -4, -6, -8],
                  [-2, 1, -1, -3, -5],
                  [-4, -1, 0, -2, -4],
                  [-6, -3, -2, -1, -1],]
        self.assertEqual(expect, result)

    def testData2(self):
        seq_x = ''
        seq_y = ''
        diag_score, off_diag_score, dash_score = 1, -1, -2
        scoring_matrix = proj4.build_scoring_matrix(set(
                seq_x+seq_y), diag_score, off_diag_score, dash_score)
        result = proj4.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
        expect = [[0]]
        self.assertEqual(expect, result)


class ComputeGlobalAlignmentTest(unittest.TestCase):

    def testData1(self):
        seq_x = 'AGC'
        seq_y = 'AAAC'
        diag_score, off_diag_score, dash_score = 1, -1, -2
        scoring_matrix = proj4.build_scoring_matrix(set(
                seq_x+seq_y), diag_score, off_diag_score, dash_score)
        alignment_matrix = proj4.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
        result = proj4.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
        expect = set(((-1, '-AGC', seq_y), (-1, 'AG-C', seq_y)))
        self.assertIn(result, expect)

    def testData2(self):
        seq_x = 'ACTACT'
        seq_y = 'GGACTGCTTCTGG'
        scoring_matrix = {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1},
                          'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1},
                          '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0},
                          'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1},
                          'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}
        alignment_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [0, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                            [0, 1, 2, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6],
                            [0, 1, 2, 4, 4, 6, 7, 7, 7, 7, 7, 7, 7, 7],
                            [0, 1, 2, 4, 6, 6, 7, 9, 9, 9, 9, 9, 9, 9],
                            [0, 1, 2, 4, 6, 8, 8, 9, 11, 11, 11, 11, 11, 11]]
        result = proj4.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
        self.assertEqual((11, '--A---CTACT--', 'GGACTGCTTCTGG'), result)


class ComputeLocalAlignmentTest(unittest.TestCase):

    def testData1(self):
        seq_x = 'AAGA'
        seq_y = 'TTAAG'
        diag_score, off_diag_score, dash_score = 1, -1, -2
        scoring_matrix = proj4.build_scoring_matrix(set(
                seq_x+seq_y), diag_score, off_diag_score, dash_score)
        alignment_matrix = proj4.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
        result = proj4.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
        self.assertEqual((3, 'AAG', 'AAG'), result)

    def testData2(self):
        seq_x = 'A'
        seq_y = 'A'
        scoring_matrix = {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2},
                          'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2},
                          '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4},
                          'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2},
                          'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}
        alignment_matrix = [[0, 0], [0, 6]]
        result = proj4.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
        self.assertEqual((6, 'A', 'A'), result)


if __name__ == '__main__':
    unittest.main()
