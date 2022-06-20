from Aud03.informed.informed_search import astar_search
from Aud02.uninformed.utils import Problem


def svrtiseDesno(ghost_orientation):
    if ghost_orientation == "Gore":
        return "Desno"
    elif ghost_orientation == "Dole":
        return "Levo"
    elif ghost_orientation == "Desno":
        return "Dole"
    elif ghost_orientation == "Levo":
        return "Gore"


def svrtiseLevo(ghost_orientation):
    if ghost_orientation == "Gore":
        return "Levo"
    elif ghost_orientation == "Dole":
        return "Desno"
    elif ghost_orientation == "Desno":
        return "Gore"
    elif ghost_orientation == "Levo":
        return "Dole"


def pridviziseNapred(ghost_orientation):
    if ghost_orientation == "Gore":
        return "Gore"
    elif ghost_orientation == "Dole":
        return "Dole"
    elif ghost_orientation == "Desno":
        return "Desno"
    elif ghost_orientation == "Levo":
        return "Levo"


def stop(ghost_orientation):
    if ghost_orientation == "Gore":
        return "Gore"
    elif ghost_orientation == "Dole":
        return "Dole"
    elif ghost_orientation == "Desno":
        return "Desno"
    elif ghost_orientation == "Levo":
        return "Levo"


