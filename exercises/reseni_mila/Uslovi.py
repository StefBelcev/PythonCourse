from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    problem.addVariable("Filip", [4])
    problem.addVariable("Naum", [1, 2])
    problem.addVariable("Petra", [2, 6])
    problem.addVariable("Marija", [3])

    problem.addConstraint(AllDifferentConstraint(), ['Filip', 'Naum', 'Petra', 'Marija'])

    resenie = {'Marija': 0, 'Filip': 0, 'Naum': 0, 'Petra': 0}
    resenija = problem.getSolutions()
    for resenie1 in resenija:
        for key, value in resenie1.items():
            if key == 'Marija':
                resenie['Marija'] = value
            if key == 'Filip':
                resenie['Filip'] = value
            if key == 'Naum':
                resenie['Naum'] = value
            if key == 'Petra':
                resenie['Petra'] = value
        print(resenie)