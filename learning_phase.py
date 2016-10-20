# -*- coding: utf-8 -*-
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import numpy as np
import operator
import cPickle as pickle
from feature_extraction import *
import itertools


dataset = pickle.load(open('training_data.p', 'rb'))
points = list(itertools.product(range(1, 7), range(1, 7)))

X = np.array([feature_set(p, s[0]) for p in points for s in dataset.values()])
y = np.array([s[1][p] for p in points for s in dataset.values()])

sc = StandardScaler()
sc.fit(X)
X_std = sc.transform(X)

svm = SVC(kernel='rbf', C=1.0, random_state=0)
svm.fit(X_std, y)


def eveluate_model(grid):
    """For a given grid, return the policy for that grid
       Parameters
       ----------
       grid: 2 dimensional array representing a grid
       Return:
       policy: type-dictionary, for states (1,1) up to (6,6)
       """
    X = np.array([feature_set(p, grid) for p in points])
    X_std = sc.transform(X)
    return {(p[0], p[1]): v for p, v in zip(points, svm.predict(X_std))}


def check_accurcy():

    testset = pickle.load(open('test_data.p', 'rb'))

    test_y = np.array([i[1][p] for p in points for i in testset.values()])

    predicted_y = [eveluate_model(i[0]).values() for i in testset.values()]
    predicted_y = np.array(reduce(operator.add, predicted_y))

    print test_y
    print predicted_y

    return sum(test_y == predicted_y) / float(test_y.size)
