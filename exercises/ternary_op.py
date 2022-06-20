if __name__ == "__main__":
    # Ternary operators examples below
    a = 10
    b = 5
    fruit = 'apple'
    is_apple = True if fruit == 'apple' else False
    print(is_apple)
    max = a if a > b else b
    print('Max is', max)
    min = b if b < a else a
    print('Min is', min)