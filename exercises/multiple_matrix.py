# def multiply_element(element, i, n):
#     if i < n / 2:
#         return element * 2
#     else:
#         return element * 3
#

if __name__ == "__main__":
    line = input()
    split_line = line.split(" ")
    n = int(split_line.pop(0))
    m = int(split_line.pop(0))
    elements_matrix = []
    # half_n = n // 2
    # print(half_n)
    for i in range(n):
        elements_row = [int(element) for element in split_line]
        elements_matrix.append(elements_row)
    # solution_matrix = [[multiply_element(elements_matrix[i][j], i, n) for j in range(m)]for i in range(n)]
    solution_matrix1 = [[elements_matrix[i][j]*2 if i < n/2 else elements_matrix[i][j]*3 for j in range(m)]for i in range(n)]
    # print(solution_matrix)
    print(solution_matrix1)
