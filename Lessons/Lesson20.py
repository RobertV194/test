from options import read_file, view_items, add_item, delete_item, edit_item, clear_file


def main(file):
    shop_items = read_file(file)
    while True:
        action = input('Enter your option [add, view, edit, delete, clear, sorted by name, exit]: ')
        if action == 'view':
            view_items(shop_items)
        elif action == 'add':
            add_item(file, shop_items)
        elif action == 'delete':
            delete_item(file, shop_items)
        elif action == 'edit':
            edit_item(file, shop_items)
        elif action == 'clear':
            clear_file(file)
        elif action == 'exit':
            break



if __name__ == '__main__':
    main('shop.txt')




# def func(num):
#     for i in range(1, num + 1):
#         file_name = f'file{i}.txt'
#         with open(file_name, 'w') as file:
#             file.write(f'{i}')
#
#
# print(func(5))