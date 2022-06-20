from constraint import *
# |Column = i col  + 4*i, col + 4*1
# |Column = 0 col + 4*0, col + 4, col + 8, col + 12
# |Column = 1 col + 4*1, col + 4+1, col + 4*2, col + 12
# |Column = 2 col + 4*2, col + 4, col + 8, col + 12
# |Column = 3 col + 4*3, col + 4, col + 8, col + 12
# 0   1   2   3 | ROW = 0 row + 0, row + 1, row + 2, row + 3
# 4   5   6   7 | Row = 1 row * 4 + 0, row *4  + 1, row*4 + 2, row*4 + 3
# 8   9   10  11| Row = 2 row + 8, row + 9, row + 10, row + 11
# 12  13  14  15| Row = 3 row + 12, row + 13, row + 14, row + 15


if __name__ == "__main__":
    problem = Problem()
    domain = range(1, 17)
    variables = range(16)
    problem.addVariables(variables, domain)
    problem.addConstraint(AllDifferentConstraint(), variables) # isto i vo sudoku vo blokot
    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(4)])
    # uslovi za 34 po redici
    sum_of_rows = []
    for row in range(4):
        sum_of_rows.append([row*4 + i for i in range(4)])
    sum_of_cols = []
    for column in range(4):
        sum_of_cols.append([i*4 + column for i in range(4)])

    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34), [col + i * 4 for i in range(4)]) # uslovi za 34 po koloni
    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
    #  glavna dijagonala
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))
    # sporedna dijagonala

    solution = problem.getSolution()
    solutions = problem.getSolutions()
    print(solution)
    print(len(solutions))
    