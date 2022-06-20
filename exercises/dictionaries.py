# Function for converting items of dictionary into List of Lists format
def items_dict_lofl(given_dict):
    items = given_dict.items()
    list_of_items = [] * len(items)
    for item in items:
        list_of_items.append([item[0], item[1]])
    return list_of_items


if __name__ == "__main__":
    d = {'user': 'Stefan', 'password': 'Belchev221997!@#$%^&', 'authentication': 'two-side'}
    print(d)
    print(f"""Values of the dictionary keys are : {d.values()}""")
    print(f"""Keys of the dictionary are : {d.keys()}""")
    print(f"""Items in format list of tuples : {d.items()}""")
    items_dict = d.items()
    items_dic_tuple_of_tuples = tuple(items_dict)
    print(f'Items in format tuple of tuples: {items_dic_tuple_of_tuples}')
    items_dic_list_of_lists = items_dict_lofl(d)
    print(f'Items in format list of lists: {items_dic_list_of_lists}')
    # Changing value of key
    d['user'] = 'Stefan123'
    # Printing new value of the key
    value_user = d['user']
    print(value_user)
    print(d['user'])
    print(d.values())
    # Inserting new key with value
    d['id'] = '4321'
    print(d)
    del(d['id'])
    print(d)
    d.clear()
    print(d)
