from grid import Grid
from mdp import MarkowModel

g = Grid()

g = Grid()

mm = MarkowModel(g, -0.001)
for i in range(100):
    mm.next_V()

print(mm.grid)
print(mm)
