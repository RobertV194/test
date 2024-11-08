#Домашня робота за другу тему

# first_name = 'Robert'
# last_name = 'Vedmedenko'
# age = 13
# population_of_Zaporizhzhia = 758011
# print(first_name + ' ' + last_name + ', ' + str(age) + ', ' + str(population_of_Zaporizhzhia))
#
# side_1 = int(input('Enter the first side of the rectangle:'))
# side_2 = int(input('Enter the second side of the rectangle:'))
# rectangle_area = side_1 * side_2
# print(f'The area of the rectangle = {rectangle_area}')


# first_name = 'Robert'
# last_name = 'Vedmedenko'
# age = 13
# population_of_Zaporizhzhia = 758011
# print(first_name + ' ' + last_name + ', ' + str(age) + ', ' + str(population_of_Zaporizhzhia))
#
# side_1 = int(input('Enter the first side of the rectangle:'))
# side_2 = int(input('Enter the second side of the rectangle:'))
# rectangle_area = side_1 * side_2
# print(f'The area of the rectangle = {rectangle_area}')



# Домашня робота за третю тему

# num1 = 8
# num2 = 2
# example = (num1 % num2)
#
# if not example:
#     print(f'Так, {num1} ділиться на 2')
# else:
#     print(f'Ні, {num1} не ділиться на 2')
#
#
# student_name = 'Данило'
# student_surname = 'Ткаченко'
# points = 82
#
# if points >= 80 and student_name:
#     print(f'{student_surname} склав іспит.')
# else:
#     print(f'{student_surname} не склав іспит.')



# Домашня робота за четверту тему

# suma = 0
# for i in range(1, 100, 2):
#     suma += i
#
# print(suma)
#
#
#
# word = 'pineapple'
# counter = 0
#
# for i in word:
#     if i == 'p':
#         counter += 1
#
# print(counter)




# Домашня робота за п'яту тему

# homework

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# squares = []
# for number in numbers:
#     squares += (number ** 2,)
# print(squares)
#
#
#
# chars = [5, 100, 200]
# result = int(f"{chars[0]}{chars[1]}{chars[2]}")
# print(result)




# Домашня робота за шосту тему


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_of_the_numbers = 0
# for num in numbers:
#     if num % 2 != 0:
#         sum_of_the_numbers += num
#
# print(sum_of_the_numbers)
#
#
#
# continents_of_the_Western_Hemisphere = ['North America', 'South America']
# continents_of_the_Eastern_Hemisphere = ['Eurasia', 'Africa', 'Australia', 'Antarctica']
# all_continents = continents_of_the_Western_Hemisphere + continents_of_the_Eastern_Hemisphere
# all_continents.sort()
# print(all_continents)







# nums = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new_nums = []
#
# for i in nums:
#     if i not in new_nums:
#         new_nums.append(i)
#
# print(new_nums)



# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = len(list) - 1
# while index >= 0:
#     print(list[index])
#     index -= 1



# while True:
#     option = input('''Enter option:
# 1) to create a list and reverse it
# 2) to quit
# Your choice:''')
#
#     if option == '1':
#         numbers = []
#         j = int(input('Enter quantity of elements in list:'))
#
#         for i in range(j):
#             num = int(input(f'Enter element number {i + 1}:'))
#             numbers.append(num)
#
#         reverse_numbers = []
#         for i in range(len(numbers)):
#             reverse_numbers.insert(0, numbers[i])
#
#         print('Reversed numbers:')
#         for num in reverse_numbers:
#             print(num)
#
#     elif option == '2':
#         print('Exit option')
#         break
#     else:
#         print('No option, try again')




# Домашня робота за восьму тему


# line = '12Hel45lo b8ye5'
# new_line = ''
# nums = '0123456789'
# for i in line:
#     if i not in nums:
#         new_line += i
# print(new_line)





# a = [2, 4, 6]
# result = 0
#
# for i in range(len(a)):
#     operation = f'{a[i]} / {i + 1}'
#     value = a[i] / (i + 1)
#     result += value
#     print(f'{operation} = {value}')
#
#
# print(f'Результат: {result}')




# Домашня робота за дев'яту тему

# завдання 1


# surname = 'Vedmedenko'
# max_count = 0
# most_common_letter = ''
#
# for letter in surname:
#     count = surname.count(letter)
#     if count > max_count:
#         max_count = count
#         most_common_letter = letter
#
#
# print(f'In surname [{surname}] letter [{most_common_letter}] meets [{max_count}] times')

