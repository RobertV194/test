# colors = ['red', 'green', 'white', 'green']
# colors.remove('green')
# colors.pop(1)
# colors.extend(('yellow', 'black'))
# print(colors)

# lst1 = ['hello', 'welcome', 'bye']
# lst2 = ['Andriy', 'back']
# # hello Andriy welcome back
# for i in range(min(len(lst1), len(lst2))):
#     print(lst1[i], lst2[i])
#
# max_lst = (
#     lst1
#     if len(lst1) > len(lst2) and len(lst1) != len(lst2)
#     else lst2
# )
# # print(max_lst)
# for i in max_lst[len(max_lst)-1:]:
#     print(i)


# lst1 = ['hello', 'welcome', 'bye']
# lst2 = ['Andriy', 'back']

# zipped_lst = list(zip(lst1, lst2))
# print(zipped_lst)
# for i, j in zipped_lst:
#     # print(i, j)
#     print(i)


# colors = ['red', 'green', 'white', 'yellow']
# print(colors[1:3])
# print(colors[len(colors)-1])

# colors = ['red', 'green', 'white', 'yellow']
# print('white' in colors)
# print('blue' in colors)
# print(1 in 101)


# items = ['qwerty', 101, True, 'hello', 'bye', None]
# filtered_items = []
# for i in items:
#     if type(i) == str:
#         filtered_items.append(i)
#
# print(filtered_items)


# colors = ['red', 'green', 'white', 'yellow',
#           'green', 'white', 'black']
# print(colors)
# ['red', 'green', 'white', 'yellow', 'black']
# new_colors = []
#
# for i in colors:
#     if i not in new_colors:
#         new_colors.append(i)

# print(new_colors)


# colors = ['red', 'green', 'white', 'yellow',
#           'green', 'white', 'black']
# # ['red', 'yellow', 'black']
# new_list = []
# for i in colors:
#     if colors.count(i) == 1:
#         new_list.append(i)
#
# print(new_list)


# for i in range(4):
#     for j in range(4):
#         print(i, j)

# countries_cities = [['Ukraine', 'Kyiv'], ['France', 'Paris'],
#                     ['Germany', 'Berlin']]
# cities = ['Paris', 'Berlin']
#
# for i in cities:
#     for j in countries_cities:
#         if i in j:
#             print(j[0])

#
# keyboard = ['1.,?!', '2abc', '3def', '4ghi', '5jkl', '6mno',
#             '7pqrs', '8tuv', '9wxyz', "*'-+=", '0 ', '#']
# message = 'hey'
#
# for i in message:
#     for j in keyboard:
#         if i in j:
#             print(j)