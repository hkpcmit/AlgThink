#!/usr/bin/python

import alg_application4_provided
import proj4


def main():
    human_protein = alg_application4_provided.read_protein(
        alg_application4_provided.HUMAN_EYELESS_URL)
    fruitfly_protein = alg_application4_provided.read_protein(
        alg_application4_provided.FRUITFLY_EYELESS_URL)
    scoring_matrix = alg_application4_provided.read_scoring_matrix(
        alg_application4_provided.PAM50_URL)
    alignment_matrix = proj4.compute_alignment_matrix(
        human_protein, fruitfly_protein, scoring_matrix, False)
    result = proj4.compute_local_alignment(
        human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)
    print 'Result: {}'.format(result)


if __name__ == '__main__':
    main()
