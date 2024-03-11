from searching_framework.informed_search import astar_search
from searching_framework.utils import Problem


def valid(state):
    f, wolf, goat, cabbage = state
    if wolf == goat and wolf != f:
        return False
    if goat == cabbage and goat != f:
        return False
    return True


class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        f, wolf, goat, cabbage = state

        # farmer alone
        f_new = 'w' if f == 'e' else 'e'
        new_state = f_new, wolf, goat, cabbage
        if valid(new_state):
            successors["Farmer_drives_alone"] = new_state

        # farmer rides wolf
        if f == wolf:
            wolf_new = 'w' if wolf == 'e' else 'e'
            new_state = f_new, wolf_new, goat, cabbage
            if valid(new_state):
                successors["Farmer_drives_wolf"] = new_state

        # farmer rides goat
        if f == goat:
            goat_new = 'w' if goat == 'e' else 'e'
            new_state = f_new, wolf, goat_new, cabbage
            if valid(new_state):
                successors["Farmer_drives_goat"] = new_state

        # farmer rides cabbage
        if f == cabbage:
            cabbage_new = 'w' if cabbage == 'e' else 'e'
            new_state = f_new, wolf, goat, cabbage_new
            if valid(new_state):
                successors["Farmer_drives_cabbage"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        c = 0
        for x, y in zip(node.state, self.goal):
            if x != y:
                c += 1
        return c


if __name__ == '__main__':
    initial_state = ('e', 'e', 'e', 'e')
    goal_state = ('w', 'w', 'w', 'w')
    farmer = Farmer(initial_state, goal_state)
    result = astar_search(farmer)
    print(result.solution())
