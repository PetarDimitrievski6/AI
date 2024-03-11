import os
import random

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


def random_from_1_to_4():
    return random.randint(1, 4)


class Player:
    def __init__(self):
        super().__init__()
        self.position = [0, 0]

    def move(self, direction):
        x = self.position[0]
        y = self.position[1]
        if direction == 1:
            self.position = [x, y + 1]
            print(self.position)
        elif direction == 2:
            self.position = [x, y - 1]
            print(self.position)
        elif direction == 3:
            self.position = [x + 1, y]
            print(self.position)
        elif direction == 4:
            self.position = [x - 1, y]
            print(self.position)


class Game:
    def __init__(self, width, height, dots):
        super().__init__()
        self.width = width
        self.height = height
        self.dots = dots


class Pacman:
    def __init__(self, game, player):
        super().__init__()
        self.game = game
        self.player = player

    def play_game(self):
        # 1 - up
        # 2 - down
        # 3 - right
        # 4 - left

        width = self.game.width
        height = self.game.height
        dots = self.game.dots

        while len(dots) > 0:
            x = self.player.position[0]
            y = self.player.position[1]
            dots_moves = list()
            allowed_moves = list()

            if y + 1 < height:
                allowed_moves.append(1)
                if [x, y + 1] in dots:
                    dots_moves.append(1)
            if y > 0:
                allowed_moves.append(2)
                if [x, y - 1] in dots:
                    dots_moves.append(2)
            if x + 1 < width:
                allowed_moves.append(3)
                if [x + 1, y] in dots:
                    dots_moves.append(3)
            if x > 0:
                allowed_moves.append(4)
                if [x - 1, y] in dots:
                    dots_moves.append(4)

            if len(dots_moves) > 0:
                if len(dots_moves) == 1:
                    self.player.move(dots_moves[0])
                    dots.remove(self.player.position)
                else:
                    rand = random_from_1_to_4()
                    while rand not in dots_moves:
                        rand = random_from_1_to_4()
                    self.player.move(rand)
                    dots.remove(self.player.position)
            else:
                rand = random_from_1_to_4()
                while rand not in allowed_moves:
                    rand = random_from_1_to_4()
                self.player.move(rand)


if __name__ == "__main__":
    grid_width = int(input())
    grid_height = int(input())
    matrix = list()

    for i in range(grid_height):
        tmp = list(input())
        matrix.insert(0, tmp)

    dots = list()
    for i in range(grid_height):
        for j in range(grid_width):
            if matrix[i][j] == '.':
                dots.append([i, j])

    if len(dots) == 0:
        print("Nothing to do here")
    else:
        player = Player()
        game = Game(grid_width, grid_height, dots)
        pacman = Pacman(game, player)
        pacman.play_game()
