if __name__ == "__main__":

    class Parent:  # Definicija na klasata - roditel
        parent_attr = 100  # Klasen atribut
        def __init__(self):
            print("Calling parent constructor")
        def parent_method(self):
            print("Calling parent method")
        def set_attr(self, attr):
            Parent.parent_attr = attr
        def get_attr(self):
            print("Parent attribute:", Parent.parent_attr)

    class Child(Parent):  # Definicija na klasata - dete
        def __init__(self):
            print("Calling child constructor")
        def child_method(self):
            print("Calling child method")


    c = Child()
    # Calling child constructor
    c.child_method()
    # Calling child method
    c.parent_method()
    # Calling parent method
    c.set_attr(200)
    c.get_attr()
    # Parent attribute