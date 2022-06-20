from constraint import *


def different(a, b):
    if a != b:
        return True
    else:
        return None


if __name__ == "__main__":

    problem = Problem(BacktrackingSolver())
    problem.addVariables(["WA", "NT", "SA", "Q", "NSW", "V", "T"], ["red", "blue", "green"])

    problem.addConstraint(different, ["WA", "NT"])
    problem.addConstraint(different, ["WA", "SA"])
    problem.addConstraint(different, ["SA", "NT"])
    problem.addConstraint(different, ["SA", "NSW"])
    problem.addConstraint(different, ["SA", "Q"])
    problem.addConstraint(different, ["SA", "V"])
    problem.addConstraint(different, ["NT", "Q"])
    problem.addConstraint(different, ["Q", "NSW"])
    problem.addConstraint(different, ["V", "NSW"])

    # problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
    # problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "NT"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
    # problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
    # problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
    # problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
    # problem.addConstraint(lambda a, b: a != b, ("V", "NSW"))

    solutions = problem.getSolutions()
    # solution = problem.getSolution()
    print(len(solutions))
    # print(solution)
    # print(solution["Q"])
    print(solutions)

