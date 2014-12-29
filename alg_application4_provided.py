#!/usr/bin/python
"""
Provide code and solution for Application 4
"""

DESKTOP = True

import itertools
import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    # import alg_project4_solution as student
    import proj4
else:
    import simpleplot
    import userXX_XXXXXXX as student
    

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list


def global_agreement(alignment, consensus, scoring_matrix):
    alignment = [c for c in alignment if c != '-']
    alignment_matrix = proj4.compute_alignment_matrix(
        alignment, consensus, scoring_matrix, True)
    result = proj4.compute_global_alignment(
        alignment, consensus, scoring_matrix, alignment_matrix)
    print 'Global alignments: {}'.format(result[1:])
    agree = sum(int(c1==c2) for c1, c2 in itertools.izip(*result[1:]))
    print 'agree: {}; length: {}'.format(agree, len(result[1]))
    return 100.0 * agree / len(result[1])


def main():
    human_protein = read_protein(HUMAN_EYELESS_URL)
    fruitfly_protein = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    alignment_matrix = proj4.compute_alignment_matrix(
        human_protein, fruitfly_protein, scoring_matrix, False)
    result = proj4.compute_local_alignment(
        human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)
    print 'Application 4.1:'
    print 'Result: {}'.format(result)
    human_alignment, fruitfly_alignment = result[1], result[2]
    consensus = read_protein(CONSENSUS_PAX_URL)
    print 'Application 4.2:'
    print 'Human prcentage: {0:4f}%'.format(
        global_agreement(human_alignment, consensus, scoring_matrix))
    print 'Fruitfly prcentage: {0:4f}%'.format(
        global_agreement(fruitfly_alignment, consensus, scoring_matrix))


if __name__ == '__main__':
    main()
