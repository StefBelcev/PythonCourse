if __name__ == "__main__":
    line = input()
    split_line = line.split(" ")
    n = int(split_line.pop(0))
    m = int(split_line.pop(0))
    print(n, m)
    print(split_line)
    element_matrix = []
    for i in range(n):
        element_row = [int(element) for element in split_line]
        # casting elements from split_line list to an row of the matrix
        element_matrix.append(element_row)
    matrix = [[element_matrix[i][j] * 2 for j in range(m)] for i in range(n)]
    print(matrix)
