from constraint import *


def meeting(marija, petar, time_term):
    if marija == 1 and petar == 0 and time_term == 14:
        return True
    if marija == 0 and petar == 1 and time_term == 19:
        return True
    if marija == 0 and petar == 1 and time_term == 16:
        return True
    if marija == 0 and petar == 1 and time_term == 13:
        return True
    else:
        return None


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    time_table = [13, 14, 16, 19]
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", time_table)
    problem.addConstraint(meeting, ["Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    solutions = problem.getSolutions()
    [print(solution) for solution in solutions]