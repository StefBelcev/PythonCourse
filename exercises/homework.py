from Aud02.uninformed.uninformed_search import *

global m
global n


def move_right(p, y_other_pacman, g_other_pacman):
    x, y = p[0], p[1]
    yellow_other_pacman = [y_pacman for y_pacman in y_other_pacman if y_pacman[0] != x and y_pacman[1] != y]
    while x < m and ([x + 1, y] not in [yellow_other_pacman, g_other_pacman]):
        x += 1
    return x


def move_left(p, y_other_pacman, g_other_pacman):
    x, y = p[0], p[1]
    yellow_other_pacman = [y_pacman for y_pacman in y_other_pacman if y_pacman[0] != x and y_pacman[1] != y]
    while 0 < x and ([x - 1, y] not in [yellow_other_pacman, g_other_pacman]):
        x -= 1
    return x


def move_up(p, y_other_pacman, g_other_pacman):
    x, y = p[0], p[1]
    yellow_other_pacman = [y_pacman for y_pacman in y_other_pacman if y_pacman[0] != x and y_pacman[1] != y]
    while y < n and ([x, y + 1] not in [yellow_other_pacman, g_other_pacman]):
        y += 1
    return y


def move_down(p, y_other_pacman, g_other_pacman):
    x, y = p[0], p[1]
    yellow_other_pacman = [y_pacman for y_pacman in y_other_pacman if y_pacman[0] != x and y_pacman[1] != y]
    while 0 < y and ([x, y - 1] not in [yellow_other_pacman, g_other_pacman]):
        y -= 1
    return y


class Pacman(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        x_grid_size = m
        y_grid_size = n
        tuple_yellow_positions = state[0]
        yellow_initial_positions = list(state[0])
        yellow_pacman_positions_list = []
        for y_x, y_y in yellow_initial_positions:
            yellow_pacman_positions_list.append([y_x, y_y])
        tuple_green_positions = state[1]
        green_initial_positions = list(state[1])
        green_pacman_positions_list = []
        for g_x, g_y in green_initial_positions:
            green_pacman_positions_list.append([g_x, g_y])

        for yellow_pacman in yellow_pacman_positions_list:
            new_y = move_down(yellow_pacman, yellow_pacman_positions_list, green_pacman_positions_list)
            if yellow_pacman != [yellow_pacman[0], new_y]:
                yellow_pacman = [yellow_pacman[0], new_y]
                temp_yellow_pacman = []
                for temp_pacman in yellow_pacman_positions_list:
                    temp_yellow_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["DoleZholt"] = (tuple(temp_yellow_pacman), tuple_green_positions)

            new_y = move_up(yellow_pacman, yellow_pacman_positions_list, green_pacman_positions_list)
            if yellow_pacman != [yellow_pacman[0], new_y]:
                yellow_pacman = [yellow_pacman[0], new_y]
                temp_yellow_pacman = []
                for temp_pacman in yellow_pacman_positions_list:
                    temp_yellow_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["GoreZholt"] = (tuple(temp_yellow_pacman), tuple_green_positions)

            new_x = move_left(yellow_pacman, yellow_pacman_positions_list, green_pacman_positions_list)
            if yellow_pacman != [new_x, yellow_pacman[1]]:
                yellow_pacman = [new_x, yellow_pacman[1]]
                temp_yellow_pacman = []
                for temp_pacman in yellow_pacman_positions_list:
                    temp_yellow_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["LevoZholt"] = (tuple(temp_yellow_pacman), tuple_green_positions)

            new_x = move_right(yellow_pacman, yellow_pacman_positions_list, green_pacman_positions_list)
            if yellow_pacman != [new_x, yellow_pacman[1]]:
                yellow_pacman = [new_x, yellow_pacman[1]]
                temp_yellow_pacman = []
                for temp_pacman in yellow_pacman_positions_list:
                    temp_yellow_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["DesnoZholt"] = (tuple(temp_yellow_pacman), tuple_green_positions)


        for green_pacman in green_pacman_positions_list:
            new_y = move_down(green_pacman, green_pacman_positions_list, yellow_pacman_positions_list)
            if green_pacman != [green_pacman[0], new_y]:
                green_pacman = [green_pacman[0], new_y]
                temp_green_pacman = []
                for temp_pacman in green_pacman_positions_list:
                    temp_green_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["DoleZelen"] = (tuple_yellow_positions, tuple(temp_green_pacman))

            new_y = move_up(green_pacman, green_pacman_positions_list, yellow_pacman_positions_list)
            if green_pacman != [green_pacman[0], new_y]:
                green_pacman = [green_pacman[0], new_y]
                temp_green_pacman = []
                for temp_pacman in green_pacman_positions_list:
                    temp_green_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["GoreZelen"] = (tuple_yellow_positions, tuple(temp_green_pacman))

            new_x = move_left(green_pacman, green_pacman_positions_list, yellow_pacman_positions_list)
            if green_pacman != [new_x, green_pacman[1]]:
                green_pacman = [new_x, green_pacman[1]]
                temp_green_pacman = []
                for temp_pacman in green_pacman_positions_list:
                    temp_green_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["LevoZelen"] = (tuple_yellow_positions, tuple(temp_green_pacman))

            new_x = move_right(green_pacman, green_pacman_positions_list, yellow_pacman_positions_list)
            if green_pacman != [new_x, green_pacman[1]]:
                green_pacman = [new_x, green_pacman[1]]
                temp_green_pacman = []
                for temp_pacman in yellow_pacman_positions_list:
                    temp_green_pacman.append((temp_pacman[0], temp_pacman[1]))
                successors["DesnoZelen"] = (tuple_yellow_positions, tuple(temp_green_pacman))
        return successors

    def value(self):
        pass

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    grid = [m, n]
    # matrix = []
    # for i in range(1, m+1):
    #     for j in range(1, n+1):
    #         matrix.append((i, j))
    # matrix = tuple(matrix)
    k = int(m/2)
    # Defining yellow and green pacman initial and goal position
    yellow_pacman_goal_positions = [] # Yellow pacman goal position
    green_pacman_goal_positions = [] # Green pacman goal position
    yellow_pacman_initial_positions = [] # Yellow pacman initial position
    green_pacman_initial_positions = [] # Green pacman intial position
    # Adding the values into the list for yellow pacman and green pacman
    for y_p in range(k+1, m+1):
        yellow_pacman_initial_positions.append((y_p, 1))
        green_pacman_goal_positions.append((y_p, 1))

    for g_p in range(1, k+1):
        green_pacman_initial_positions.append((g_p, n))
        yellow_pacman_goal_positions.append((g_p, n))
    yellow_pacman_initial_positions = tuple(yellow_pacman_initial_positions)
    green_pacman_initial_positions = tuple(green_pacman_initial_positions)
    yellow_pacman_goal_positions = tuple(yellow_pacman_goal_positions)
    green_pacman_goal_positions = tuple(green_pacman_goal_positions)
    print(f'Initial yellow pacman positions {yellow_pacman_initial_positions}')
    print(f'Goal yellow pacman positions {yellow_pacman_goal_positions}')
    print(f'Initial green pacman positions {green_pacman_initial_positions}')
    print(f'Goal green pacman positions {green_pacman_goal_positions}')
    # print(matrix)
    pacman = Pacman((yellow_pacman_initial_positions, green_pacman_initial_positions),
                    (yellow_pacman_goal_positions, green_pacman_goal_positions))
    result = breadth_first_graph_search(pacman)
    print(result.solution())




