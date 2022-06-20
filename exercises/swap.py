def swap(lista):
    return [(item2, item1) for item1, item2 in lista]


if __name__ == "__main__":
    lista = [('a', 1), ('b', 2), ('c', 3)]
    print(swap(lista))
