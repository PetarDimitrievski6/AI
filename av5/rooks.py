from constraint import *


def not_attacking(rook1, rook2):
    return rook1[0] != rook2[0] and rook1[1] != rook2[1]


if __name__ == '__main__':
    # (row, column)
    problem = Problem()
    domain = [(i, j) for i in range(8) for j in range(8)]
    rooks = range(1, 9)
    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 != rook2:
                problem.addConstraint(not_attacking, (rook1, rook2))

    print(problem.getSolution())
