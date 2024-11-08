# n = 16
# # x = 0
# # divisors = []
# # while x < 16:
# #     x += 1
# #     if n % x == 0:
# #         divisors.append(x)
# # print(divisors)


# alph = 'abcdefghijklm'
# word = 'hello'
# counter = 0
# for i in word:
#     if i not in alph:
#         counter += 1
#         print(f'{counter} / {len(word)}')


# data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# lvl = []
#
# for i in data:
#     if i[0] > 55 and i[1] > 7:
#         lvl.append("Senior")
#     else:
#         lvl.append("Junior")
# print(lvl)


# list = ['a', 'b', 'a', 'g', 'f', 'f']
# new_list = []
# for i in list:
#     if list.count(i) == 1:
#         new_list.append(i)
# print(new_list)


# words = ['hello', 'bye', 'qwerty', 'hi']
# new_words = [len(i) for i in words]
# print(new_words)


# num = 1944
# print(len(str(num)))


my_games = []
while True:
    game = input('Enter a game`s name: ')
    if game == 'quit':
        break
    my_games.append(game)

for game in my_games:
    print(game.index(game))

