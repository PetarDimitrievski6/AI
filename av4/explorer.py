from searching_framework.informed_search import *
from searching_framework.utils import Problem


class Explorer(Problem):

    def __init__(self, initial, goal=None, grid_width=0, grid_height=0):
        super().__init__(initial, goal)
        self.grid_height = grid_height
        self.grid_width = grid_width

    def move_obstacle(self, obstacle):
        if obstacle[2] == 1:
            if obstacle[1] == self.grid_height - 1:
                obstacle[1] -= 1
                obstacle[2] = -1
            else:
                obstacle[1] += 1
        else:
            if obstacle[1] == 0:
                obstacle[1] += 1
                obstacle[2] = 1
            else:
                obstacle[1] -= 1
        return obstacle

    def successor(self, state):
        successors = dict()

        explorer_x = state[0]
        explorer_y = state[1]

        obstacle1 = self.move_obstacle(list(state[2]))
        obstacle2 = self.move_obstacle(list(state[3]))
        obstacles = [(obstacle1[0], obstacle1[1]), (obstacle2[0], obstacle2[1])]

        # up
        if explorer_y + 1 < self.grid_height and (explorer_x, explorer_y + 1) not in obstacles:
            successors["Up"] = (explorer_x, explorer_y + 1, tuple(obstacle1), tuple(obstacle2))

        # down
        if explorer_y > 0 and (explorer_x, explorer_y - 1) not in obstacles:
            successors["Down"] = (explorer_x, explorer_y - 1, tuple(obstacle1), tuple(obstacle2))

            # right
        if explorer_x + 1 < self.grid_width and (explorer_x + 1, explorer_y) not in obstacles:
            successors["Right"] = (explorer_x + 1, explorer_y, tuple(obstacle1), tuple(obstacle2))

        # left
        if explorer_x > 0 and (explorer_x - 1, explorer_y) not in obstacles:
            successors["Left"] = (explorer_x - 1, explorer_y, tuple(obstacle1), tuple(obstacle2))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def h(self, node):
        explorer_x = node.state[0]
        explorer_y = node.state[1]
        house_x = self.goal[0]
        house_y = self.goal[1]
        return abs(explorer_x - house_x) + abs(explorer_y - house_y)


if __name__ == '__main__':
    explorer = Explorer((0, 2, (2, 5, -1), (0, 5, 1)), (7, 4), 8, 6)
    print(astar_search(explorer).solution())
