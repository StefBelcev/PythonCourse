from abc import ABC

from SearchingFrameworks import *


# 1   2   3   4
# 5   6   7   8
# 9   10  11  12
# 13  14  15  16


class GraphExplorer(Problem, ABC):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        player = state[0]
        # star1 = state[1][0]
        # star2 = state[1][1]
        links = state[2]

        successors = dict()

        # Gore
        if player - 4 >= 1 and (player - 4, player) in links or (player, player - 4) in links:
            stars = tuple([x for x in state[1] if x != player - 4])
            new_links = [x for x in links if x != (player - 4, player) and (player, player - 4)]
            successors["Gore"] = player - 4, stars, new_links

        # Dole
        if player + 4 <= 16 and (player + 4, player) in links or (player, player + 4) in links:
            stars = tuple([x for x in state[1] if x != player + 4])
            new_links = [x for x in links if x != (player + 4, player) and (player, player + 4)]
            successors["Dole"] = player + 4, stars, new_links

        # Levo
        if player % 4 != 1 and (player - 1, player) in links or (player, player - 1) in links:
            stars = tuple([x for x in state[1] if x != player - 1])
            new_links = [x for x in links if x != (player - 1, player) and (player, player - 1)]
            successors["Levo"] = player - 1, stars, new_links

        # Desno
        if player % 4 != 0 and (player + 1, player) in links or (player, player + 1) in links:
            stars = tuple([x for x in state[1] if x != player + 1])
            new_links = [x for x in links if x != (player + 1, player) and (player, player + 1)]
            successors["Desno"] = player + 1, stars, new_links

        # Gorelevo
        if player % 4 != 1 and player - 5 >= 1 and (player - 5, player) in links or (player, player - 5) in links:
            stars = tuple([x for x in state[1] if x != player - 5])
            new_links = [x for x in links if x != (player - 5, player) and (player, player - 5)]
            successors["Gorelevo"] = player - 5, stars, new_links

        # Doledesno
        if player % 4 != 0 and player + 5 <= 16 and (player + 5, player) in links or (
                player, player - 5) in links:
            stars = tuple([x for x in state[1] if x != player + 5])
            new_links = [x for x in links if x != (player + 5, player) and (player, player + 5)]
            successors["Dole edesno"] = player + 5, stars, new_links

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)

    def goal_test(self, state):
        return len(list(state[1])) == 0

    @staticmethod
    def euclidean(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

    def h(self):
        pass


if __name__ == '__main__':
    player_position11 = int(input())
    star11 = int(input())
    star22 = int(input())
    player_position = 4
    star1 = 1
    star2 = 16
    graphToExplore = range(1, 17)
    # print(matrix)
    links = ((1, 2), (1, 5), (2, 6), (5, 6), (6, 7), (6, 10), (6, 11), (3, 7), (3, 4), (7, 8), (4, 8), (9, 13), (9, 10),
             (10, 14), (13, 14), (10, 14), (10, 11), (7, 11), (11, 15), (15, 16), (12, 16), (8, 12))
    initial_state = (player_position, (star1, star2), links)
    problem = Problem(initial_state)
    astar_search(problem)

