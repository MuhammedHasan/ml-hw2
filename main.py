# import cPickle as pickle
# import numpy as np
# import itertools
#
# dataset = pickle.load(open('training_data.p', 'rb'))
#
# f = open('m.txt', 'w')
# # points = list(itertools.product(range(0, 8), range(0, 8)))
#
# for i in dataset.values():
#     for x in range(0, 8)[::-1]:
#         for y in range(0, 8):
#             if i[0][7 - x][y] != 0:
#                 f.write(' %d ' % i[0][7 - x][y])
#             else:
#                 if i[1][x, y] == 0:
#                     f.write(' ^ ')
#                 elif i[1][x, y] == 1:
#                     f.write(' > ')
#                 elif i[1][x, y] == 2:
#                     f.write(' v ')
#                 elif i[1][x, y] == 3:
#                     f.write(' < ')
#         f.write('\n')
#     f.write('\n')
#     f.write('\n')
#
# # print dataset[0][1]

from grid import Grid
from mdp import MarkowModel
from feature_extraction import get_exits_from_grid
import pickle
import time
import threading


dataset = pickle.load(open('training_data.p', 'rb'))
testset = pickle.load(open('test_data.p', 'rb'))

print len(testset)

for i in dataset.values():
    grid = i[0]
    g = Grid(exits=get_exits_from_grid(grid))
    mm = MarkowModel(g, -1)
    mm.optimal_polity()
