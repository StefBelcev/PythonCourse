from Aud02.uninformed.uninformed_search import *
from Aud02.uninformed.utils import Problem

# Functions for moving Pacman:

# ProdolzhiPravo
# istok: new_x = x + 1; new_y = y; new_direction = istok
# sever: new_x = x ; new_y = y + 1; new_direction = sever
# zapad: new_x = x - 1; new_y = y; new_direction = zapad
# jug: new_x = x; new_y = y - 1; new_direction = jug


def ProdolzhiPravo(x, y, direction, obstacles):
    if direction == 'istok':
        if x < 9 and [x + 1, y] != [x, y] and [x + 1, y] not in obstacles:
            x = x + 1
            y = y
            direction = 'istok'
        return x, y, direction
    elif direction == 'sever':
        if y < 9 and [x, y + 1] != [x, y] and [x, y + 1] not in obstacles:
            x = x
            y = y + 1
            direction = 'sever'
        return x, y, direction
    elif direction == 'zapad':
        if x > 0 and [x - 1, y] != [x, y] and [x - 1, y] not in obstacles:
            x = x - 1
            y = y
            direction = 'zapad'
        return x, y, direction
    elif direction == 'jug':
        if y > 0 and [x, y - 1] != [x, y] and [x, y - 1] not in obstacles:
            x = x
            y = y - 1
            direction = 'jug'
        return x, y, direction


# ProdolzhiNazad
# istok: new_x = x - 1; new_y = y; new_direction = zapad
# sever: new_x = x ; new_y = y - 1; new_direction = jug
# zapad: new_x = x + 1; new_y = y; new_direction = istok
# jug: new_x = x; new_y = y + 1; new_direction = sever

def ProdolzhiNazad(x, y, direction, obstacles):
    if direction == 'istok':
        if x > 0 and [x - 1, y] != [x, y] and [x - 1, y] not in obstacles:
            x = x - 1
            y = y
            direction = 'zapad'
        return x, y, direction
    elif direction == 'sever':
        if y > 0 and [x, y - 1] != [x, y] and [x, y - 1] not in obstacles:
            x = x
            y = y - 1
            direction = 'jug'
        return x, y, direction
    elif direction == 'zapad':
        if x < 9 and [x + 1, y] != [x, y] and [x + 1, y] not in obstacles:
            x = x + 1
            y = y
            direction = 'istok'
        return x, y, direction
    elif direction == 'jug':
        if y < 9 and [x, y + 1] != [x, y] and [x, y + 1] not in obstacles:
            x = x
            y = y + 1
            direction = 'sever'
        return x, y, direction


# SvrtiLevo
# istok: new_x = x; new_y = y + 1; new_direction = sever
# sever: new_x = x - 1 ; new_y = y; new_direction = zapad
# zapad: new_x = x ; new_y = y - 1; new_direction = jug
# jug: new_x = x + 1 ; new_y = y; new_direction = istok

def SvrtiLevo(x, y, direction, obstacles):
    if direction == 'istok':
        if y < 9 and [x, y + 1] != [x, y] and [x, y + 1] not in obstacles:
            x = x
            y = y + 1
            direction = 'sever'
        return x, y, direction
    elif direction == 'sever':
        if x > 0 and [x - 1, y] != [x, y] and [x - 1, y] not in obstacles:
            x = x - 1
            y = y
            direction = 'zapad'
        return x, y, direction
    elif direction == 'zapad':
        if y > 0 and [x, y - 1] != [x, y] and [x, y - 1] not in obstacles:
            x = x
            y = y - 1
            direction = 'jug'
        return x, y, direction
    elif direction == 'jug':
        if x < 9 and [x + 1, y] != [x, y] and [x + 1, y] not in obstacles:
            x = x + 1
            y = y
            direction = 'istok'
        return x, y, direction


# SvrtiDesno
# istok: new_x = x; new_y = y - 1; new_direction = jug
# sever: new_x = x + 1 ; new_y = y; new_direction = istok
# zapad: new_x = x ; new_y = y + 1; new_direction = sever
# jug: new_x = x - 1 ; new_y = y; new_direction = zapad

