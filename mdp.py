import copy


class MarkowModel:

    def __init__(self, grid, r_value):
        self.iteration_number = 0
        self.grid = grid
        self.r_value = r_value
        self.polities = [['x' for i in range(len(grid.V[0]))]
                         for i in range(len(grid.V))]
        self.actions = ['^', 'v', '<', '>']

    def R(self, i, j):
        # TODO: may there is issue in exit points as + r_value
        if self.grid.is_wall(i, j):
            raise ValueError()
        elif self.grid.is_exit(i, j):
            return self.grid.exits[i, j]
        return self.r_value

    def next_V(self):
        previous_grid = copy.deepcopy(self.grid)
        for i in range(len(self.grid.V)):
            for j in range(len(self.grid.V[0])):
                if not (self.grid.is_exit(i, j) or self.grid.is_wall(i, j)):
                    polity = max(self.Qs(i, j, previous_grid),
                                 key=lambda x: x[1])
                    self.grid.set_V(i, j, polity[1])
                    self.polities[i][j] = polity[0]

    def Q(self, i, j, action, previous_grid):
        outcomes = self.grid.outcome_of_action(i, j, action)
        q = float()
        for k, v in outcomes.items():
            q += v * (self.R(k[0], k[1]) + previous_grid.get_V(k[0], k[1]))
        return q

    def Qs(self, i, j, previous_grid):
        return map(lambda x: (x, self.Q(i, j, x, previous_grid)), self.actions)

    def __str__(self):
        return ''.join(str(i) + '\n' for i in self.polities)
