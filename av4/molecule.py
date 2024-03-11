from searching_framework.informed_search import *
from searching_framework.uninformed_search import *


class Molecule(Problem):
    def __init__(self, initial, goal=None, grid_width=0, grid_height=0, obstacles=None):
        super().__init__(initial, goal)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.obstacles = obstacles

    def valid_move(self, element, molecules):
        return 0 <= element[0] < self.grid_width and 0 <= element[1] < self.grid_height \
            and element not in self.obstacles and element not in molecules

    def successor(self, state):
        successors = dict()

        h1 = [state[0], state[1]]
        o = [state[2], state[3]]
        h2 = [state[4], state[5]]
        molecules = [h1, o, h2]

        # up
        new_h1 = [h1[0], h1[1] + 1]
        if self.valid_move(new_h1, molecules):
            while self.valid_move([new_h1[0], new_h1[1] + 1], molecules):
                new_h1[1] += 1
            successors["Up_H1"] = (new_h1[0], new_h1[1], o[0], o[1], h2[0], h2[1])

        new_o = [o[0], o[1] + 1]
        if self.valid_move(new_o, molecules):
            while self.valid_move([new_o[0], new_o[1] + 1], molecules):
                new_o[1] += 1
            successors["Up_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])

        new_h2 = [h2[0], h2[1] + 1]
        if self.valid_move(new_h2, molecules):
            while self.valid_move([new_h2[0], new_h2[1] + 1], molecules):
                new_h2[1] += 1
            successors["Up_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])

        # down
        new_h1 = [h1[0], h1[1] - 1]
        if self.valid_move(new_h1, molecules):
            while self.valid_move([new_h1[0], new_h1[1] - 1], molecules):
                new_h1[1] -= 1
            successors["Down_H1"] = (new_h1[0], new_h1[1], o[0], o[1], h2[0], h2[1])

        new_o = [o[0], o[1] - 1]
        if self.valid_move(new_o, molecules):
            while self.valid_move([new_o[0], new_o[1] - 1], molecules):
                new_o[1] -= 1
            successors["Down_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])

        new_h2 = [h2[0], h2[1] - 1]
        if self.valid_move(new_h2, molecules):
            while self.valid_move([new_h2[0], new_h2[1] - 1], molecules):
                new_h2[1] -= 1
            successors["Down_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])

        # right
        new_h1 = [h1[0] + 1, h1[1]]
        if self.valid_move(new_h1, molecules):
            while self.valid_move([new_h1[0] + 1, new_h1[1]], molecules):
                new_h1[0] += 1
            successors[("Right_H1")] = (new_h1[0], new_h1[1], o[0], o[1], h2[0], h2[1])

        new_o = [o[0] + 1, o[1]]
        if self.valid_move(new_o, molecules):
            while self.valid_move([new_o[0] + 1, new_o[1]], molecules):
                new_o[0] += 1
            successors["Right_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])

        new_h2 = [h2[0] + 1, h2[1]]
        if self.valid_move(new_h2, molecules):
            while self.valid_move([new_h2[0] + 1, new_h2[1]], molecules):
                new_h2[0] += 1
            successors["Right_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])

        # left
        new_h1 = [h1[0] - 1, h1[1]]
        if self.valid_move(new_h1, molecules):
            while self.valid_move([new_h1[0] - 1, new_h1[1]], molecules):
                new_h1[0] -= 1
            successors[("Left_H1")] = (new_h1[0], new_h1[1], o[0], o[1], h2[0], h2[1])

        new_o = [o[0] - 1, o[1]]
        if self.valid_move(new_o, molecules):
            while self.valid_move([new_o[0] - 1, new_o[1]], molecules):
                new_o[0] -= 1
            successors["Left_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])

        new_h2 = [h2[0] - 1, h2[1]]
        if self.valid_move(new_h2, molecules):
            while self.valid_move([new_h2[0] - 1, new_h2[1]], molecules):
                new_h2[0] -= 1
            successors["Left_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] + 1 == state[2] == state[4] - 1 and state[1] == state[3] == state[5]

    def h(self, node):
        # Хевристичка функција која за секоја состојба пресметува минимален
        # број на турнувања на паровите од атоми за тие да се спојат
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]
        value = 0

        # проверка за позициите на H1 и O и потребниот број на чекори за да се спојат
        if h1[0] != o[0]:
            if h1[1] != (o[1] - 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h1[0] == o[0]
            if h1[1] > o[1]:
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h1[1] < (o[1] - 1):
                # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn right) за да се спојат
                value += 1

        # проверка за позициите на H2 и O и потребниот број на чекори за да се спојат
        if h2[0] != o[0]:
            if h2[1] != (o[1] + 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h2[0] == o[0]
            if h2[1] < o[1]:  # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h2[1] > (o[1] + 1):
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn left) за да се спојат
                value += 1

        if h1[0] == h2[0] and h1[0] != o[0]:
            # ако водородните атоми се во ист ред тогаш можеме да имаме само едно турнување на
            # атомот на кислород up/down (а претходно сме пресметале турнување на H1 и турнување на H2)
            value -= 1

        return value


if __name__ == '__main__':
    initial_state = (2, 1, 7, 2, 2, 6)
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    molecule = Molecule(initial_state, None, 9, 7, obstacles_list)
    print(astar_search(molecule).solution())
    print(greedy_best_first_graph_search(molecule).solution())
