from searching_framework.uninformed_search import *



class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        knight_x = state[0]
        knight_y = state[1]
        bishop_x = state[2]
        bishop_y = state[3]
        stars_pos = state[4]

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        pass


if __name__ == '__main__':
    pass
