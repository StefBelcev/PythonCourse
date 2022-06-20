from constraint import *


def sostanok(simona, marija, petar, sostanoci):
    if simona == 1 and marija == 1 and petar == 0 and sostanoci == 14 \
            or simona == 1 and marija == 0 and petar == 1 and sostanoci == 19 \
            or simona == 1 and marija == 0 and petar == 1 and sostanoci == 16 \
            or simona == 1 and marija == 0 and petar == 1 and sostanoci == 13:
        return True
    else:
        return None


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    termini_za_sostanok = [12, 13, 14, 15, 16, 17, 18, 19]
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", termini_za_sostanok)
    problem.addConstraint(sostanok, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    resenie = {"Simona_prisustvo": 0, "Marija_prisustvo": 0, "Petar_prisustvo": 0, "vreme_sostanok": 0}
    resenija = problem.getSolutions()
    for res in resenija:
        for key, value in res.items():
            if key == "Simona_prisustvo":
                resenie["Simona_prisustvo"] = value
            if key == "Marija_prisustvo":
                resenie["Marija_prisustvo"] = value
            if key == "Petar_prisustvo":
                resenie["Petar_prisustvo"] = value
            if key == "vreme_sostanok":
                resenie["vreme_sostanok"] = value
        print(resenie)