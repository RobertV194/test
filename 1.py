employee = {
    'John': {
        'salary': 2000,
        'start_date': 2020,
        'position': 'developer'
    },
    'Andriy': {
        'salary': 1000,
        'start_date': 2020,
        'position': 'developer'
    }
}

while True:
    option = input('''Enter your option
-a to add one more employee
-r to list all employee
-d to delete an employee
-u to update an employee's salary or position
-q to quit:

''')
    if option == '-a':
        name = input('Enter employee name: ')
        salary = int(input('Enter employee salary: '))
        start_date = int(input('Enter year: '))
        position = input('Enter employee position: ')

        if name in employee:
            print('This employee already exists')
        else:
            employee[name] = {
                'salary': salary,
                'start_date': start_date,
                'position': position
            }
            print('We added your employee')
    elif option == '-r':
        print('-' * 80)
        for name, data in employee.items():
            print(name)
            for k, v in data.items():
                print(f'{k}: {v}')
            print('-' * 80)
    elif option == '-d':
        name_to_del = input('Enter employee name to delete: ')
        if name_to_del in employee:
            del employee[name_to_del]
            print(f'We deleted {name_to_del} successfully')
        else:
            print('There is no such employee')
    elif option == '-u':
        name_to_update = input('Enter employee name to update: ')
        if name_to_update in employee:
            field = input('Which field do you want to update? (salary/position): ')
            if field == 'salary':
                new_salary = int(input('Enter new salary: '))
                employee[name_to_update]['salary'] = new_salary
                print(f'Salary for {name_to_update} updated successfully.')
            elif field == 'position':
                new_position = input('Enter new position: ')
                employee[name_to_update]['position'] = new_position
                print(f'Position for {name_to_update} updated successfully.')
            else:
                print('Invalid field. Please enter "salary" or "position".')
        else:
            print('There is no such employee')
    elif option == '-q':
        break
