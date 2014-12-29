#!/usr/bin/python

import alg_application4_provided as app4
import proj4


SCORING_MATRIX = proj4.build_scoring_matrix(
    'abcdefghijklmnopqrstuvwxyz', 2, 1, 0)


def CheckSpelling(checked_word, edit, word_list):
    return sorted(word for word in word_list
                  if EditDistance(checked_word, word) <= edit)


def EditDistance(checked_word, word):
    align_matrix = proj4.compute_alignment_matrix(
        checked_word, word, SCORING_MATRIX, True)
    result = proj4.compute_global_alignment(
        checked_word, word, SCORING_MATRIX, align_matrix)
    return len(checked_word) + len(word) - result[0]


def main():
    word_list = app4.read_words(app4.WORD_LIST_URL)
    checked_word = 'humble' 
    result = CheckSpelling(checked_word, 1, word_list)
    print 'checked_word: {}'.format(checked_word)
    print 'Result: {}'.format(result)
    checked_word = 'firefly' 
    result = CheckSpelling(checked_word, 2, word_list)
    print 'checked_word: {}'.format(checked_word)
    print 'Result: {}'.format(result)


if __name__ == '__main__':
    main()
