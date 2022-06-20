if __name__ == "__main__":
    number = int(input())
    single_line_minesweeper = []
    for n in range(0, number):
        single_line = input()
        single_line_minesweeper.append(list(map(str, single_line.split("   "))))
    for single_line in single_line_minesweeper:
        print(f'{single_line}')

