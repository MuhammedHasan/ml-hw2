# -*- coding: utf-8 -*-
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
import operator
import cPickle as pickle
from feature_extraction import *
import itertools
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

points = list(itertools.product(range(1, 7), range(1, 7)))


def train_model(feature_selection=feature_set):
    dataset = pickle.load(open('training_data.p', 'rb'))

    X = np.array([feature_selection(p, s[0])
                  for s in dataset.values() for p in points])
    y = np.array([s[1][p] for s in dataset.values() for p in points])

    svm = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', SVC(kernel='rbf', C=1.0, random_state=0))
    ])
    return svm.fit(X, y)

svm = train_model()


def eveluate_model(grid, feature_selection=feature_set, model=svm):
    """For a given grid, return the policy for that grid
       Parameters
       ----------
       grid: 2 dimensional array representing a grid
       Return:
       policy: type-dictionary, for states (1,1) up to (6,6)
       """
    X = np.array([feature_selection(p, grid) for p in points])
    return {(p[0], p[1]): v for p, v in zip(points, model.predict(X))}


def check_accurcy(dataset='test_data', model=eveluate_model):

    testset = pickle.load(open(dataset + '.p', 'rb'))
    test_y = [i[1][p] for i in testset.values() for p in points]

    eve_models = [model(i[0]) for i in testset.values()]
    predicted_y = [pre[p] for pre in eve_models for p in points]

    return accuracy_score(predicted_y, test_y)
