# Аритметички изрази +, -, *, ** : во Python :
# 1. Собирање (+) --> оператор + (addition)
# 2. Одземање (-) --> оператор - (subtract)
# 3. Множење  (*) --> оператор * (multiply)
# 4. Делење   (:) --> оператор / (division)
# 5. Степенисување (^) --> оператор ** (exponent)

if __name__ == "__main__":
    # Иницијализација на променливи, дополнително објаснување на термини за податочни типови
    # на променливи и начин на доделување вредност и споредба на вредности на променливи
    a = 5
    b = 10
    c = 6
    d = 3

    # Оператор за собирање (+)
    sobiranje = a + b # 10 + 5 = 15
    print(f'\t Збирот на броевите {a} и {b} e', sobiranje)

    # Оператор за одземање (-)
    odzemanje = b - a # 10 - 5 = 5
    print(f'\t Разликата на броевите {b} и {a} e', odzemanje)

    # Оператори за делење (//), (/), (%)
    # Целобројно делење
    cel_delenje = b // c # 10 // 6 = 1
    print(f'\t Целобројно делење на броевите {b} и {c} e', cel_delenje)
    # Децимално делење
    dec_delenje = b / c # 10 / 6 = 1.67
    print(f'\t Децимално делење на броевите {b} и {c} е', dec_delenje)
    # Остаток од делењето
    ostatok = b % c # 10 % 6 = 4
    print(f'\t Остатокот при делењето на броевите {b} и {c} e', ostatok)

    # Оператор за множење (*)
    mnozenje = a * b
    print(f'\t Множење на броевите {a} и {b} e', mnozenje)

    # Оператор за степенување (**)
    stepenuvanje = d ** a
    print(f'\t Степенување на бројот {d} со основа {a} e', stepenuvanje)