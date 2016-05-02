from grid import Grid
from mdp import MarkowModel

g = Grid()

previous_mm = object()
previous_r = int()

transition_intervals = list()

interval = [0.01] + [-i / 100.0 for i in range(1000)]

for r in interval:
    mm = MarkowModel(g, r)
    mm.optimal_polity()

    if str(previous_mm) != str(mm):
        transition_intervals.append((previous_r, r))
    previous_r = r
    previous_mm = mm

transition_intervals = transition_intervals[2:]
print 'There is transition point in those intervals:'
print transition_intervals
