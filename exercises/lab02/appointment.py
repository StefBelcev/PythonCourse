from constraint import *


# od toa sto go znaeme kako informacija gi proveruvame ogranuchuvanjata
def checkvalid(s_p, m_p, p_p, v_s):
    if s_p == 1:
        if m_p == 1 and p_p == 0 and v_s == 14:
            return True
        if m_p == 0 and p_p == 1 and v_s == 19 or m_p == 0 and p_p == 1 and v_s == 16 or m_p == 0 and p_p == 1 and v_s == 13:
            return True
    else:
        return None


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    vreme_sostanoci = [12, 13, 14, 15, 16, 17, 18, 19]
    # ---Dadeni se promenlivite, dodadete gi domenite-----
    licnost_prisustvo = [0, 1]
    problem.addVariable("Simona_prisustvo", licnost_prisustvo)
    problem.addVariable("Marija_prisustvo", licnost_prisustvo)
    problem.addVariable("Petar_prisustvo", licnost_prisustvo)
    problem.addVariable("vreme_sostanok", vreme_sostanoci)
    problem.addConstraint(checkvalid, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])

    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
