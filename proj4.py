"""Project 4."""
from collections import defaultdict


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """Build scoring matrix."""
    alphabet = alphabet if isinstance(alphabet, set) else set(alphabet)
    result = defaultdict(dict)
    for char1 in alphabet.union(set(['-'])):
        result['-'][char1] = dash_score
        result[char1]['-'] = dash_score
        if char1 != '-':
            result[char1][char1] = diag_score
        else:
            continue
        for char2 in alphabet:
            if char2 not in (char1, '-'):
                result[char1][char2] = off_diag_score
                result[char2][char1] = off_diag_score
    return result


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """Compute alignment matrix."""
    length_x, length_y = len(seq_x), len(seq_y)
    result = defaultdict(dict)
    result = [[0] * (length_y+1) for _ in xrange(length_x+1)]
    for index_x in xrange(1, length_x+1):
        char_x = seq_x[index_x-1]
        result[index_x][0] = update_score(
            result[index_x-1][0] + scoring_matrix[char_x]['-'],
            global_flag)
    for index_y in xrange(1, length_y+1):
        char_y = seq_y[index_y-1]
        result[0][index_y] = update_score(
            result[0][index_y-1] + scoring_matrix['-'][char_y],
            global_flag)
    for index_x in xrange(1, length_x+1):
        for index_y in xrange(1, length_y+1):
            char_x, char_y = seq_x[index_x-1], seq_y[index_y-1]
            result[index_x][index_y] = update_score(
                max(result[index_x-1][index_y-1] + scoring_matrix[char_x][char_y],
                    result[index_x-1][index_y] + scoring_matrix[char_x]['-'],
                    result[index_x][index_y-1] + scoring_matrix['-'][char_y]),
                global_flag)
    return result


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Compute global alignment."""
    index_x, index_y = len(seq_x), len(seq_y)
    result_x, result_y = '', ''
    while index_x and index_y:
        char_x, char_y = seq_x[index_x-1], seq_y[index_y-1]
        if (alignment_matrix[index_x][index_y]
            == (alignment_matrix[index_x-1][index_y-1] + scoring_matrix[char_x][char_y])):
            result_x, result_y = char_x + result_x, char_y + result_y
            index_x, index_y = index_x - 1, index_y - 1
        elif (alignment_matrix[index_x][index_y]
              == (alignment_matrix[index_x-1][index_y] + scoring_matrix[char_x]['-'])):
            result_x, result_y = char_x + result_x, '-' + result_y
            index_x = index_x - 1
        else:
            result_x, result_y = '-' + result_x, char_y + result_y
            index_y = index_y - 1
    for index in xrange(index_x-1, -1, -1):
        result_x, result_y = seq_x[index] + result_x, '-' + result_y
    for index in xrange(index_y-1, -1, -1):
        result_x, result_y = '-' + result_x, seq_y[index] + result_y
    return alignment_matrix[-1][-1], result_x, result_y


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Compute local alignment."""
    if not seq_x and not seq_y:
        return 0, '', ''
    index_x, index_y = find_max_score_indices(alignment_matrix)
    max_score = alignment_matrix[index_x][index_y]
    score, result_x, result_y = max_score, '', ''
    while score:
        char_x, char_y = seq_x[index_x-1], seq_y[index_y-1]
        if (alignment_matrix[index_x][index_y]
            == (alignment_matrix[index_x-1][index_y-1] + scoring_matrix[char_x][char_y])):
            score = alignment_matrix[index_x-1][index_y-1]
            result_x, result_y = char_x + result_x, char_y + result_y
            index_x, index_y = index_x - 1, index_y - 1
        elif (alignment_matrix[index_x][index_y]
              == (alignment_matrix[index_x-1][index_y] + scoring_matrix[char_x]['-'])):
            score = alignment_matrix[index_x-1][index_y]
            result_x, result_y = char_x + result_x, '-' + result_y
            index_x = index_x - 1
        else:
            score = alignment_matrix[index_x][index_y-1]
            result_x, result_y = '-' + result_x, char_y + result_y
            index_y = index_y - 1
    return max_score, result_x, result_y


def find_max_score_indices(alignment_matrix):
    """Find indices of max score."""
    max_value, max_x, max_y = 0, 0, 0
    for index_x, row in enumerate(alignment_matrix):
        for index_y, value in enumerate(row):
            if value > max_value:
                max_value, max_x, max_y = value, index_x, index_y
    return max_x, max_y


def update_score(score, global_flag):
    """Update score based on global flag."""
    return score if global_flag else max(score, 0)
