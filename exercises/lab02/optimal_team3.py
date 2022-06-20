from constraint import *


def checkSum(t_s, t_l, t_m1, t_m2, t_m3, t_m4, t_m5):
    team_lider_weight = t_l[1]
    team_member1 = t_m1[1]
    team_member2 = t_m2[1]
    team_member3 = t_m3[1]
    team_member4 = t_m4[1]
    team_member5 = t_m5[1]
    total_score = team_lider_weight + team_member1 + team_member2 + team_member3 + team_member4 + team_member5
    if 0 < total_score <= 100.0:
        t_s = total_score
        return True
        # togas ovaa kombinacija e validna moze da se racuna kako rezultat
    else:
        return None
        # togas ovaa kombinacija na vrednosti ne gi zadovoluva uslovite


if __name__ == '__main__':
    problem = Problem()

    total_score = 0.0
    number_members = int(input())

    i = 0
    team_members = []
    while i < number_members:
        line = input().split(" ")
        number = float(line[0])
        name = str(line[1])
        team_member = [name, number]
        team_members.append(team_member)
        i += 1

    number_leaders = int(input())
    j = 0
    leader_members = []
    while j < number_leaders:
        line = input().split(" ")
        number = float(line[0])
        name = str(line[1])
        lider_member = [name, number]
        leader_members.append(lider_member)
        j += 1
    team_members.reverse()
    leader_members.reverse()
    weights = range(0, 101)
    problem.addVariable('0', weights)
    problem.addVariable('1', leader_members)
    problem.addVariable('2', team_members)
    problem.addVariable('3', team_members)
    problem.addVariable('4', team_members)
    problem.addVariable('5', team_members)
    problem.addVariable('6', team_members)
    problem.addConstraint(AllDifferentConstraint(), ['1'])
    for i in range(2, 7):
        for j in range(2, 7):
            if i < j:
                problem.addConstraint(lambda a, b: a != b, (f'{i}', f'{j}'))
    problem.addConstraint(checkSum, ['0', '1', '2', '3', '4', '5', '6'])
    solutions = problem.getSolutions()
    solution = dict()
    # print(len(solutions))
    # solution = problem.getSolution()
    for i in range(0, len(solutions)):
        for key, value in solutions[i].items():
            if key == '0':
                if value == 100.0:
                    solution = solutions[i]
    print(f'Total score: {solution["0"]}')
    print(f'Team leader: {solution["1"][0]}')
    print(f'Participant 1: {solution["2"][0]}')
    print(f'Participant 2: {solution["3"][0]}')
    print(f'Participant 3: {solution["4"][0]}')
    print(f'Participant 4: {solution["5"][0]}')
    print(f'Participant 5: {solution["6"][0]}')


