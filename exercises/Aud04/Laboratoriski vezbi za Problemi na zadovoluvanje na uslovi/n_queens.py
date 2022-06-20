from constraint import *

# N-Кралици Problem 1 (2 / 5)
# Дадена е nxn табла за шах. Треба да се постават n кралици на таблата така што ниедна кралица да не се напаѓа. Кралиците може да се постават на било која позиција која сметаме дека е најсоодветна. Единственото ограничување е дека не треба да се напаѓаат. Можните придвижувања на кралицата ви се дадени на сликата подолу:
#
# enter image description here
#
# На влез се прима бројот на кралици и димензии на таблата n. На излез треба да се испечати бројот на уникатни позиции на кои може да ги
#поставете кралиците со default Backtracking Solver ако бројот на кралици е помал или еднаков на 6. Во спротивно да се испечати само првото решение.
# Забелешка: За кралиците да не се напаѓаат треба да се провери нивната редица, колона или дијагонала. Не е задолжително да ви поминуваат последните два тест примери за задачата да биде точна. Зависи како сте ги поставиле условите.
if __name__ == '__main__':
    n = int(input())
    problem = Problem()
    domain = []
    for i in range(n):
        for j in range(n):
            domain.append((i, j))
    queens = range(1, n + 1)
    problem.addVariables(queens, domain)
    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(lambda q1, q2:
                                      abs(q1[0] - q2[0]) != abs(q1[1] - q2[1]) and
                                      q1[0] != q2[0] and q1[1] != q2[1], (queen1, queen2))
    if n <= 6:
        solutions = problem.getSolutions()
        number_sol = len(solutions)
        print(number_sol)
    else:
        solution = problem.getSolution()
        print(solution)