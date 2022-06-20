from constraint import *

# можните вредности за секој топ се [(0,0), (0,1), (0,2)...]
# а променливите (топовите) ги именуваме со 1,2,3,4,5,6,7 и 8.
# Сега алгоритмот на секоај од овие променливи ќе долеи некоја од
# вредностите [(0,0), (0,1), (0,2)...].
# Со циклусот кажуваме: земи ја променливата 1,
# итерирај ги сите променливи и ако името на променливата
# е поголемо од 1, додади ограничување дека ако на променливата 1
# и се додели вредност (a,b) тогаш на втората не може да и се додели
# (а,x) или (x,b) каде што х е било која можна вредност 0-7
if __name__ == '__main__':

    problem = Problem()
    domain = []
    for i in range(0, 8):
        for j in range(0, 8):
            domain.append((i, j))

    domainLC = [[0 for j in range(8)] for i in range(8)]
    # rooks = range(1, 9)
    # problem.addVariables(rooks, domain)
    # First solution
    # for rook1 in rooks:
    #     for rook2 in rooks:
    #         if rook1 < rook2:
    #             problem.addConstraint(lambda r1, r2: r1[0] != r2[0] and r1[1] != r2[1], (rook1, rook2))

    # Second solution
    rooks = range(1, 9)
    domain1 = range(8)
    problem.addVariables(rooks, domain1)
    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 < rook2:
                problem.addConstraint(lambda r1, r2: r1 != r2, (rook1, rook2))

    # solution = problem.getSolution()
    solution1 = problem.getSolutions()
    # print(solution)
    # print(solution1)
    print(solution1)
    print(len(solution1))