# завдання 2 варіант 1

# word = 'HeLLo WoRLD'
# print(f'{word} ===> {word.swapcase()}')



# завдання 2 варіант 2

# word = 'HeLLo WoRLD'
# new_word = ''
#
# for i in word:
#     if i.isupper():
#         new_word += i.lower()
#     if i.islower():
#         new_word += i.upper()
#
# word1 = new_word[:5]
# word2 = new_word[5:]
# new_word1 = word1 + ' ' + word2
#
# print(f'{word} ===> {new_word1}')




# Домашня робота за десяту тему




# завдання 1


# names = ['Maks', 'Andriy', 'Ihor', 'Artem', 'Nastia', 'Nastia', 'Artem']
# unique_names = []
#
# for name in names:
#     if names.count(name) == 1:
#         unique_names.append(name)
#
# new_names = ', '.join(unique_names)
# print(f'Unique names: {new_names}')


# завдання 2

# nums = {5, 1, 2, 6, 9, 3}
#
# min_number = min(nums)
# max_number = max(nums)
#
# sum_of_min_and_max_numbers = min_number + max_number
#
# print(f'The smallest number is [{min_number}], the biggest number is [{max_number}] | Their sum = [{sum_of_min_and_max_numbers}]')






# Домашня робота за одинадцяту тему




# завдання 1

# num1 = 5
# num2 = 7
#
# if num1 >= num2:
#     max_num = num1
#     min_num = num2
# else:
#     max_num = num2
#     min_num = num1
#
# result = 0
#
# for i in range(min(num1, num2), max(num1, num2)+1):
#     result += i
#
# print(result)



# завдання 2 варіант 1

# words = ['apple', 'pear', 'pineapple', 'banana', 'plum', 'orange']
# the_longest_word = ''
# suma = 0
#
# for i in words:
#     if len(i) > len(the_longest_word):
#         the_longest_word = i
#         suma = len(the_longest_word)
# print(f'the longest word is: [{the_longest_word}], this word concludes: [{suma}] symbols')



# завдання 2 варіант 2

# lst = ['apple', 'pear', 'pineapple', 'banana', 'plum', 'orange']
# the_longest_word = ''
# suma = 0
#
# for the_longest_word in lst:
#     if len(the_longest_word) > len(lst):
#         suma = len(the_longest_word)
#
#         print(f'The longest word is: [{the_longest_word}], this word concludes: [{suma}] symbols')





# Домашня робота за дванадцяту тему





# завдання 1

# names_and_colors = {'Maks': 'yellow', 'Ivan': 'white', 'Dima': 'orange', 'Mark': 'green'}
# names_and_colors['Maks'] = 'black'
# names_and_colors['Ivan'] = 'blue'
# print(names_and_colors)




# завдання 2

# dict = {
#     'name': 'Андрій',
#     'age': 19,
#     'city': 'Львів'
# }
#
# dict['location'] = dict.pop('city')
#
# print(dict)





# Домашня робота за тринадцяту тему

# завдання 1

# scores = {
#     'Maks': 4,
#     'Ivan': 3,
#     'Stepan': 5,
#     'Andriy': 5,
#     'Oleh': 2
# }
#
# good_scores = {}
#
# for k, v in scores.items():
#     if v >= 4:
#         good_scores[k] = v
#
# print(good_scores)



# завдання 2

# city_temperature = {
#     'Kyiv': 23,
#     'Berlin': 18,
#     'Helsinki': 16,
#     'Oslo': 19,
#     'Rome': 25
# }
# temperature = city_temperature.values()
#
# if temperature:
#     average_temperature = sum(temperature) / len(temperature)
#     print(f'The average temperature in the cities are: {average_temperature} degrees Celsius')






# Домашня робота за чотирнадцяту тему

# завдання 1

a = 'rfpekkrrf'
dct_a = {}

for i in set(a):
    dct_a[i] = a.count(i)

p = []

for i in sorted(a, key=a.count):
    if i not in p:
        p.append(i)
print(p[-3:])




# завдання 2

# Приклад словника
numbers = {'a': 3, 'b': 5, 'c': 3}
result = 1
for v in numbers.values():
    result *= v
print('Result is:', result)
