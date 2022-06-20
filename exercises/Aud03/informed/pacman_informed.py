from Aud03.informed.informed_search import astar_search
from Aud02.uninformed.utils import Problem


class Pacman(Problem):
    def __init__(self, obstacle_list, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [10, 10]
        self.obstacle_list = obstacle_list

    def successor(self, state):
        successors = dict()
        maximum_x = self.grid_size[0]
        maximum_y = self.grid_size[1]
        man_x, man_y = state[0], state[1]
        side = state[2]
        dots = list(state[3])
        # dots_list = []
        # for d_x, d_y in dots:
        #     dots_list.append([d_x, d_y])
        # this should be added everywhere inside the if statements and [man_x, man_y] != [man_x + 1, man_y]
        if side == 'istok':
            if man_x < maximum_x - 1 and [man_x, man_y] != [man_x + 1, man_y] and [man_x + 1,
                                                                                   man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x + 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'istok'
                successors['ProdolzhiPravo'] = (man_x + 1, man_y, new_side, tuple(temp_dots))

            if man_x > 0 and [man_x, man_y] != [man_x - 1, man_y] and [man_x - 1, man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x - 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'zapad'
                successors['ProdolzhiNazad'] = (man_x - 1, man_y, new_side, tuple(temp_dots))

            if man_y < maximum_y - 1 and [man_x, man_y] != [man_x, man_y + 1] and [man_x,
                                                                                   man_y + 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y + 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'sever'
                successors['SvrtiLevo'] = (man_x, man_y + 1, new_side, tuple(temp_dots))

            if man_y > 0 and [man_x, man_y] != [man_x, man_y - 1] and [man_x, man_y - 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y - 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'jug'
                successors['SvrtiDesno'] = (man_x, man_y - 1, new_side, tuple(temp_dots))

        elif side == 'zapad':
            if man_x > 0 and [man_x, man_y] != [man_x - 1, man_y] and [man_x - 1, man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x - 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'zapad'
                successors['ProdolzhiPravo'] = (man_x - 1, man_y, new_side, tuple(temp_dots))

            if man_x < maximum_x - 1 and [man_x, man_y] != [man_x + 1, man_y] and [man_x + 1,
                                                                                   man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x + 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'istok'
                successors['ProdolzhiNazad'] = (man_x + 1, man_y, new_side, tuple(temp_dots))

            if man_y > 0 and [man_x, man_y] != [man_x, man_y - 1] and [man_x, man_y - 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y - 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'jug'
                successors['SvrtiLevo'] = (man_x, man_y - 1, new_side, tuple(temp_dots))

            if man_y < maximum_y - 1 and [man_x, man_y] != [man_x, man_y + 1] and [man_x,
                                                                                   man_y + 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y + 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'sever'
                successors['SvrtiDesno'] = (man_x, man_y + 1, new_side, tuple(temp_dots))

        elif side == 'sever':
            if man_y < maximum_y - 1 and [man_x, man_y] != [man_x, man_y + 1] and [man_x,
                                                                                   man_y + 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y + 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'sever'
                successors['ProdolzhiPravo'] = (man_x, man_y + 1, new_side, tuple(temp_dots))

            if man_y > 0 and [man_x, man_y] != [man_x, man_y - 1] and [man_x, man_y - 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y - 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'jug'
                successors['ProdolzhiNazad'] = (man_x, man_y - 1, new_side, tuple(temp_dots))

            if man_x > 0 and [man_x, man_y] != [man_x - 1, man_y] and [man_x - 1, man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x - 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'zapad'
                successors['SvrtiLevo'] = (man_x - 1, man_y, new_side, tuple(temp_dots))

            if man_x < maximum_x - 1 and [man_x, man_y] != [man_x + 1, man_y] and [man_x + 1,
                                                                                   man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x + 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'istok'
                successors['SvrtiDesno'] = (man_x + 1, man_y, new_side, tuple(temp_dots))

        elif side == 'jug':
            if man_y > 0 and [man_x, man_y] != [man_x, man_y - 1] and [man_x, man_y - 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y - 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'jug'
                successors['ProdolzhiPravo'] = (man_x, man_y - 1, new_side, tuple(temp_dots))

            if man_y < maximum_y - 1 and [man_x, man_y] != [man_x, man_y + 1] and [man_x,
                                                                                   man_y + 1] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x, man_y + 1]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'sever'
                successors['ProdolzhiNazad'] = (man_x, man_y + 1, new_side, tuple(temp_dots))

            if man_x < maximum_x - 1 and [man_x, man_y] != [man_x + 1, man_y] and [man_x + 1,
                                                                                   man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x + 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'istok'
                successors['SvrtiLevo'] = (man_x + 1, man_y, new_side, tuple(temp_dots))

            if man_x > 0 and [man_x, man_y] != [man_x - 1, man_y] and [man_x - 1, man_y] not in self.obstacle_list:
                temp_dots = []
                dots_list_temp = []
                for d_x, d_y in dots:
                    dots_list_temp.append([d_x, d_y])
                temp = [man_x - 1, man_y]
                if temp in dots_list_temp:
                    dots_list_temp.remove(temp)
                for d_x, d_y in dots_list_temp:
                    temp_dots.append(tuple((d_x, d_y)))
                new_side = 'zapad'
                successors['SvrtiDesno'] = (man_x - 1, man_y, new_side, tuple(temp_dots))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        dots = state[3]
        return len(dots) == 0

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


if __name__ == "__main__":
    p_x = int(input())
    p_y = int(input())
    p_side = str(input())
    initial_p = [p_x, p_y, p_side]
    obstacles = [[0, 6], [0, 8], [0, 9], [1, 9], [2, 9], [3, 9], [1, 2], [1, 3], [1, 4], [3, 6], [4, 1], [4, 5],
                 [4, 6], [4, 7], [5, 1], [5, 6], [6, 0], [6, 1], [6, 2], [6, 9], [8, 1], [8, 4], [8, 7], [8, 8],
                 [9, 4], [9, 7], [9, 8]]
    n_dots = int(input())
    i = 0
    list_dots = []
    while i < n_dots:
        line = input()
        # my way
        list_dots.append(tuple(map(int, line.split(','))))
        i += 1
    tuple_dots = tuple(list_dots)
    pacman = Pacman(obstacles, (initial_p[0], initial_p[1], initial_p[2], tuple_dots))
    result = astar_search(pacman)
    print(result.solution())
