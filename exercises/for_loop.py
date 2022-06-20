def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


if __name__ == "__main__":
    for (x, y) in [('a', 1), ('b', 2), ('c', 3), ('d', 4)]:
        print(x, y)
    for char in "Hello World":
        print(char)
    x = range(2,6)
    for n in x:
        print(n)
    for y in range(6):
        print(y)
    z = range(2, 7, 2)
    for double_z in z:
        print(double_z)
    fruits = ['banana', 'orange', 'kiwi', 'apple']
    for x in range(len(fruits)):
        print(x + 1, fruits[x])
    # print(len(fruits))
    for index in range(len(fruits)):
        print(fruits[index])
    ages = {'Sam': 4, 'Marry': 6, 'Billy': 1}
    for name in ages.keys():
        print(name, ages[name])

    for x in my_range(1, 10, 0.5):
        print(x)
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)
    for (x, y) in [('a', 1), ('b', 2), ('c', 3), ('d', 4)]:
        print(x)
    ages = {'Sam': 4, 'Mary': 3, 'Kaj si be': 5}
    for key in ages.keys():
        print(ages[key])
    for value in ages.values():
        print(value)
    for (key, value) in ages.items():
        print(key, value)
    list1 = [0, 1, 2]
    for i in range(3):
        if list1[i] == 1:
            print(f'We found the index ->{i}')
            list1[i] = 0
    print(list1)