def SvrtiDesno(x, y, direction, obstacles):
    if direction == 'istok':
        if y > 0 and [x, y - 1] != [x, y] and [x, y - 1] not in obstacles:
            x = x
            y = y - 1
            direction = 'jug'
        return x, y, direction
    elif direction == 'sever':
        if x < 9 and [x + 1, y] != [x, y] and [x + 1, y] not in obstacles:
            x = x + 1
            y = y
            direction = 'istok'
        return x, y, direction
    elif direction == 'zapad':
        if y < 9 and [x, y + 1] != [x, y] and [x, y + 1] not in obstacles:
            x = x
            y = y + 1
            direction = 'sever'
        return x, y, direction
    elif direction == 'jug':
        if x > 0 and [x - 1, y] != [x, y] and [x - 1, y] not in obstacles:
            x = x - 1
            y = y
            direction = 'zapad'
        return x, y, direction


class Pacman(Problem):

    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def value(self):
        pass

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = dict()

        p_x, p_y = state[0], state[1]
        p_direction = state[2]
        points_position = state[3]

        # Prodolzhi Pravo
        new_x, new_y, new_direction = ProdolzhiPravo(p_x, p_y, p_direction, self.obstacles)
        if [p_x, p_y] != [new_x, new_y]:
            successors['ProdolzhiPravo'] = (new_x, new_y, new_direction, tuple([s for s in points_position if
                                                                                s[0] != new_x or s[1] != new_y]))

        # Prodolzhi Nazad
        new_x, new_y, new_direction = ProdolzhiNazad(p_x, p_y, p_direction, self.obstacles)
        if [p_x, p_y] != [new_x, new_y]:
            successors['ProdolzhiNazad'] = (new_x, new_y, new_direction, tuple([s for s in points_position if
                                                                                s[0] != new_x or s[1] != new_y]))

        # Svrti Levo
        new_x, new_y, new_direction = SvrtiLevo(p_x, p_y, p_direction, self.obstacles)
        if [p_x, p_y] != [new_x, new_y]:
            successors['SvrtiLevo'] = (new_x, new_y, new_direction, tuple([s for s in points_position if
                                                                           s[0] != new_x or s[1] != new_y]))

        # Svrti Desno
        new_x, new_y, new_direction = SvrtiDesno(p_x, p_y, p_direction, self.obstacles)
        if [p_x, p_y] != [new_x, new_y]:
            successors['SvrtiDesno'] = (new_x, new_y, new_direction, tuple([s for s in points_position if
                                                                           s[0] != new_x or s[1] != new_y]))

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        possible = self.successor(state)
        return possible[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return len(state[3]) == 0

    @staticmethod
    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def h(self, node):
        pacman = list((node.state[0], node.state[1]))
        dots = node.state[3]

        distances = []
        for dot in dots:
            a = Pacman.dist(pacman, dot)
            distances.append(a)

        if len(distances) > 0:
            temp = max(distances)
        else:
            temp = 0
        return temp


if __name__ == '__main__':
    obstacles_list = [[0, 6], [0, 8], [0, 9], [1, 2], [1, 3], [1, 4], [1, 9], [2, 9],
                      [3, 6], [3, 9], [4, 1], [4, 5], [4, 6], [4, 7], [5, 1], [5, 6],
                      [6, 0], [6, 1], [6, 2], [6, 9], [8, 1], [8, 4], [8, 7], [8, 8],
                      [9, 4], [9, 7], [9, 8]]


    pacman_x = int(input())
    pacman_y = int(input())

    direction_input = input()

    num_points = int(input())
    list_points = []

    for i in range(num_points):
        list_points.append(tuple(int(x.strip()) for x in input().split(',')))

    points_pos = tuple(list_points)
    print(points_pos)
    pacman = Pacman(obstacles_list, (pacman_x, pacman_y, direction_input, points_pos))
    result = breadth_first_graph_search(pacman)

    print(result.solution())