class DarkSide(Problem):
    def __init__(self, obstacle_list, initial, goal):
        super().__init__(initial, goal)
        self.grid_size = [5, 7]
        self.obstacle_list = obstacle_list

    def successor(self, state):
        successors = dict()
        maximum_x = self.grid_size[0]
        maximum_y = self.grid_size[1]
        ghost_a, ghost_b = list(state[0][1]), list(state[0][2])
        ghost_a_x = ghost_a[0]
        ghost_a_y = ghost_a[1]
        ghost_a_ori = ghost_a[2]
        ghost_b_x = ghost_b[0]
        ghost_b_y = ghost_b[1]
        ghost_b_ori = ghost_b[2]

        # Промена на состојбата во придвижи се напред
        new_ghost_a_ori = pridviziseNapred(ghost_a_ori)
        if new_ghost_a_ori == "Desno":
            if ghost_a_x + 1 < maximum_x - 1 and [ghost_a_x + 1, ghost_a_y]  not in self.obstacle_list and [ghost_a_x + 1, ghost_a_y] != ghost_b:
                new_ghost_a_x = ghost_a_x + 1
                successors["PridviziseNapred"] = ((new_ghost_a_x,  ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Levo":
            if ghost_a_x - 1 > 0 and [ghost_a_x - 1, ghost_a_y]  not in self.obstacle_list and [ghost_a_x - 1, ghost_a_y] != ghost_b:
                new_ghost_a_x = ghost_a_x - 1
                successors["PridviziseNapred"] = ((new_ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Dole":
            if ghost_a_y - 1 > 0 and [ghost_a_x, ghost_a_y - 1]  not in self.obstacle_list and [ghost_a_x , ghost_a_y - 1] != ghost_b:
                new_ghost_a_y = ghost_a_y - 1
                successors["PridviziseNapred"] = ((ghost_a_x, new_ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Gore":
            if ghost_a_y + 1 < maximum_y - 1 and [ghost_a_x, ghost_a_y + 1] not in self.obstacle_list and [ghost_a_x, ghost_a_y + 1] != ghost_b:
                new_ghost_a_y = ghost_a_y + 1
                successors["PridviziseNapred"] = ((ghost_a_x, new_ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        else:
            new_ghost_a_ori = stop(new_ghost_a_ori)
            successors["Stop"] = (
                (ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))

        new_ghost_a_ori = svrtiseLevo(ghost_a_ori)
        if new_ghost_a_ori == "Desno":
            if ghost_a_x + 1 < maximum_x - 1 and [ghost_a_x + 1, ghost_a_y] not in self.obstacle_list and [ghost_a_x + 1, ghost_a_y] != ghost_b:
                new_ghost_a_x = ghost_a_x + 1
                successors["SvrtiseLevo"] = (
                (new_ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Levo":
            if ghost_a_x - 1 > 0 and [ghost_a_x - 1, ghost_a_y] not in self.obstacle_list and [ghost_a_x - 1, ghost_a_y] != ghost_b:
                new_ghost_a_x = ghost_a_x - 1
                successors["SvrtiseLevo"] = (
                (new_ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Dole":
            if ghost_a_y - 1 > 0 and [ghost_a_x, ghost_a_y - 1] not in self.obstacle_list and [ghost_a_x , ghost_a_y - 1] != ghost_b:
                new_ghost_a_y = ghost_a_y - 1
                successors["SvrtiseLevo"] = (
                (ghost_a_x, new_ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Gore":
            if ghost_a_y + 1 < maximum_y - 1 and [ghost_a_x, ghost_a_y + 1] not in self.obstacle_list and [ghost_a_x, ghost_a_y + 1] != ghost_b:
                new_ghost_a_y = ghost_a_y + 1
                successors["SvrtiseLevo"] = (
                (ghost_a_x, new_ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        else:
            new_ghost_a_ori = stop(new_ghost_a_ori)
            successors["Stop"] = (
                (ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))

        new_ghost_a_ori = svrtiseDesno(ghost_a_ori)
        if new_ghost_a_ori == "Desno":
            if ghost_a_x + 1 < maximum_x - 1 and [ghost_a_x + 1, ghost_a_y] not in self.obstacle_list and [ghost_a_x + 1, ghost_a_y] != ghost_b:
                new_ghost_a_x = ghost_a_x + 1
                successors["SvrtiseDesno"] = (
                    (new_ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Levo":
            if ghost_a_x - 1 > 0 and [ghost_a_x - 1, ghost_a_y] not in self.obstacle_list and [ghost_a_x - 1, ghost_a_y] != ghost_b:
                new_ghost_a_x = ghost_a_x - 1
                successors["SvrtiseDesno"] = (
                    (new_ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Dole":
            if ghost_a_y - 1 > 0 and [ghost_a_x, ghost_a_y - 1] not in self.obstacle_list and [ghost_a_x , ghost_a_y - 1] != ghost_b:
                new_ghost_a_y = ghost_a_y - 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, new_ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        elif new_ghost_a_ori == "Gore":
            if ghost_a_y + 1 < maximum_y - 1 and [ghost_a_x, ghost_a_y + 1] not in self.obstacle_list and [ghost_a_x, ghost_a_y + 1] != ghost_b:
                new_ghost_a_y = ghost_a_y + 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, new_ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))
        else:
            new_ghost_a_ori = stop(new_ghost_a_ori)
            successors["Stop"] = (
                (ghost_a_x, ghost_a_y, new_ghost_a_ori), (ghost_b_x, ghost_b_y, ghost_b_ori))

        #Дух б
        new_ghost_b_ori = pridviziseNapred(ghost_a_x)
        if new_ghost_b_ori == "Desno":
            if ghost_b_x + 1 < maximum_x - 1 and [ghost_b_x + 1, ghost_b_y] not in self.obstacle_list and [ghost_b_x + 1, ghost_b_y] != ghost_a:
                new_ghost_b_x = ghost_b_x + 1
                successors["PridviziseNapred"] = (
                (ghost_a_x, ghost_a_y, ghost_a_ori), (new_ghost_b_x, ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Levo":
            if ghost_b_x - 1 > 0 and [ghost_b_x - 1, ghost_b_y] not in self.obstacle_list and [ghost_b_x - 1, ghost_b_y] != ghost_a:
                new_ghost_b_x = ghost_b_x - 1
                successors["PridviziseNapred"] = (
                (ghost_a_x, ghost_a_y, ghost_a_ori), (new_ghost_b_x, ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Dole":
            if ghost_b_y - 1 > 0 and [ghost_b_x, ghost_b_y - 1] not in self.obstacle_list and [ghost_b_x , ghost_b_y - 1] != ghost_a:
                new_ghost_b_y = ghost_b_y - 1
                successors["PridviziseNapred"] = (
                (ghost_a_x, ghost_b_y, ghost_a_ori), (ghost_b_x, new_ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Gore":
            if ghost_b_y + 1 < maximum_y - 1 and [ghost_b_x, ghost_b_y + 1] not in self.obstacle_list and [ghost_b_x, ghost_b_y + 1] != ghost_a:
                new_ghost_b_y = ghost_b_y + 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, new_ghost_b_y, new_ghost_b_ori))
        else:
            new_ghost_b_ori = stop(new_ghost_b_ori)
            successors["Stop"] = (
                (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, ghost_b_y, new_ghost_b_ori))

        new_ghost_b_ori = svrtiseLevo(ghost_b_ori)
        if new_ghost_b_ori == "Desno":
            if ghost_b_x + 1 < maximum_x - 1 and [ghost_b_x + 1, ghost_b_y] not in self.obstacle_list and [ghost_b_x + 1, ghost_b_y] != ghost_a:
                new_ghost_b_x = ghost_b_x + 1
                successors["SvrtiseLevo"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (new_ghost_b_x, ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Levo":
            if ghost_b_x - 1 > 0 and [ghost_b_x - 1, ghost_b_y] not in self.obstacle_list and [ghost_b_x - 1, ghost_b_y] != ghost_a:
                new_ghost_b_x = ghost_b_x - 1
                successors["SvrtiseLevo"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (new_ghost_b_x, ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Dole":
            if ghost_b_y - 1 > 0 and [ghost_b_x, ghost_b_y - 1] not in self.obstacle_list [ghost_b_x , ghost_b_y - 1] != ghost_a:
                new_ghost_b_y = ghost_b_y - 1
                successors["SvrtiseLevo"] = (
                    (ghost_a_x, ghost_b_y, ghost_a_ori), (ghost_b_x, new_ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Gore":
            if ghost_b_y + 1 < maximum_y - 1 and [ghost_b_x, ghost_b_y + 1] not in self.obstacle_list and [ghost_b_x, ghost_b_y + 1] != ghost_a:
                new_ghost_b_y = ghost_b_y + 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, new_ghost_b_y, new_ghost_b_ori))
        else:
            new_ghost_b_ori = stop(new_ghost_b_ori)
            successors["Stop"] = (
                (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, ghost_b_y, new_ghost_b_ori))

        new_ghost_b_ori = svrtiseDesno(ghost_b_ori)
        if new_ghost_b_ori == "Desno":
            if ghost_b_x + 1 < maximum_x - 1 and [ghost_b_x + 1, ghost_b_y] not in self.obstacle_list and [ghost_b_x + 1, ghost_b_y] != ghost_a:
                new_ghost_b_x = ghost_b_x + 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (new_ghost_b_x, ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Levo":
            if ghost_b_x - 1 > 0 and [ghost_b_x - 1, ghost_b_y] not in self.obstacle_list and [ghost_b_x - 1, ghost_b_y] != ghost_a:
                new_ghost_b_x = ghost_b_x - 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (new_ghost_b_x, ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Dole":
            if ghost_b_y - 1 > 0 and [ghost_b_x, ghost_b_y - 1] not in self.obstacle_list [ghost_b_x , ghost_b_y - 1] != ghost_a:
                new_ghost_b_y = ghost_b_y - 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, new_ghost_b_y, new_ghost_b_ori))
        elif new_ghost_b_ori == "Gore":
            if ghost_b_y + 1 < maximum_y - 1 and [ghost_b_x, ghost_b_y + 1] not in self.obstacle_list and [ghost_b_x, ghost_b_y + 1] != ghost_a:
                new_ghost_b_y = ghost_b_y + 1
                successors["SvrtiseDesno"] = (
                    (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, new_ghost_b_y, new_ghost_b_ori))
        else:
            new_ghost_b_ori = stop(new_ghost_b_ori)
            successors["Stop"] = (
                (ghost_a_x, ghost_a_y, ghost_a_ori), (ghost_b_x, ghost_b_y, new_ghost_b_ori))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    @staticmethod
    def euclidean(self, point1, point2):
        return abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2

    @staticmethod
    def manhattan(self, ghost, pacman_pos):
        return abs(ghost[0] - pacman_pos[0]) - abs(ghost[1] - pacman_pos[1])

    def h_max(self, node):
        ghost_a = node.state[0]
        ghost_b = node.state[1]
        goal = list(self.goal)
        pass
        # dist_gA = DarkSide.manhattan(ghost_a, goal)
        # dist_gB = DarkSide.euclidean(ghost_b, goal)
        # max_dist = max(dist_gA, dist_gB)
        # return max_dist

    def h(self, node):
        ghost_a = list(node.state[0])
        ghost_b = list(node.state[1])
        goal = list(self.goal)
        dist_ga = DarkSide.euclidean(ghost_a, goal)
        dist_gb = DarkSide.euclidean(ghost_b, goal)
        min_dist = min(dist_ga, dist_gb)
        return min_dist

    def goal_test(self, state):
        goal = self.goal
        return goal[0] == state[0][0] and goal[1] == state[0][1] or goal[0] == state[1][0] and goal[1] == state[1][1]


if __name__ == "__main__":
    x_a = int(input())
    y_a = int(input())
    orientation_a = str(input())
    x_b = int(input())
    y_b = int(input())
    orientation_b = str(input())
    x_p = int(input())
    y_p = int(input())
    # ghost_a = (x_a, y_a, orientation_a)
    # ghost_b = (x_b, y_b, orientation_b)
    # pacman = (x_p, y_p)
    ghost_a = (0, 4, 'Desno')
    ghost_b = (6, 4, 'Levo')
    pacman = (4, 2)
    obstacles = [[0, 3], [1, 3], [2, 2], [2, 3], [2, 4]]
    ghosts = DarkSide(obstacles, (ghost_a, ghost_b), pacman)
    result = astar_search(ghosts)
    print(result.solution())
