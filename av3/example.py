from searching_framework.uninformed_search import *


class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        # (j0,j1)

        successors = dict()

        j0, j1 = state
        c0, c1 = self.capacities

        if j0 > 0:
            successors["Isprazni go sadot J0"] = (0, j1)

        if j1 > 0:
            successors["Isprazni go sadot J1"] = (j0, 0)

        if j0 > 0 and j1 < c1:
            dif = min(c1 - j1, j0)
            successors["Preturi od J0 vo J1"] = (j0 - dif, j1 + dif)

        if j1 > 0 and j0 < c0:
            dif = min(c0 - j0, j1)
            successors["Preturi od J1 vo J0"] = (j0 + dif, j1 - dif)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    container = Container([15, 10], (7, 3), (10, 0))

    result = breadth_first_graph_search(container)
    print(result.solution())
    print(result.solve())

    result = depth_first_graph_search(container)
    print(result.solution())
    print(result.solve())