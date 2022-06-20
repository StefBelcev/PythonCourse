from constraint import *


def check_BI(cas, vezhbi):
    if cas == 'Mon_10' and vezhbi == 'Tue_10' or cas == 'Mon_10' and vezhbi == 'Thu_10':
        return True
    elif cas == 'Mon_11' and vezhbi == 'Tue_11' or cas == 'Mon_11' and vezhbi == 'Thu_11':
        return True
    elif cas == 'Wed_10' and vezhbi == 'Tue_10' or cas == 'Wed_10' and vezhbi == 'Thu_10':
        return True
    elif cas == 'Wed_11' and vezhbi == 'Tue_11' or cas == 'Wed_11' and vezhbi == 'Thu_11':
        return True
    elif cas == 'Fri_10' and vezhbi == 'Tue_10' or cas == 'Fri_10' and vezhbi == 'Thu_10':
        return True
    elif cas == 'Fri_11' and vezhbi == 'Tue_11' or cas == 'Fri_11' and vezhbi == 'Thu_11':
        return True
    else:
        return None


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    # gi dodavame casovite na Vestacka Inteligencija kako promenlivi ako imame max 3 i vezhbite
    if casovi_AI == 3:
        problem.addVariables(['AI_cas_1', 'AI_cas_2', 'AI_cas_3'], AI_predavanja_domain)
    elif casovi_AI == 2:
        problem.addVariables(['AI_cas_1', 'AI_cas_2'], AI_predavanja_domain)
    else:
        problem.addVariable('AI_cas_1', AI_vezbi_domain)
    problem.addVariable('AI_vezbi', AI_vezbi_domain)

    # gi dodavame casovite na Mashinsko Ucenje kako promenlivi ako imame max 3 i vezhbite
    if casovi_ML == 3:
        problem.addVariables(['ML_cas_1', 'ML_cas_2', 'ML_cas_3'], ML_predavanja_domain)
    elif casovi_ML == 2:
        problem.addVariables(['ML_cas_1', 'ML_cas_2'], ML_predavanja_domain)
    else:
        problem.addVariable('ML_cas_1', ML_predavanja_domain)
    problem.addVariable('ML_vezbi', ML_vezbi_domain)

    # gi dodavame casovite na Robotika kako promenlivi ako imame max 3 no neame vezhbi
    if casovi_R == 3:
        problem.addVariables(['R_cas_1', 'R_cas_2', 'R_cas_3'], R_predavanja_domain)
    elif casovi_R == 2:
        problem.addVariables(['R_cas_1', 'R_cas_2'], R_predavanja_domain)
    else:
        problem.addVariable('R_cas_1', R_predavanja_domain)

    # gi dodavame casovite na Bioinformatika kako promenlivi ako imame max 3 i vezhbite
    if casovi_BI == 3:
        problem.addVariables(['BI_cas_1', 'BI_cas_2', 'BI_cas_3'], BI_predavanja_domain)
    elif casovi_BI == 2:
        problem.addVariables(['BI_cas_1', 'BI_cas_2'], BI_predavanja_domain)
    else:
        problem.addVariable('BI_cas_1', BI_predavanja_domain)
    problem.addVariable('BI_vezbi', BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ogranichuvanje za site promenlivi da imaat razlicna vrednost - odnosno da nemame preklopuvanje
    problem.addConstraint(AllDifferentConstraint())
    if casovi_BI == 3:
        problem.addConstraint(check_BI, ['BI_cas_1', 'BI_cas_2', 'BI_cas_3', 'BI_vezbi'])
    elif casovi_BI == 2:
        problem.addConstraint(check_BI, ['BI_cas_1', 'BI_cas_2', 'BI_vezbi'])
    elif casovi_BI == 1:
        problem.addConstraint(check_BI, ['BI_cas_1', 'BI_vezbi'])
    # ----------------------------------------------------
    # solutions = problem.getSolutions()
    solution = problem.getSolution()
    resenie = {'BI_vezbi': '', 'BI_cas_1': '', 'AI_cas_1': '', 'AI_vezbi': '', 'ML_vezbi': '', 'ML_cas_1': '',
               'R_cas_1': ''}

    for key, value in solution.items():
        if key == 'BI_vezbi':
            resenie['BI_vezbi'] = value
        if key == 'BI_cas_1':
            resenie['BI_cas_1'] = value
        if key == 'AI_cas_1':
            resenie['AI_cas_1'] = value
        if key == 'AI_vezbi':
            resenie['AI_vezbi'] = value
        if key == 'ML_vezbi':
            resenie['ML_vezbi'] = value
        if key == 'ML_cas_1':
            resenie['ML_cas_1'] = value
        if key == 'R_cas_1':
            resenie['R_cas_1'] = value
    print(resenie)
