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

import logging

# Get the top-level logger object
log = logging.getLogger()

# make it print to the console.
console = logging.StreamHandler()
log.addHandler(console)
log.warn('Citizens of Earth, be warned!')
print 'a'
# emit a warning to the puny Humans
log.warn('Citizens of Earth, be warned!')
