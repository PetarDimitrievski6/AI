import itertools
from collections import Counter

from searching_framework.informed_search import *
from searching_framework.utils import *


class Pacmans(Problem):
    def __init__(self, initial, grid_width, grid_height, walls, pellets_mapping, pacman_bag_capacity, goal=None):
        super().__init__(initial, goal)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.walls = walls
        self.pellets_mapping = pellets_mapping
        self.pacman_bag_capacity = pacman_bag_capacity
        self.moves = ["stop", "up", "down", "right", "left"]
        self.number_of_pacmans = len(initial[:-1])

    def check_valid(self, pacmans):
        if min(p[0] for p in pacmans) < 0 or max(p[0] for p in pacmans) >= self.grid_width or \
                min(p[1] for p in pacmans) < 0 or max(p[1] for p in pacmans) >= self.grid_height:
            return False
        if any(tuple(p[:2]) in self.walls for p in pacmans):
            return False
        counter = Counter([p[:2] for p in pacmans])
        if any(count > 4 for count in counter.values()):
            return False
        return True

    def pickup_pellet(self, pacman, pellets):
        index = self.pellets_mapping.get(tuple(pacman[:2]), -1)
        if index != -1:
            if pellets[index] == True:
                pellets[index] = False
                pacman[2] += 1

    def successor(self, state):
        successors = dict()
        pacmans = state[:-1]
        pellets = state[-1]

        combinations = itertools.product(self.moves, repeat=self.number_of_pacmans)

        for combination in combinations:
            new_pacmans = list()
            new_pellets = list(pellets)
            actions_taken = ""
            for move, pacman in zip(combination, pacmans):
                new_pacman = list(pacman)

                # check if bag capacity of pacman is full then move is stop
                if pacman[-1] == self.pacman_bag_capacity or move == 'stop':
                    actions_taken += 'stop,'
                elif move == 'up':
                    new_pacman[1] += 1
                    actions_taken += 'up,'
                elif move == 'down':
                    new_pacman[1] -= 1
                    actions_taken += 'down,'
                elif move == 'right':
                    new_pacman[0] += 1
                    actions_taken += 'right,'
                elif move == 'left':
                    new_pacman[0] -= 1
                    actions_taken += 'left,'

                self.pickup_pellet(new_pacman, new_pellets)
                new_pacmans.append(tuple(new_pacman))

            if not self.check_valid(new_pacmans):
                continue

            new_pacmans.append(tuple(new_pellets))
            actions_taken = actions_taken[:-1]
            successors[actions_taken] = tuple(new_pacmans)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        pellets = state[-1]
        for pellet in pellets:
            if pellet is True:
                return False
        return True

    def h(self, node):
        pacmans = node.state[:-1]
        pellets = node.state[-1]

        remaining_pellets = [key for key, eaten in self.pellets_mapping.items() if pellets[eaten]]
        remaining_space_pacmans = [pacman[:2] for pacman in pacmans if pacman[2] < self.pacman_bag_capacity]

        if not remaining_pellets:
            return 0

        min_distances = []
        for pellet in remaining_pellets:
            distances = [
                abs(pacman[0] - pellet[0]) + abs(pacman[1] - pellet[1])
                for pacman in remaining_space_pacmans
            ]
            min_distances.append(min(distances))

        min_distance = min(min_distances)

        diff = len(remaining_pellets) / len(remaining_space_pacmans)

        # heuristic function returns the maximum of
        # 1. minimum remaining distance to pellet of pacmans with non-full bag
        # 2. difference between remaining pellets and pacmans with non-full bag
        return max(min_distance, diff)


if __name__ == '__main__':
    # initial_state = ((p1_x, p1_y, p1_bag), (p2_x, p2_y, p2_bag),...(pK_x, pK_y, pK_bag), (pellets))
    grid_width = int(input())
    grid_height = int(input())

    walls_n = int(input())
    walls = list()
    for i in range(walls_n):
        walls.append(tuple(map(int, input().split(','))))

    pellets_n = int(input())
    # dict to map key = (pellet_x, pellet_y), value = index of the flag of pellets_flags
    pellets_mapping = dict()
    pellets_flags = [True for i in range(pellets_n)]
    for i in range(pellets_n):
        pellets_mapping[(tuple(map(int, input().split(','))))] = i

    pacmans_n = int(input())
    pacmans = [(0, 0, 0) for i in range(pacmans_n)]
    pacman_bag_capacity = int(input())

    pacmans.append(tuple(pellets_flags))
    initial_state = tuple(pacmans)

    problem = Pacmans(initial_state, grid_width, grid_height, walls, pellets_mapping, pacman_bag_capacity)
    result = astar_search(problem).solution()

    pacman_moves = [[] for _ in range(pacmans_n)]
    for move in result:
        directions = move.split(',')
        for i in range(pacmans_n):
            pacman_moves[i].append(directions[i])

    for i, pm in enumerate(pacman_moves, start=1):
        sequence = ", ".join(pm)
        print(f"Pacman{i}: {sequence}")
