def print_birthday(name):
    for k in birthday_dict.keys():
        if name == k:
            return birthday_dict[name]


if __name__ == "__main__":
    birthday_dict = { 'Stefan': '02/02/1997', 'Mia': '12/12/1996', 'Ana': '01/17/1991', 'Aleksandar': '03/03/1997'}
    birthday_dict_names = birthday_dict.keys()
    print(birthday_dict_names)
    print(birthday_dict.items())
    print(f'Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:')
    for name in birthday_dict_names:
        print(name)
    print(f'Koj rodenden e potrebno da se prebara')
    entered_name = input()
    birthday = print_birthday(entered_name)
    print(f'Rodendenot na ' + entered_name + ' e na ' + birthday)

