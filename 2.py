# employee = {
#    'John': {
#         'salary': 2000,
#         'start_date': 2020,
#         'position': 'developer'
#     },
#     'Andriy': {
#         'salary': 1000,
#         'start_date': 2020,
#         'position': 'developer'
#     }
# }
#
#
# while True:
#     option = input('''Enter your option
# -a to add one more employee
# -p to change the employee`s position
# -s to change the employee`s salary
# -r to list all employee
# -d to delete an employee
# -q to quit:
#
# ''')
#     if option == '-a':
#         name = input('Enter employee name: ')
#         salary = int(input('Enter employee salary: '))
#         start_date = int(input('Enter year: '))
#         position = input('Enter employee position: ')
#
#         if name in employee:
#             print('This employee already exist')
#         else:
#             employee[name] = {
#                 'salary': salary,
#                 'start_date': start_date,
#                 'position': position
#             }
#             print('We added your employee')
#
#     elif option == '-p':
#         name_to_change = input('Enter employee name to change: ')
#         if name_to_change in employee:
#             new_position = input('Enter new position: ')
#             employee[name_to_change]['position'] = new_position
#             print(f'Position for {name_to_change} changed successfully')
#         else:
#             print('There is no such employee')
#
#     elif option == '-s':
#         name_to_change = input('Enter employee name to change: ')
#         if name_to_change in employee:
#             new_salary = int(input('Enter new salary: '))
#             employee[name_to_change]['salary'] = new_salary
#             print(f'Salary for {name_to_change} changed successfully')
#         else:
#             print('There is no such employee')
#
#     elif option == '-r':
#         print('-' * 80)
#         for name, data in employee.items():
#             print(name)
#             for k, v in data.items():
#                 print(f'{k}: {v}')
#             print('-'*80)
#
#     elif option == '-d':
#         name_to_del = input('Enter employee name to delete: ')
#         if name_to_del in employee:
#             del employee[name_to_del]
#             print(f'We deleted {name_to_del} successfully')
#         else:
#             print('There is no such employee')
#
#     elif option == '-q':
#         break






# def table_booking(surname, count_of_tables):
#
#     if len(surname) == 0:
#         return f'Please enter your surname'
#
#     if count_of_tables == 1:
#         return f'Person [{surname}] booked [{count_of_tables}] table'
#     if count_of_tables == 0:
#         return f'Person [{surname}] didn`t book any tables'
#     else:
#         return f'Person [{surname}] booked [{count_of_tables}] tables'
#
#
# print(table_booking('Petrov', 3))
# print(table_booking('Ivanov', 1))
# print(table_booking('Sidorov', 0))



# def sum_of_squares(nums):
#
#     return sum(i**2 for i in nums)
#
#
# print(sum_of_squares(nums=[1, 2, 3, 4, 5, 6]))











# def checked_word(word1, word2):
#
#     return sorted(word1) == sorted(word2)
#
#
# print(checked_word('wqrtey', 'qwerty'))




# def palindrome(word):
#
#     word = word.lower()
#     return word == word[::-1]
#
#
# print(palindrome('dud'))
# print(palindrome('ananas'))
# print(palindrome('a n a'))










# import math
#
# def func(R):
#     return math.pi * R**2
#
#
# print(func(8))



























