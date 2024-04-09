from constraint import *


def vreme(v):
    return v == 13 or v == 14 or v == 16 or v == 19


times = []


def different(v):
    if v not in times:
        times.append(v)
        return True
    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 21))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(lambda a: a == 1, ["Simona_prisustvo"])
    problem.addConstraint(vreme, ["vreme_sostanok"])
    problem.addConstraint(different, ["vreme_sostanok"])
    problem.addConstraint(AllDifferentConstraint(), ["Marija_prisustvo", "Petar_prisustvo"])

    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
