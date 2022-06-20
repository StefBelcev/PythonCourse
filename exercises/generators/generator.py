if __name__ == "__main__":
    def gy():
        x,y = 2,3
        yield x, y, x + y
        z = 12
        yield z/x
        yield z/y
        return
    g = gy()
    print(next(g))
    print(next(g))
    print(next(g))

    #site zborovi vo datoteka get_word
    def get_word(file):
        for line in file:
            for word in line.split():
                yield word
        return
    