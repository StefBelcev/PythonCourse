if __name__ == "__main__":
    f = open()
    for line in f.readlines():
        #readLines() -> lista od redovite u fajlot
        print(len(line))
    for line in f:
        print(len(line))