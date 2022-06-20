from Aud02.uninformed.utils import Problem
from Aud03.informed.informed_search import astar_search


def update_obstacle_position(obstacle_pos):
    x, y, direction = obstacle_pos
    if (y == 0 and direction == -1) or (y == 5 and direction == 1):
        direction *= (-1)
    y_new = y + direction
    position_new = x, y_new, direction
    return position_new


def check_collision(man, ob1, ob2):
    return man != ob1[:2] and man != ob2[:2]
    # return man[0] != ob1[0] and man[1] != ob1[1] and man[0] != ob2[0] and man[1] != ob2[1]


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        x = state[0]
        y = state[1]
        obstacle_1 = state[2:5]
        obstacle_2 = state[5:-1]
        ob1 = (state[2], state[3], state[4])
        ob2 = (state[5], state[6], state[7])
        ob_new1 = update_obstacle_position(ob1)
        ob_new2 = update_obstacle_position(ob2)
        if x < 7:
            x_new = x + 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, ob_new1, ob_new2):
                successors["Right"] = (
                    x_new, y_new, ob_new1[0], ob_new1[1], ob_new1[2], ob_new2[0], ob_new2[1], ob_new2[2])
        if x > 0:
            x_new = x - 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, ob_new1, ob_new2):
                successors["Left"] = (
                    x_new, y_new, ob_new1[0], ob_new1[1], ob_new1[2], ob_new2[0], ob_new2[1], ob_new2[2])
        if y < 5:
            x_new = x
            y_new = y + 1
            man = x_new, y_new
            if check_collision(man, ob_new1, ob_new2):
                successors["Up"] = (
                    x_new, y_new, ob_new1[0], ob_new1[1], ob_new1[2], ob_new2[0], ob_new2[1], ob_new2[2])
        if y > 0:
            x_new = x
            y_new = y - 1
            man = x_new, y_new
            if check_collision(man, ob_new1, ob_new2):
                successors["Down"] = (
                    x_new, y_new, ob_new1[0], ob_new1[1], ob_new1[2], ob_new2[0], ob_new2[1], ob_new2[2])
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        # possible = self.successor(state)
        # return possible[action]
        return self.successor(state)[action]

    def goal_test(self, state):
        man = [state[0], state[1]]
        goal = [self.goal[0], self.goal[1]]
        return man == goal
        # g = self.goal
        # return state[0] == g[0] and state[1] == g[1]

    def h(self, node):
        return abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])


if __name__ == "__main__":
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())
    house = [house_x, house_y]
    # testing = [man_x, man_y, 2, 5, -1, 5, 0, 1]
    # obstacle_1 = testing[2: 4]
    # obstacle_2 = testing[5: -1]
    informed_explorer = Explorer((man_x, man_y, 2, 5, -1, 5, 0, 1), house)
    result = astar_search(informed_explorer)
    print(result.solution())
    # print(obstacle_2)
    # print(obstacle_1)
