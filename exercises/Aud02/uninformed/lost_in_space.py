# from uninformed.uninformed_search import *
# from uninformed.problem import Problem
#
#
# class Explorer(Problem):
#     def __init__(self, initial, goal=None):
#         super().__init__(initial, goal)
#         self.grid_size = (8, 6)
#
#     def successor(self, state):
#         successors = dict()
#         man_x = state[0]
#         man_y = state[1]
#         obstacle1 = list(state[2])
#         obstacle2 = list(state[3])
#         max_x = self.grid_size[0]
#         max_y = self.grid_size[1]
#         if obstacle1[2] == 0: #up
#             if(obstacle1[1] == max_y-1):  #change the way of moving (down)
#                 obstacle1[2] = -1
#                 obstacle1[1] -= 1
#             else:
#                 obstacle1[1] += 1
#         else: #down
#             if obstacle1[1] == 0:
#                 obstacle1[2] = 0
#                 obstacle1[1] += 1
#             else:
#                 obstacle1[1] -= 1
#
#         if obstacle2[2] == 0:  # up
#             if (obstacle2[1] == max_y - 1):  # change the way of moving (down)
#                 obstacle2[2] = -1
#                 obstacle2[1] -= 1
#             else:
#                 obstacle2[1] += 1
#         else:  # down
#             if obstacle2[1] == 0:
#                 obstacle2[2] = 0
#                 obstacle2[1] += 1
#             else:
#                 obstacle2[1] -= 1
#
#         if man_x < max_x - 1 and (man_x + 1, man_y) not in [obstacle1, obstacle2]:
#             successors['Right'] = (man_x + 1, man_y, tuple(obstacle1), tuple(obstacle2))
#
#         if man_x > 0 and (man_x - 1, man_y) not in [obstacle1, obstacle2]:
#             successors['Left'] = (man_x - 1, man_y, tuple(obstacle1), tuple(obstacle2))
#
#         if man_y < max_y - 1 and (man_x, man_y + 1) not in [obstacle1, obstacle2]:
#             successors['Up'] = (man_x, man_y + 1, tuple(obstacle1), tuple(obstacle2))
#
#         if man_y > 0 and (man_x, man_y - 1) not in [obstacle1, obstacle2]:
#             successors['Down'] = (man_x, man_y - 1, tuple(obstacle1), tuple(obstacle2))
#         return successors
#
#     def goal_test(self, state):
#         position = (state[0], state[1])
#         return position == self.goal
#
# if __name__ == "__main__":
#     goal_state = (7, 4)
#     initial_state = (0, 2)
#     obstacle_1 = (2, 0, -1) #down
#     obstacle_2 = (5, 0, 0) #up
#
#     explorer = Explorer((initial_state[0], initial_state[1], obstacle_1, obstacle_2), goal_state)
#     result = breadth_first_graph_search(explorer)
#     print(result.solution())
#     print(result.solve())

from SearchingFrameworks.uninformed_search import *
from SearchingFrameworks.utils import *



class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

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

        man_x = state[0]
        man_y = state[1]
        obstacle1 = [state[2], state[3], state[4]]
        obstacle2 = [state[5], state[6], state[7]]
        max_x = self.grid_size[0]
        max_y = self.grid_size[1]

        if obstacle1[2] == 0:  # up
            if obstacle1[1] == max_y - 1:
                obstacle1[2] = 1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1
        else:  # down
            if obstacle1[1] == 0:
                obstacle1[2] = 0
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1

        if obstacle2[2] == 0:  # up
            if obstacle2[1] == max_y - 1:
                obstacle2[2] = 1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else:  # down
            if obstacle2[1] == 0:
                obstacle2[2] = 0
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        # obstacle1_pos = [obstacle1[0], obstacle1[1]]
        # obstacle2_pos = [obstacle2[0], obstacle2[1]]
        obstacles = [[obstacle1[0], obstacle1[1]], [obstacle2[0], obstacle2[1]]]

        if man_x < max_x - 1 and [man_x + 1, man_y] not in obstacles:  # right
            successors['Right'] = (man_x + 1, man_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_x > 0 and [man_x - 1, man_y] not in obstacles:  # left
            successors['Left'] = (man_x - 1, man_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y < max_y - 1 and [man_x, man_y + 1] not in obstacles:  # up
            successors['Up'] = (man_x, man_y + 1,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y > 0 and [man_x, man_y - 1] not in obstacles:  # down
            successors['Down'] = (man_x, man_y - 1,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

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
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        position = (state[0], state[1])
        return position == self.goal


if __name__ == '__main__':
    goal_state = (7, 4)
    initial_state = (0, 2)
    obstacle_1 = (2, 5, 1)  # down
    obstacle_2 = (5, 0, 0)  # up
    # man_x = int(input())
    # man_y = int(input())
    # house_x = int(input())
    # house_y = int(input())
    # house = [house_x, house_y]
    # informed_explorer = Explorer((man_x, man_x, 2, 5, -1, 5, 0, 1), house)

    explorer = Explorer((initial_state[0], initial_state[1],
                         obstacle_1[0], obstacle_1[1], obstacle_1[2],
                         obstacle_2[0], obstacle_2[1], obstacle_2[2]), goal_state)

    result = breadth_first_graph_search(explorer)
    print(result.solution())
    # print(breadth_first_graph_search(explorer).solution())
    # print(breadth_first_graph_search(explorer).solve())