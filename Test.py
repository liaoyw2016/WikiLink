from __future__ import division
from numpy.random import random
deuce_flag = 0  # A Global variable to indicate Deuce


def sim_round(points, prob_a):
    """ sim_round simulates the round where program decides which player have won the game """
    if random() < prob_a:
        points['A'] = points['A'] + 1
    else:
        points['B'] = points['B'] + 1
    return points


def continue_criteria(points, target_score):
    """continue_criteria indicates when a single game shall be continue"""
    min_cross = min(points['A'], points['B']) > min(target_score['A'], target_score['B'])
    if min_cross:
        return False
    deuce(points)
    if deuce_flag == 0:
        if max(points['A'], points['B']) == 11:
            return False
    else:
        if abs(points['A'] - points['B']) == 2:
                return False
        else:
                return True
    return True


def deuce(points):
    """when deuce happens deuce function raise a flag which will be used in stopping_criteria"""
    global deuce_flag
    if points['A'] == points['B'] and points['A'] == 10:
        deuce_flag = 1


def sim_game(target_score, prob_a):
    """sim_game simulates one single game and then its final score matches with target score or not"""
    global deuce_flag
    deuce_flag = 0
    continue_game = True
    points = {'A': 0, 'B': 0}
    deuce_flag = 0
    while continue_game:
        points = sim_round(points, prob_a)
        continue_game = continue_criteria(points, target_score)
    if points['A'] == target_score['A'] and points['B'] == target_score['B']:
        return 1
    else:
        return 0


def montecarlo(target_score, prob_a, num_sim):
    """Montecarlo simulates the Monte Carlo method.
    Its input are target score, winning prob of A and number of sample"""
    success = 0
    for i in xrange(num_sim):
        success = success + sim_game(target_score, prob_a)
    print success
    print success / num_sim


if __name__ == '__main__':
    target_score = {'A': 18, 'B': 16}
    prob_A = 0.5
    montecarlo(target_score, prob_A, 100000)
