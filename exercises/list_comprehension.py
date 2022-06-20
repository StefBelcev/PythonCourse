if __name__ == "__main__":
    #First example in exercises
    li = [3, 6, 2, 7]
    li = [elem*2 for elem in li if (elem % 2 == 0)]
    print(li)
    #Second example in exercises
    list_ex1 = [('a', 1), ('b', 2), ('c', 7)]
    lc_list_ex1 = [ n*3 for (x, n) in li]
    print(lc_list_ex1)
    #My example
    li1 = [3, 2, 4, 1]
    li2 = [elem * 2 for elem in [item + 1 for item in li1]]
    print(li2)
    #Another my example
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(list_of_lists)
    for list in list_of_lists:
        print(list)
        for x in list:
            print(x)
    #Third example in exercises
    def subtract(a, b):
        return a - b
    oplist = [(6, 3), (1, 7), (5, 5)]
    result = [subtract(b, a) for (a, b) in oplist]
    print(result)
    #Nested List Compreshension
    list_nested = [3, 2, 4, 1]
    list_nested_res = [elem*2 for elem in
                       [item+1 for item in list_nested]]
    print(list_nested_res)
    #Example for creating matrix with List Comprehension
    list_1_10 = [i for i in range(10)]
    list_example_matrix = [[j+1 for j in range(3*i, 3*i+3)] for i in range(3)]

    n = 5
    matrix = [[0 for j in range(n)] for i in range(n)]
    print(list_1_10)
    print(list_example_matrix)
    print(matrix)