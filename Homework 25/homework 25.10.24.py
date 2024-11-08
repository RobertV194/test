import multiply
import sum
import minus
import divide

while True:
    option = input('''Enter your option
1 to multiply
2 to sum
3 to minus
4 to divide
5 to quit   
''')

    if option == '1':
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        a = multiply.multiply(num1, num2)
        print(f'result: {num1} * {num2} = {a}')

    if option == '2':
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        b = sum.sum(num1, num2)
        print(f'result: {num1} + {num2} = {b}')

    if option == '3':
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        c = minus.minus(num1, num2)
        print(f'result: {num1} - {num2} = {c}')

    if option == '4':
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        d = divide.divide(num1, num2)
        print(f'result: {num1} / {num2} = {d}')

    if option == '5':
        break

    else:
        print('No such option, try again')







