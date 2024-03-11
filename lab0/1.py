import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def grade(points):
    if points > 90:
        return 10
    elif points > 80:
        return 9
    elif points > 70:
        return 8
    elif points > 60:
        return 7
    elif points > 50:
        return 6
    else:
        return 5


if __name__ == "__main__":
    students = dict()
    while True:
        line = input()
        if line == "end":
            break
        parts = line.split(",")
        name = parts[0] + " " + parts[1]
        index = parts[2]
        course = parts[3]
        theoretical_points = int(parts[4])
        practical_points = int(parts[5])
        labs_points = int(parts[6])
        if name not in students:
            students[name] = {}
        students[name][course] = grade(theoretical_points + practical_points + labs_points)

    for student, courses in students.items():
        print(f"Student: {student}")
        for course, grade in courses.items():
            print(f"----{course}: {grade}")
        print()
