from searching_framework import Problem, astar_search


class Man(Problem):

    def __init__(self, initial, goal=None, grid_size=0, walls=None):
        super().__init__(initial, goal)
        self.grid_size = grid_size
        self.walls = walls

    @staticmethod
    def check_valid(state):
        return (state[0], state[1]) not in walls and 0 <= state[0] < grid_size and 0 <= state[1] < grid_size

    @staticmethod
    def check_nowalls(state, i):
        man_x, man_y = state[0], state[1]
        for j in range(1, i):
            if (man_x - j, man_y) in walls:
                return False
        return True

    def successor(self, state):
        successors = dict()

        man_x, man_y, house_x, house_y = state

        # desno
        for i in range(2, 4):
            new_state = (man_x + i, man_y, house_x, house_y)
            if self.check_valid(new_state) and self.check_nowalls(new_state, i):
                successors[f"Desno {i}"] = new_state

        # gore
        new_state = (man_x, man_y + 1, house_x, house_y)
        if self.check_valid(new_state):
            successors["Gore"] = new_state

        # dolu
        new_state = (man_x, man_y - 1, house_x, house_y)
        if self.check_valid(new_state):
            successors["Dolu"] = new_state

        # levo
        new_state = (man_x - 1, man_y, house_x, house_y)
        if self.check_valid(new_state):
            successors["Levo"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        man_x, man_y, house_x, house_y = node.state
        result = abs(man_y - house_y)
        if man_x < house_x:
            result += (house_x - man_x) / 3
        else:
            result += man_x - house_x
        return result


if __name__ == '__main__':
    grid_size = int(input())
    num_walls = int(input())
    walls = list()
    for i in range(num_walls):
        walls.append(tuple(map(int, input().split(','))))

    man_state = tuple(map(int, input().split(',')))
    house_position = tuple(map(int, input().split(',')))
    initial_state = (man_state[0], man_state[1], house_position[0], house_position[1])
    goal_state = (house_position[0], house_position[1], house_position[0], house_position[1])

    problem = Man(initial_state, goal_state, grid_size, walls)
    result = astar_search(problem)

    if result is not None:
        print(result.solution())
