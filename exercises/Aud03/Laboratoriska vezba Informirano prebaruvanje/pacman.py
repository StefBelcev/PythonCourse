# Предложете соодветна репрезентација на играта Pacman и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на Слика 1:
#
# enter image description here
#
# Слика 1
#
# "Во табла со димензии 10x10 се наоѓа човече. Човечето може да се придвижува на кое било соседно поле хоризонтално или вертикално, доколку на соодветната позиција не постои пречка. Потребно е човечето да ги изеде сите точки поставени во таблата. Во даден момент можни се четири акции на движење на човечето: продолжи право, продолжи назад, сврти лево и сврти десно. На Слика 2 се прикажани можните движења на човечето за две насоки, каде што со сина боја е обележана новата позиција добиена со акцијата продолжи право, продолжи назад со црвена боја, сврти лево со сива боја и сврти десно со зелена боја. Потребно е проблемот да се реши во најмал број на потези."
#
# enter image description here
#
# Слика 2
#
# За сите тест примери изгледот и големината на таблата се исти како на примерот даден на Слика 1. За сите тест примери позициите на пречките се исти. За секој тест пример почетната позиција на човечето се менува, а исто така се менуваат и позиците на точките.
#
# Од стандарден влез се читаат почетните x и y координати во кои на почетокот се наоѓа човечето (ако таблата ја гледате во стандардниот координатен систем). Следно се чита насоката кон која е поставен играчот ('istok', 'zapad', 'sever', 'jug'). Потоа се чита број на точки во таблата, по што во секој нов ред се читаат x и y координатите на точките во таблата (ако таблата ја гледате во стандардниот координатен систем).
#
# Движењата на човечето потребно е да ги именувате на следниот начин:
#
# ProdolzhiPravo - за придвижување на човечето за едно поле нанапред
# ProdolzhiNazad - за придвижување на човечето за едно поле наназад
# SvrtiLevo - за придвижување на човечето за едно поле налево
# SvrtiDesno - за придвижување на човечето за едно поле надесно
# Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на движења која човечето треба да ја направи за да може од својата почетна позиција да стигне до позицијата на куќичката. Треба да примените информирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите. Дефинирајте прифатлива хевристичка функција за информираниот алгоритам.
#
# Напомена: За различна хевристичка функција може да добиете различно оптимално решение кое не секогаш се поклопува со тест примерите.
import sys
import bisect
from sys import maxsize as infinity

infinity = float('inf')


class Queue:
    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        for item in items:
            self.append(item)


def Stack():
    return []


class FIFOQueue(Queue):
    def __init__(self):
        self.A = []
        self.start = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)

    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A) / 2:
            self.A = self.A[self.start:]
            self.start = 0
        return e

    def __contains__(self, item):
        return item in self.A[self.start:]


class PriorityQueue(Queue):
    def __init__(self, order=min, f=lambda x: x):
        self.A = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.A)

    def __getitem__(self, key):
        for _, item in self.A:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        raise NotImplementedError

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self):
        raise NotImplementedError


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next))

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def solve(self):
        return [node.state for node in self.path()[0:]]

    def path(self):
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        return list(reversed(result))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


def tree_search(problem, fringe):
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        print(node.state)
        if problem.goal_test(node.state):
            return node
        fringe.extend(node.expand(problem))
    return None


def breadth_first_tree_search(problem):
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    return tree_search(problem, Stack())


def graph_search(problem, fringe):
    closed = {}
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue())


def depth_first_graph_search(problem):
    return graph_search(problem, Stack())


def uniform_cost_search(problem):
    return graph_search(problem, PriorityQueue(lambda a, b: a.path_cost < b.path_cost))


def depth_limited_search(problem, limit=50):
    def recursive_dls(node, problem, limit):
        cutoff_occurred = False
        if problem.goal_test(node.state):
            return node
        elif node.depth == limit:
            return 'cutoff'
        else:
            for successor in node.expand(problem):
                result = recursive_dls(successor, problem, limit)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result != None:
                    return result
        if cutoff_occurred:
            return 'cutoff'
        else:
            return None

    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    for depth in range(sys.maxint):
        result = depth_limited_search(problem, depth)
        if result is not 'cutoff':
            return result


def memoize(fn, slot=None):
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        def memoized_fn(*args):
            if args not in memoized_fn.cache:
                memoized_fn.cache[args] = fn(*args)
            return memoized_fn.cache[args]

        memoized_fn.cache = {}
    return memoized_fn


def best_first_graph_search(problem, f):
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return None


def greedy_best_first_graph_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)


def astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


def recursive_best_first_search(problem, h=None):
    h = memoize(h or problem.h, 'h')

    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node, 0
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, infinity
        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)
        while True:
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = infinity
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f

    node = Node(problem.initial)
    node.f = h(node)
    result, bestf = RBFS(problem, node, infinity)
    return result


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
