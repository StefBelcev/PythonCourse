from constraint import *


def checkSum(t_s, t_l, t_m1, t_m2, t_m3, t_m4, t_m5):
    team_lider_weight = t_l[0]
    team_member1 = t_m1[0]
    team_member2 = t_m2[0]
    team_member3 = t_m3[0]
    team_member4 = t_m4[0]
    team_member5 = t_m5[0]
    total_sum = team_lider_weight + team_member1 + team_member2 + team_member3 + team_member4 + team_member5
    if total_sum == 100.0:
        t_s = total_sum


if __name__ == '__main__':
    problem = Problem()

    number_members = int(input())
    i = 0
    weights_members = []
    team_members = []
    while i < number_members:
        line = input().split(" ")
        number = float(line[0])
        weights_members.append(number)
        name = str(line[1])
        team_member = [number, name]
        team_members.append(team_member)
        i += 1

    number_leaders = int(input())
    j = 0
    weights_liders = []
    team_liders = []
    while j < number_leaders:
        line = input().split(" ")
        number = float(line[0])
        weights_liders.append(number)
        name = str(line[1])
        team_lider = [number, name]
        team_liders.append(team_lider)
        j += 1

    team_liders.reverse()
    team_members.reverse()
    team_weights = []
    team_weights.append(0)
    team_weights.append(weights_liders)
    team_weights.append(weights_members)
    team_weights.append(100)
    # team_weights = team_liders + team_members
    print(team_weights)

    problem.addVariable("Total score:", [0, 100.0])
    problem.addVariable("Team leader:", team_liders)
    problem.addVariable("Participant 1", team_members)
    problem.addVariable("Participant 2", team_members)
    problem.addVariable("Participant 3", team_members)
    problem.addVariable("Participant 4", team_members)
    problem.addVariable("Participant 5", team_members)
    problem.addConstraint(AllDifferentConstraint(), "Team leader")
    # total_score = 0.0
    for i in range(1, 6):
        for j in range(1, 6):
            if i < j:
                problem.addConstraint(lambda a, b: a != b, (f'Participant {i}', f'Participant {j}'))

    problem.addConstraint(checkSum, ["Total score:", "Team leader:", "Participant 1", "Participant 2", "Participant 3",
                                     "Participant 4", "Participant 5"])
    result = problem.getSolutions()
    print(len(result))
    # solution = dict()
    # for i in range(0, len(result)):
    #     for key in result[i].keys():
    #         total_score += result[i][key][0]
    #     if total_score == 100.0:
    #         solution = result[i]
    # print(f'Total score: {total_score}')
    # print(f'Team leader: {solution["Team leader"][1]}')
    # print(f'Participant 1: {solution["Participant 1"][1]}')
    # print(f'Participant 2: {solution["Participant 2"][1]}')
    # print(f'Participant 3: {solution["Participant 3"][1]}')
    # print(f'Participant 4: {solution["Participant 4"][1]}')
    # print(f'Participant 5: {solution["Participant 5"][1]}')

