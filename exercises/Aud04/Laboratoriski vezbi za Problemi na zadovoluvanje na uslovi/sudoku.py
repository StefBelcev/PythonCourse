# Судоку Problem 2 (0 / 2)
# Дадена ви е играта судоку. Во оваа игра во секој блок се ставаат бројки од 1 до 9 така што во ниедна редица, колона и блок не смее да се повторува ниедна цифра. Почетно сите полиња се празни. Вашата задача е да најдете решение на овој проблем. Просторот ви е даден на сликата подолу.
#
# Забелешка: На влез добивате со каков Solver да работите. Испечатете го само првото решение. Не е задолжително да ви поминуваат сите тест примери за задачата да биде точна. Зависи како сте ги поставиле условите.
from constraint import *

if __name__ == '__main__':
    # problem = Problem(BacktrackingSolver())
    # # variables = []
    # # for variable in variables:
    # #     problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------
    algorithm = str(input())
    problem = Problem(algorithm)
    variables = range(1, 10)
    domain = range(81)
    # for i in range(9):
    #     for j in range(9):
    #         domain.append((i, j))
    problem.addVariables(variables, domain)

    # 0   1   2   3   4   5   6   7   8
    # 9   10  11  12  13  14  15  16  17
    # 18  19  20  21  22  23  24  25  26
    # 27  28  29  30  31  32  33  34  35
    # 36  37  38  39  40  41  42  43  44
    # 45  46  47  48  49  50  51  52  53
    # 54  55  56  57  58  59  60  61  62
    # 63  64  65  66  67  68  69  70  71
    # 72  73  74  75  76  77  78  79  80
    # site razlicni vo eden red za site 9 reda i sumata na site clenovi vo redot treba da e 45
    for row in range(9):
        problem.addConstraint(AllDifferentConstraint(), [row * 9 + i for i in range(9)])
    # for i in range(9):
        # problem.addConstraint(AllDifferentConstraint(), variables)
    # for i in range(9,18):
    # site razlicni vo edna kolona za site 9 koloni i sumata na site clenovi vo kolonata treba da e 45
    for col in range(9):
        problem.addConstraint(AllDifferentConstraint(), [col + i * 9 for i in range(9)])
    for col in range(3):
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(3)])
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(3, 5)])
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(6, 9)])
    for col in range(3, 6):
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(3)])
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(3, 5)])
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(6, 9)])
    for col in range(6, 9):
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(3)])
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(3, 5)])
        problem.addConstraint(AllDifferentConstraint(), [col * 9 + i for i in range(6, 9)])

    print(problem.getSolution())

# if __name__ == '__main__':
#     algorithm = str(input())
#     problem = Problem(algorithm)
#     variables = range(1, 10)
#     domain = range(81)
#     # for i in range(9):
#     #     for j in range(9):
#     #         domain.append((i, j))
#     problem.addVariables(variables, domain)
#
#     # 0   1   2   3   4   5   6   7   8
#     # 9   10  11  12  13  14  15  16  17
#     # 18  19  20  21  22  23  24  25  26
#     # 27  28  29  30  31  32  33  34  35
#     # 36  37  38  39  40  41  42  43  44
#     # 45  46  47  48  49  50  51  52  53
#     # 54  55  56  57  58  59  60  61  62
#     # 63  64  65  66  67  68  69  70  71
#     # 72  73  74  75  76  77  78  79  80
#     # site razlicni vo eden red za site 9 reda i sumata na site clenovi vo redot treba da e 45
#     for row in range(9):
#         problem.addConstraint(ExactSumConstraint(45), [row * 9 + i for i in range(9)])
#         problem.addConstraint(AllDifferentConstraint())
#     # site razlicni vo edna kolona za site 9 koloni i sumata na site clenovi vo kolonata treba da e 45
#     for col in range(9):
#         problem.addConstraint(ExactSumConstraint(45), [col + i * 9 for i in range(9)])
#         problem.addConstraint(AllDifferentConstraint())
#     for col in range(3):
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(3)])
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(3, 5)])
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(6, 9)])
#         problem.addConstraint(AllDifferentConstraint())
#     for col in range(3, 6):
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(3)])
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(3, 5)])
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(6, 9)])
#         problem.addConstraint(AllDifferentConstraint())
#     for col in range(6, 9):
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(3)])
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(3, 5)])
#         problem.addConstraint(ExactSumConstraint(45), [col * 9 + i for i in range(6, 9)])
#         problem.addConstraint(AllDifferentConstraint())
#
#     solution = problem.getSolution()
#     print(solution)
# # TREBA DA SE DORESHI