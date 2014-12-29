#!/usr/bin/python

import alg_application4_provided as app4
import collections
import matplotlib.pyplot as plt
import numpy
import proj4
import random


LOCAL_ALIGNMENT_SCORE = 875
TRIALS = 1000


random.seed(1234)


def BarPlot(scoring_dist):
    total = sum(scoring_dist.itervalues())
    x, y = [], []
    for score in sorted(scoring_dist):
        x.append(score)
        y.append(float(scoring_dist[score])/total)
    plt.bar(x, y)
    plt.ylabel('Fraction of Total Trials')
    plt.xlabel('Local Alignment Scores')
    plt.title('Bar Plot of Normalized Distribution of Local Alignment Scores')
    plt.show()


def GenNullDist(seq_x, seq_y, scoring_matrix, num_trials):
    rand_y = list(seq_y)
    scoring_dist = collections.Counter()
    for _ in xrange(num_trials):
        random.shuffle(rand_y)
        alignment_matrix = proj4.compute_alignment_matrix(
            seq_x, rand_y, scoring_matrix, False)
        score, _, _ = proj4.compute_local_alignment(
            seq_x, rand_y, scoring_matrix, alignment_matrix)
        scoring_dist[score] += 1
    return scoring_dist


def ZScore(score_list, s):
    mean = numpy.mean(score_list)
    std = numpy.std(score_list)
    z_score = (s - mean) / std
    print 'Mean: {}; Std: {}'.format(mean, std)
    print 'Z-score: {}'.format(z_score)


def main():
    human_protein = app4.read_protein(app4.HUMAN_EYELESS_URL)
    fruitfly_protein = app4.read_protein(app4.FRUITFLY_EYELESS_URL)
    scoring_matrix = app4.read_scoring_matrix(app4.PAM50_URL)
    scoring_dist = GenNullDist(
        human_protein, fruitfly_protein, scoring_matrix, TRIALS)
    BarPlot(scoring_dist)
    ZScore(scoring_dist.keys(), LOCAL_ALIGNMENT_SCORE)


if __name__ == '__main__':
    main()
