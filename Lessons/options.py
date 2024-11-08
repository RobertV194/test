def read_file(file_name):
    shop_items = {}
    with open(file_name, encoding='utf-8') as file:
        for i in file:
            item = i.strip().split(', ')
            shop_items[item[0]] = item[1]
    return shop_items


def write_file(file_name, shop_items):
    with open(file_name, 'w', encoding='utf-8') as file:
        for k, v in shop_items.items():
            file.write(f'{k}, {v}\n')


def view_items(items):
    for k, v in items.items():
        print(k, v)


def add_item(file_name, items):
    item = input('Enter an item: ')
    quantity = input('Enter a quantity: ')
    items[item] = quantity
    print('You successfully added a new item')
    write_file(file_name, items)


def delete_item(file_name, items):
    item = input('Enter an item: ')
    if item not in items:
        print('There is no such item')
    else:
        del items[item]
        print('You  successfully deleted an item')
        write_file(file_name, items)


def edit_item(file_name, items):
    item = input('Enter an item: ')
    if item not in items:
        print('There is no such item')
    else:
        quantity = input('Enter a quantity: ')
        items[item] = quantity
        print('You successfully updated an item')
        write_file(file_name, items)


def clear_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.truncate(0)
    print(f'File cleared successfully')



