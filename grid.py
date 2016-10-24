class Grid:

    def __init__(self, size=(8, 8), walls=[],
                 exits={(0, 3): 1, (1, 3): -1}, start=(6, 0)):
        self.V = [[0 for i in range(size[1])] for i in range(size[0])]
        self.walls = walls
        self.exits = exits
        self.start = start

    def is_wall(self, i, j):
        return (i, j) in self.walls

    def is_exit(self, i, j):
        return (i, j) in self.exits.keys()

    def get_V(self, i, j):
        if self.is_wall(i, j) or self.is_out_of_map(i, j):
            raise ValueError('incorrent coordinats')
        return self.V[i][j]

    def set_V(self, i, j, new_v):
        if self.is_wall(i, j) or self.is_exit(i, j) \
                or self.is_out_of_map(i, j):
            raise ValueError('incorrent coordinats')
        self.V[i][j] = new_v

    def is_out_of_map(self, i, j):
        return i < 0 or j < 0 or i >= len(self.V) or j >= len(self.V[0])

    def outcome_of_action(self, i, j, action):
        outcomes = self._pre_outcome_of_action(i, j, action)
        for k, v in outcomes.items():
            if self.is_wall(k[0], k[1]) or self.is_out_of_map(k[0], k[1]):
                if (i, j) in outcomes.keys():
                    outcomes[(i, j)] += v
                else:
                    outcomes[(i, j)] = v
                del outcomes[(k[0], k[1])]
        return outcomes

    def _pre_outcome_of_action(self, i, j, action):
        outcomes = dict()
        if action == '^':
            outcomes = {(i - 1, j): 0.8, (i, j - 1): 0.1, (i, j + 1): 0.1}
        elif action == 'v':
            outcomes = {(i + 1, j): 0.8, (i, j - 1): 0.1, (i, j + 1): 0.1}
        elif action == '<':
            outcomes = {(i, j - 1): 0.8, (i + 1, j): 0.1, (i - 1, j): 0.1}
        elif action == '>':
            outcomes = {(i, j + 1): 0.8, (i + 1, j): 0.1, (i - 1, j): 0.1}
        return outcomes

    def __str__(self):
        return ''.join(str(i) + '\n' for i in self.V)
