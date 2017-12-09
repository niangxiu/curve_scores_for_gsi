from __future__ import division
from numpy import *
from pandas import *


def run(xl, which, max):
    n_students = xl[0].shape[0]
    n_quiz = 13

    score_flat = []
    for i in range(n_quiz):
        for j in range(n_students):
            if not isnan(xl[i][j]):
                # first sanction data
                assert (xl[i][j] >=0 and xl[i][j] <=max), print(i,j,xl[i][j])
                score_flat.append(xl[i][j])

    score_flat = array(score_flat)
    mu = average(score_flat)
    sig = std(score_flat)

    scores = zeros([n_quiz,n_students])
    for i in range(n_quiz):
        for j in range(n_students):
            if not isnan(xl[i][j]):
                if which == 'quiz':
                    # normalize if quiz
                    scores[i,j] = min((xl[i][j] - mu)/sig + 8, 10)
                elif which == 'hw':
                    # do not normalize if for homework
                    scores[i,j] = xl[i][j]
                else:
                    print('illegal input here')
                    raise()
            elif isnan(xl[i][j]):
                scores[i,j] = 0
    scores = rollaxis(scores,1,0)
    print(scores.shape)

    # to compute each students final score
    print(which)
    raw = zeros(n_students)
    final = zeros(n_students)
    for j in range(n_students):
        # print(j)
        # print(scores[j][scores[j].argsort()[2:]])
        raw[j] = average(scores[j][scores[j].argsort()[2:]])
        final[j] = rint(2*raw[j]) /2
        print(final[j])

xl =  read_excel('quiz_hw.xlsx', 'quiz')
run(xl, 'quiz', 20)

xl =  read_excel('quiz_hw.xlsx', 'hw')
run(xl, 'hw', 10)
