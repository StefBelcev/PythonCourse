# Gradebook Problem 1 (3 / 25)
# Дефинирајте речник students во кој ќе се чуваат информации за предметите кои ги полагале студентите.
# Од стандарден влез се читаат информации за име, презиме, број на индекс, предмет, поени од теоретски дел,
# поени од практичен дел и поени од лабораториски вежби. Може да се вчитаат информации за неограничен број
# студенти. Вчитувањето информации завршува кога ќе се прочита клучниот збор end.
# Пополнете го речникот students со вчитаните информации.
#
# Потоа, за секој од студентите да се испечати името и презимето,
# и оцената за секој од предметите кои ги има полагано.
#
# Оцената се пресметува на следниот начин:
#
# [0, 50] - 5
#
# (50, 60] - 6
#
# (60, 70] - 7
#
# (70, 80] - 8
#
# (80, 90] - 9
#
# (90, 100] - 10

def display_information(list_lists):
    students_dic = {'Student': []}
    for list_el in list_lists:
        students_dic['Student'].append(list_el)
    return students_dic


def grades(grade):
    if grade in range(0, 51):
        return 5
    elif grade in range(51, 61):
        return 6
    elif grade in range(61, 71):
        return 7
    elif grade in range(71, 81):
        return 8
    elif grade in range(81, 91):
        return 9
    elif grade in range(91, 100):
        return 10


def reverse_list(data_list):
    new_list = data_list[::-1]
    # length = len(data_list)
    # s = length
    # new_list = [None] * length
    # for item in data_list:
    #     s = s - 1
    #     new_list[s] = item
    return new_list


if __name__ == "__main__":
    single_line = []
    while True:
        line = input()
        if line != "end":
            single_line.append(list(map(str, line.split(','))))
        else:
            break
    print(f'{single_line}')

    dic = display_information(single_line)
    students = dic['Student']
    for student in students:
        sum_points = int(student[-1]) + int(student[-2]) + int(student[-3])
        grade = grades(sum_points)
        point1 = student.pop(-1)
        point2 = student.pop(-1)
        point_labs = student.pop(-1)
        student.append(grade)

    print(f'{students}')
    students_copy = students
    rev_students = students[:]
    for student in students_copy:
        print(f'Student: {student[0]} {student[1]}')
        print(f'\t{student[3]}: {student[4]}')
        for rev_student in rev_students:
            if (student[0] == rev_student[0]) and (student[1] == rev_student[1]) and (
                    student[2] == rev_student[2]) and (student[3] != rev_student[3]):
                print(f'\t{rev_student[3]}: {rev_student[4]}')
                students.remove(rev_student)
        print(f'')
