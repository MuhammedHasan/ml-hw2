import cPickle as pickle
import numpy as np
import itertools

dataset = pickle.load(open('training_data.p', 'rb'))

f = open('m.txt', 'w')
points = list(itertools.product(range(0, 8)[::-1], range(0, 8)))

for i in dataset.values():
    for j in i[0]:
        f.write(str(j))
        f.write('\n')
    f.write('\n')
    for index, p in enumerate(points):
        if i[1][p] == 0:
            f.write(' ^ ')
        elif i[1][p] == 1:
            f.write(' > ')
        elif i[1][p] == 2:
            f.write(' v ')
        elif i[1][p] == 3:
            f.write(' < ')

        if (index + 1) % 8 == 0:
            f.write('\n')
    f.write('\n')
    f.write('\n')
print dataset[0][1]
