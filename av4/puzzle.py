from searching_framework.informed_search import *
from searching_framework.utils import Problem


class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        """ 0 1 2
            3 4 5
            6 7 8 """

        star_i = state.index("*")

        # up
        if star_i > 2:
            new_state = list(state)
            new_state[star_i], new_state[star_i - 3] = new_state[star_i - 3], new_state[star_i]
            new_state = ''.join(new_state)
            successors["Up"] = new_state

        # down
        if star_i < 6:
            new_state = list(state)
            new_state[star_i], new_state[star_i + 3] = new_state[star_i + 3], new_state[star_i]
            new_state = ''.join(new_state)
            successors["Down"] = new_state

        # right
        if star_i % 3 != 2:
            new_state = list(state)
            new_state[star_i], new_state[star_i + 1] = new_state[star_i + 1], new_state[star_i]
            new_state = ''.join(new_state)
            successors["Right"] = new_state

        # left
        if star_i % 3 != 0:
            new_state = list(state)
            new_state[star_i], new_state[star_i - 1] = new_state[star_i - 1], new_state[star_i]
            new_state = ''.join(new_state)
            successors["Left"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        c = 0
        for x, y in zip(node.state, "*12345678"):
            if x != y:
                c += 1
        return c


class Puzzle2(Puzzle):
    coordinates = {0: (0, 2), 1: (1, 2), 2: (2, 2), 3: (0, 1),
                   4: (1, 1), 5: (2, 1), 6: (0, 0), 7: (1, 0),
                   8: (2, 0)}

    @staticmethod
    def mhd(n, m):
        x1, y1 = Puzzle2.coordinates[n]
        x2, y2 = Puzzle2.coordinates[m]

        return abs(x1 - x2) + abs(y1 - y2)

    def h(self, node):
        sum_value = 0

        for x in '12345678':
            val = Puzzle2.mhd(node.state.index(x), int(x))
            sum_value += val

        return sum_value


if __name__ == '__main__':
    initial_state = "*32415678"
    goal_state = "*12345678"
    puzzle2 = Puzzle2(initial_state, goal_state)
    print(astar_search(puzzle2).solution())
