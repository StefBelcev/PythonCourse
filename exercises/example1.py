if __name__ == "__main__":
    tu = (123, 'abc', (2, 3), 4.26)
    list = [123, 'abc', 4.26]
    tu1 = tu[:2]
    tu2 = tu[:]
    tu3 = tu[0:-1]
    tu4 = tu[1:]
    print(tu1, tu2, tu3, tu4)
    print(tu[0], list[1])
    print(tu[-1], list[1])
