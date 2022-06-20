if __name__ == "__main__":
    # Deklaracija na funkcii, funkcii se deklariraat so klucniot zbor def
    def call_func(x, func):
        print(func(x))

    # Funkciite mozhe da se pishuvaat i vo eden red
    def double(n): return n*2
    def triple(n): return n*3

    # Funkcija mozhe da bide dadena kako argument na druga funkcija
    call_func(3, double)
    call_func(4, triple)

    def hello(word):
        print(f'Hello ' + word)
    hello('World')
    hello('Universe')

    # Moze da deklarirame nova funkcija od vekje postoechka
    say_hi = hello
    say_hi('Mars')
    say_hi('Jupiter')
