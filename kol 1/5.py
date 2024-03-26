from constraint import *


def check_valid(t1, t2):
    day_t1, hour_t1 = t1.split('_')
    day_t2, hour_t2 = t2.split('_')
    if day_t1 == day_t2:
        return abs(int(hour_t1) - int(hour_t2)) >= 2
    return True


def check_valid_ml(t1, t2):
    return t1.split('_')[1] != t2.split('_')[1]


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    variables = []
    variables_ML = []

    for i in range(1, casovi_AI + 1):
        variables.append(f"AI_cas_{i}")
        problem.addVariable(f"AI_cas_{i}", AI_predavanja_domain)

    for i in range(1, casovi_ML + 1):
        variables.append(f"ML_cas_{i}")
        variables_ML.append(f"ML_cas_{i}")
        problem.addVariable(f"ML_cas_{i}", ML_predavanja_domain)

    for i in range(1, casovi_R + 1):
        variables.append(f"R_cas_{i}")
        problem.addVariable(f"R_cas_{i}", R_predavanja_domain)

    for i in range(1, casovi_BI + 1):
        variables.append(f"BI_cas_{i}")
        problem.addVariable(f"BI_cas_{i}", BI_predavanja_domain)

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    variables.extend(["AI_vezbi", "ML_vezbi", "BI_vezbi"])
    variables_ML.append("ML_vezbi")

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            problem.addConstraint(check_valid, [variables[i], variables[j]])

    for i in range(len(variables_ML)):
        for j in range(i + 1, len(variables_ML)):
            problem.addConstraint(check_valid_ml, [variables_ML[i], variables_ML[j]])

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
