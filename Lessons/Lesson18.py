def check_word(word1, word2):
    return sorted(word1) == sorted(word2)


print(check_word('', ''))



# f = lambda x : x % 2
#
# def func(lst, lst_filter=None):
#     if not lst_filter:
#         return lst
#     res = []
#     for i in lst:
#         if lst_filter(i):
#             res.append(i)
#     return res
#
# print(func([3, 2, 1, 5, 4], f))


# import random
# import math
#
# print(random.randint(1, 100))
# print(math.pi)



import math

def func(R, pi):
    return pi * R**2


print(func(5, math.pi))



# import random
# def func(lst):
#     res_lst = []
#     for i in lst:
#         if len(i) >= 5:
#             res_lst.append(i)
#     return random.choice(res_lst)
#
#
#
# print(func(['Berlin', 'Paris', 'London', 'Lviv', 'Kyiv', 'Rio']))




# q = {}
#
# def counter(name, count = 3):
#     for i in range(count):
#         print(name)
#
# counter('Oleh', 6)
#
# q = {}
#
# def nums(num1, num2, num3, suma=0):
#     if suma:
#         return num1 + num2 + num3
#     return(num1, num2, num3)
#
# print(nums(1,2,3))
# print(nums(1,2,3, suma=True))