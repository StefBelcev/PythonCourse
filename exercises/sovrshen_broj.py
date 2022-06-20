def sovrshen_broj(broj):
    suma = 0
    for n in range(1, broj):
        if broj % 2 == 0:
            suma += n
    if suma == broj:
        print(f'Brojot {broj} e sovrshen')
    else:
        print(f'Brojot {broj} ne e sovrshen')

if __name__ == "__main__":
    broj = eval(input())
    sovrshen_broj(broj)
