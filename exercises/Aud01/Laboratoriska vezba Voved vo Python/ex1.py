# Alice,Doe,141414,Artificial Intelligence,40,40,5
# Alice,Doe,141414,Machine Learning,30,40,10
# Lewis,Smith,141415,Robotics,40,30,10
# Lewis,Smith,141415,Bioinformatics,40,30,10
# George,Williams,123456,Artificial Intelligence,20,40,9
# James,Brown,123457,Artificial Intelligence,25,30,3
# William,Williams,123458,Artificial Intelligence,10,45,8
# Elle,Brown,123459,Artificial Intelligence,45,10,7
# end
def subject_grade(points):
    if points in range(0, 51):
        return 5
    elif points in range(51, 61):
        return 6
    elif points in range(61, 71):
        return 7
    elif points in range(71, 81):
        return 8
    elif points in range(81, 91):
        return 9
    elif points in range(91, 101):
        return 10

if __name__ == "__main__":
    list_of_students = []
    while True:
        line = input()
        if line != "end":
            list_of_students.append(list(map(str, line.split(','))))
        else:
            break
    dict_students = {'Student': []}
    for single_student in list_of_students:
        dict_students['Student'].append(single_student)
    final_points = 0
    students = dict_students['Student']
    for student in students:
        lab_points = student[-1]
        student.pop(-1)
        points2 = student[-1]
        student.pop(-1)
        points1 = student[-1]
        student.pop(-1)
        final_points = int(lab_points) + int(points1) + int(points2)
        grade = subject_grade(final_points)
        student.append(grade)
    print(students)
    copy_students = students[:]
    for student in students:
        print(f'Student: {student[0]} {student[1]}')
        print(f'\t{student[3]}: {student[-1]}')
        for copy_student in copy_students:
            if((student[0] == copy_student[0] and student[1] == copy_student[1]\
                    and student[2] == copy_student[2] and student[3] != copy_student[3])):
                print(f'\t{copy_student[3]} : {copy_student[-1]}')
                students.remove(copy_student)
        print(f'')
