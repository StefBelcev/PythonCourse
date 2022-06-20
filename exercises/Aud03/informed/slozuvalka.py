from Aud02.uninformed.utils import Problem
from Aud03.informed.informed_search import greedy_best_first_graph_search, recursive_best_first_search, astar_search


class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        """
        '*32415678'
        0 1 2 - prvi tri na prva redica
        3 4 5 - vtori tri na vtora redica
        6 7 8 - treti tri na treta redica
        """
        successors = dict()
        ind = state.index('*')
        # index na prazno pole
        if ind >= 3:
            # pomestuvanje nagore ili namaluvanje na indeksot za 3
            temp = list(state)
            temp[ind], temp[ind - 3] = temp[ind - 3], temp[ind]
            new_state = ''.join(temp) # spojuvanje
            successors['Gore'] = new_state

        # pomestuvanje nadole ili zgolemuvanje na indeksot za 3
        if ind <= 5:
            # pomestuvanje nagore ili namaluvanje na indeksot za 3
            temp = list(state)
            temp[ind], temp[ind + 3] = temp[ind + 3], temp[ind]
            new_state = ''.join(temp) # spojuvanje
            successors['Dole'] = new_state
        # pomestuvanje nalevo ili namaluvanje na indeksot za 1
        if ind % 3 != 0:
            temp = list(state)
            temp[ind], temp[ind - 1] = temp[ind - 1], temp[ind]
            new_state = ''.join(temp)
            successors['Levo'] = new_state
        # pomestuvanje nadesno ili zgolemuvanje na indeksot za 1
        if ind % 3 != 2:
            temp = list(state)
            temp[ind], temp[ind + 1] = temp[ind + 1], temp[ind]
            new_state = ''.join(temp)
            successors['Desno'] = new_state
        return successors

    def h(self, node):
        counter = 0
        """
        Obicna hevretika so kolku slozuvalki se na razlicno mesto
        """
        for x, y in zip(node.state, self.goal):
            if x != y:
                counter += 1
        return counter

    def actions(self, state):
        return self.successor (state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


class Puzzle_h2(Puzzle):
    coordinates = {0: (0, 2), 1: (1, 2), 2: (2, 2), 3: (0, 1), 4: (1, 1), 5: (2, 1), 6: (0, 0), 7: (1, 0), 8: (2, 0)}
    #koordinati za dadenite indeksi od stringot
    """
            '*32415678'
            0 1 2 - prvi tri na prva redica
            3 4 5 - vtori tri na vtora redica
            6 7 8 - treti tri na treta redica
            """
    @staticmethod
    def mnd(m, n):
        x1, y1 = Puzzle_h2.coordinates[m]
        x2, y2 = Puzzle_h2.coordinates[n]
        return abs(x1 - x2) + abs(y1 - y2)

    def h(self, node):
        total_sum = 0
        for x in '12345678':
            val = Puzzle_h2.mnd(node.state.index(x), int(x))
            total_sum += val
        return total_sum
zip()

if __name__ == "__main__":
    puzzle = Puzzle('*32415678', '*12345678')
    result1 = greedy_best_first_graph_search(puzzle)
    print(result1.solution())
    print(result1.solve())
    result2 = astar_search(puzzle)
    print(result2.solution())
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solve())

    puzzle = Puzzle_h2('*32415678', '*12345678')
    result1 = greedy_best_first_graph_search(puzzle)
    print(result1.solution())
    print(result1.solve())
    result2 = astar_search(puzzle)
    print(result2.solution())
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solve())