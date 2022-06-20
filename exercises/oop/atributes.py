if __name__ == "__main__":
    class Counter:
        overall_total = 0 #class attribute
        def __init__(self):
            self.my_total = 0 #data attribute
        def increment(self):
            Counter.overall_total = Counter.overall_total + 1
            self.my_total = self.my_total + 1
    a = Counter()
    b = Counter()
    a.increment()
    b.increment()
    print(a.my_total)
    print(a.__class__.overall_total)
    print(b.my_total)
    print(b.__class__.overall_total)