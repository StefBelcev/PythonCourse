from Aud02.uninformed.uninformed_search import *
from Aud02.uninformed.utils import Problem


# D1: Disk i - за преместување на дискот i надесно во соседно празно поле, i = 1, 2, ..., N
# D2: Disk i - за преместување на дискот i преку едно поле надесно, i = 1, 2, ..., N
# L1: Disk i - за преместување на дискот i налево во соседно празно поле, i = 1, 2, ..., N
# L2: Disk i - за преместување на дискот i преку едно поле налево, i = 1, 2, ..., N
# value -1 ednas levo, -2 dva pati levo, +1 ednas nadesno, +2 dva pati nadesno

class Disk(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        start_disks = list(state[0])
        end_disks = state[1]
        ls = len(start_disks)
        for i in range(ls):
            if start_disks[i] != 0:
                # dali elementot ima vrednost, broj na disk e vrednosta i koja pozicija
                # e, e tekovnata pozicija vo listata
                # na pocetok na lista sme , moze da odime 2 nadesno i 1 nadesno
                if i == 0:

                    if start_disks[i + 1] == 0:  # + 1
                        temp_disks = start_disks[:]
                        temp_disks[i+1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i + 1] != 0:  # +2
                        temp_disks = start_disks[:]
                        temp_disks[i + 2] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D2: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                # vtor element na lista sme, moze da odime 1 nalevo,1 nadesno i 2 nadesno
                elif i == 1:

                    if start_disks[i + 1] == 0:  # +1
                        temp_disks = start_disks[:]
                        temp_disks[i + 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i + 1] != 0:  # +2
                        temp_disks = start_disks[:]
                        temp_disks[i + 2] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D2: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i - 1] == 0:  # -1
                        temp_disks = start_disks[:]
                        temp_disks[i - 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                elif i == n - 1:

                    if start_disks[i - 1] == 0:  # -1
                        temp_disks = start_disks[:]
                        temp_disks[i - 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i - 1] != 0:  # -2
                        temp_disks = start_disks[:]
                        temp_disks[i - 2] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L2: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                elif i == n - 2:
                    if start_disks[i + 1] == 0:  # +1
                        temp_disks = start_disks[:]
                        temp_disks[i + 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i - 1] == 0:  # -1
                        temp_disks = start_disks[:]
                        temp_disks[i - 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i - 1] != 0:  # -2
                        temp_disks = start_disks[:]
                        temp_disks[i - 2] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L2: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                else:
                    if start_disks[i + 1] == 0:  # +1
                        temp_disks = start_disks[:]
                        temp_disks[i + 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i + 1] != 0:  # +2
                        temp_disks = start_disks[:]
                        temp_disks[i + 2] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'D2: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i - 1] == 0:  # -1
                        temp_disks = start_disks[:]
                        temp_disks[i - 1] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L1: Disk {start_disks[i]}'] = (new_start_disks, end_disks)

                    elif start_disks[i - 1] != 0:  # -2
                        temp_disks = start_disks[:]
                        temp_disks[i - 2] = start_disks[i]
                        temp_disks[i] = 0
                        new_start_disks = tuple(temp_disks)
                        successors[f'L2: Disk {start_disks[i]}'] = (new_start_disks, end_disks)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        start_disks = state[0]
        end_disks = state[1]
        return start_disks == end_disks


if __name__ == "__main__":
    n = int(input())
    l = int(input())
    disks = []
    disks1 = []
    for c in range(l):
        # disks.append([f'Disk {i + 1}', 0])
        disks1.append(0)
    for j in range(n):
        # disks[j] = [f'Disk {j + 1}', j + 1]
        disks1[j] = j + 1
    print(disks1)
    end_disks1 = disks1[:]
    end_disks1.reverse()
    end_disks1 = tuple(end_disks1)
    start_disks1 = tuple(disks1)
    disk = Disk((start_disks1, end_disks1))
    result = breadth_first_graph_search(disk)
    print(result.solution())
