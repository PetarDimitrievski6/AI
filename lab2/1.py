from searching_framework import Problem, astar_search
import math

class Man(Problem):
    grid_width = 5
    grid_height = 9

    def __init__(self, initial, goal=None, allowed=None):
        super().__init__(initial, goal)
        self.allowed = allowed

    def move_house(self, house_x, house_y, house_dir):
        new_house_dir = house_dir
        if house_x == 0:
            new_house_dir = 1
        elif house_x == self.grid_width - 1:
            new_house_dir = -1
        return house_x + new_house_dir, house_y, new_house_dir

    def successor(self, state):
        successors = dict()

        man_x, man_y, house_x, house_y, house_dir = state
        new_house_x, new_house_y, new_house_dir = self.move_house(house_x, house_y, house_dir)

        # stoj
        successors["Stoj"] = (man_x, man_y, new_house_x, new_house_y, new_house_dir)

        for i in range(1, 3):
            # gore
            new_man_x, new_man_y = man_x, man_y + i
            if (new_man_x, new_man_y) in allowed or (new_man_x == new_house_x and new_man_y == new_house_y):
                successors[f"Gore {i}"] = (new_man_x, new_man_y, new_house_x, new_house_y, new_house_dir)
            # gore-desno
            new_man_x, new_man_y = man_x + i, man_y + i
            if (new_man_x, new_man_y) in allowed or (new_man_x == new_house_x and new_man_y == new_house_y):
                successors[f"Gore-desno {i}"] = (new_man_x, new_man_y, new_house_x, new_house_y, new_house_dir)

            # gore-levo
            new_man_x, new_man_y = man_x - i, man_y + i
            if (new_man_x, new_man_y) in allowed or (new_man_x == new_house_x and new_man_y == new_house_y):
                successors[f"Gore-levo {i}"] = (new_man_x, new_man_y, new_house_x, new_house_y, new_house_dir)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[2] and state[1] == state[3]

    def h(self, node):
        man_x, man_y, house_x, house_y, house_dir = node.state
        return abs(man_y - house_y) / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    tmp = input().split(',')
    man_x, man_y = int(tmp[0]), int(tmp[1])
    tmp = input().split(',')
    house_x, house_y = int(tmp[0]), int(tmp[1])
    house_dir = input()
    if house_dir == "desno":
        house_dir = 1
    else:
        house_dir = -1
    initial_state = (man_x, man_y, house_x, house_y, house_dir)
    problem = Man(initial_state, None, allowed)

    result = astar_search(problem)
    if result is not None:
        print(result.solution())
