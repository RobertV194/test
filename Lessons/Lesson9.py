# nums = [2, 4, 6, 4]  # 2/1 + 4/2 + 6/3 + 4/4 = 7
# s = 0
for i in nums:
    s += i / (nums.index(i)+1)
# for i in range(len(nums)):
#     s += nums[i] / (i+1)
#
# print(s)

# sentence = 'hello world'
# print(sentence.count('l', 0, 5))

# name = 'ARTEM'
# print(name)
# new_name = name.lower()
# print(new_name)
# name = 'ARtEM !***'
# print(name.lower())

# name = 'anDriy !@&'
# print(name.upper())
# print(name)


# l = [1,2,3]
# print(l.append(4))
# print(l)

# intro = 'my name is AndDSG.SMVFLriy'
# print(intro.capitalize())

# name = 'andriy'
# print(name.capitalize())

# name = 'My name is Andriy'
# print(name.title())

# word = 'abracadbra'
# result = ''  # AbrAcAdAbrA
# for i in word:
#     ...


# word = 'abracadbra'
# result = ''
#
# for i in word:
#     if i == 'a':
#         result += i.upper()  # 'A'
#     else:
#         result += i
#
# print(result)


# name = 'My name is Andriy!!!!'
# print(name.swapcase())

# name = 'My name m is Andriy!!!!'
# print(name.find('m', 0, 6))
# print(name.index('x'))

# sentence = 'my name is Andriy. qwerty. asdzxc'
# lst = sentence.split('.')
# print(lst)

# s = "I am learning strings in Python. Some new methods got now."
# for i in s.split():
#     print(i)

# cities = ['Kyiv', 'Paris', 'London', 'Berlin']
# cities = 'Madrid Paris'
# cities_str = '=>'.join(cities)
# print(cities_str, type(cities_str))
#
# print(list('Paris'))