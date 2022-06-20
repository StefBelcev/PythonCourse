from constraint import *


def checkSum(t_l, t_m1, t_m2, t_m3, t_m4, t_m5):
    team_lider_weight = t_l
    team_member1 = t_m1
    team_member2 = t_m2
    team_member3 = t_m3
    team_member4 = t_m4
    team_member5 = t_m5
    total_score = team_lider_weight + team_member1 + team_member2 + team_member3 + team_member4 + team_member5
    if 0 < total_score <= 100.0:
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
    t_m_names = []
    t_m_weights = []

    while i < number_members:
        line = input().split(" ")
        number = float(line[0])
        t_m_weights.append(number)
        name = str(line[1])
        t_m_names.append(name)
        i += 1

    number_leaders = int(input())

    j = 0
    t_l_names = []
    t_l_weights = []

    while j < number_leaders:
        line = input().split(" ")
        number = float(line[0])
        t_l_weights.append(number)
        name = str(line[1])
        t_l_names.append(name)
        j += 1

    t_m_names.reverse()
    t_m_weights.reverse()

    t_l_names.reverse()
    t_l_weights.reverse()

    problem.addVariable('1', t_l_weights)
    problem.addVariable('2', t_m_weights)
    problem.addVariable('3', t_m_weights)
    problem.addVariable('4', t_m_weights)
    problem.addVariable('5', t_m_weights)
    problem.addVariable('6', t_m_weights)
    problem.addConstraint(AllDifferentConstraint(), ['1'])

    for i in range(2, 7):
        for j in range(2, 7):
            if i < j:
                problem.addConstraint(lambda a, b: a != b, (f'{i}', f'{j}'))
    problem.addConstraint(checkSum, ['1', '2', '3', '4', '5', '6'])

    solutions = problem.getSolutions()

    optimal_team = dict()
    max_score = 0
    total_score = 0
    number_of_optimal_team = 0

    for index in range(0, len(solutions)):
        for k in solutions[index].keys():
            total_score += solutions[index][k]
        if total_score == 100.0:
            max_score = total_score
            number_of_optimal_team = index
        else:
            total_score = 0

    optimal_team = solutions[number_of_optimal_team]

    t_l_index = t_l_weights.index(optimal_team["1"])
    t_m1_index = t_m_weights.index(optimal_team["2"])
    t_m2_index = t_m_weights.index(optimal_team["3"])
    t_m3_index = t_m_weights.index(optimal_team["4"])
    t_m4_index = t_m_weights.index(optimal_team["5"])
    t_m5_index = t_m_weights.index(optimal_team["6"])

    print(f'Total score: {max_score}')
    print(f'Team leader: {t_l_names[t_l_index]}')
    print(f'Participant 1: {t_m_names[t_m1_index]}')
    print(f'Participant 2: {t_m_names[t_m2_index]}')
    print(f'Participant 3: {t_m_names[t_m3_index]}')
    print(f'Participant 4: {t_m_names[t_m4_index]}')
    print(f'Participant 5: {t_m_names[t_m5_index]}')