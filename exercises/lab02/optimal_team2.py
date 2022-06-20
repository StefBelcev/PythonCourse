from constraint import *

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

    problem.addVariable('1', t_l_names)
    problem.addVariable('2', t_m_names)
    problem.addVariable('3', t_m_names)
    problem.addVariable('4', t_m_names)
    problem.addVariable('5', t_m_names)
    problem.addVariable('6', t_m_names)
    problem.addConstraint(AllDifferentConstraint(), '1')

    for i in range(2, 7):
        for j in range(2, 7):
            if i < j:
                problem.addConstraint(lambda a, b: a != b, (f'{i}', f'{j}'))
    solutions = problem.getSolutions()
    solution = dict()
    optimal_team = []
    solution_team_names = []
    for i in range(0, len(solutions)):
        for key, value in solutions[i].items():
            if key == '1':
                leader = t_l_names.index(value)
                total_score += t_l_weights[leader]
                solution_team_names.append(t_l_names[leader])
            else:
                team_member = t_m_names.index(value)
                total_score += t_m_weights[team_member]
                solution_team_names.append(t_m_names[team_member])

        if total_score == 100.0:
            optimal_team = solution_team_names
            solution = solutions[i]
            print(f'Total score: {total_score}')
            print(f'Team leader: {optimal_team[5]}')
            print(f'Participant 1: {optimal_team[4]}')
            print(f'Participant 2: {optimal_team[3]}')
            print(f'Participant 3: {optimal_team[2]}')
            print(f'Participant 4: {optimal_team[1]}')
            print(f'Participant 5: {optimal_team[0]}')
            break
        else:
            optimal_team = []
            solution_team_names = []
            total_score = 0.0