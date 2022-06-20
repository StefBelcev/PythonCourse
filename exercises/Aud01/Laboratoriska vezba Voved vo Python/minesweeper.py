# Minesweeper Problem 2 (1 / 9)
# Овој проблем се базира на играта Minesweeper.
#
# Креирајте функција која како влез зема листа од # и -, каде што секој хаш знак (#) претставува мина,
# а секоја цртичка (-) претставува поле без мина. Функцијата треба да враќа листа каде што секоја цртичка
# е заменета со бројка која го претставува бројот на мини од најблиските полиња на моменталното поле
# (хоризонтално, вертикално, и дијагонално). Листата која се враќа на излез креирајте ја со пристапот
# list comprehension.
#
# Од стандарден влез е дадена големината на полето N (полето е со димензии NxN), како и репрезентацијата
# на полето со # и -. Потребно е да направите репрезентација на полето преку листа од листи,
# каде што елементите се # и -. Оваа листа е влез на претходно дефинираната функција,
# а излезот од функцијата е потребно да се испечати од стандарден влез.
#
# Помош: влезот е зададен ред по ред за секоја редица во полето, додека индивидуалните елементи се
# одвоени со 3 празни места. За да се одделат елементите со 3 празни места, може да ја искористите
# функцијата split() дефинирана на стрингови. За печатење на излезот може да ја користите функцијата
# join() дефинирана на стрингови.
if __name__ == "__main__":
        n = int(input())
        single_line = []
        for i in range(0, n):
            line = input()
            single_line.append(list(map(str, line.split('   '))))
        print(f'{single_line}')
        solution = []
        for i in range(0, n):
            temp = []
            for j in range(0, n):
                temp.append(0)
            solution.append(temp)

        for x in range(0, n):
            for y in range(0, n):
                if single_line[x][y] == '-':
                    if x > 0:
                        if single_line[x - 1][y] == '#': # up
                            solution[x][y] += 1
                    if x < n-1:
                        if single_line[x + 1][y] == '#': #down
                            solution[x][y] += 1
                    if y < n-1:
                        if single_line[x][y + 1] == '#': #right
                            solution[x][y] += 1
                    if y > 0:
                        if single_line[x][y - 1] == '#': #left
                            solution[x][y] += 1
                    if x > 0 and y < n-1:
                        if single_line[x - 1][y + 1] == '#': #up right
                            solution[x][y] += 1
                    if x < n-1 and y > 0:
                        if single_line[x + 1][y - 1] == '#': #down left
                            solution[x][y] += 1
                    if x < n-1 and y < n-1:
                        if single_line[x + 1][y + 1] == '#': #down right
                            solution[x][y] += 1
                    if x > 0 and y > 0:
                        if single_line[x - 1][y - 1] == '#': #up left
                            solution[x][y] += 1
                    else:
                        solution[x][y] += 0
                else:
                    solution[x][y] = '#'

        solution1 = ''
        for x in range(0, n):
            for y in range(0, n):
                if y == 0:
                    solution1 += str(solution[x][y])
                else:
                    solution1 += '   ' + str(solution[x][y])
            if x == n-1:
                solution1 += ''
            else:
                solution1 += '\n'
        print(solution1)