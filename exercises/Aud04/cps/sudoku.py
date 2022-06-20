from constraint import *

if __name__ == '__main__':
    algorithm = str(input())
    problem = Problem()
    variables = range(1, 10)
    domain = []
    for i in range(9):
        for j in range(9):
            domain.append((i, j))
    problem.addVariables(variables, domain)
    rows = [(i, j) for j in range(9) for i in range(9)]
    columns = [(i, j) for i in range(9) for j in range(9)]
    square1 = [(i, j) for j in range(3) for i in range(3)]
    square2 = [(i, j) for j in range(3, 6) for i in range(3)]
    square3 = [(i, j) for j in range(6, 9) for i in range(3)]
    square4 = [(i, j) for j in range(3) for i in range(3, 6)]
    square5 = [(i, j) for j in range(3, 6) for i in range(3, 6)]
    square6 = [(i, j) for j in range(6, 9) for i in range(3, 6)]
    square7 = [(i, j) for j in range(3) for i in range(6, 9)]
    square8 = [(i, j) for j in range(3, 6) for i in range(6, 9)]
    square9 = [(i, j) for j in range(6, 9) for i in range(6, 9)]
    problem.addConstraint(rows, variables)
    problem.addConstraint(columns, variables)
    problem.addConstraint(square1, variables)
    problem.addConstraint(square2, variables)
    problem.addConstraint(square3, variables)
    problem.addConstraint(square4, variables)
    problem.addConstraint(square5, variables)
    problem.addConstraint(square6, variables)
    problem.addConstraint(square7, variables)
    problem.addConstraint(square8, variables)
    problem.addConstraint(square9, variables)

    solution = problem.getSolution()
    print(solution)
