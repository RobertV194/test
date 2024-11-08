word = 'qwe1asd2zxc36'
nums = 0
letters = 0

for i in word:
    if i.isdigit():
        nums += 1
    if i.isalpha():
        letters += 1

print(f'numbers: {nums} | letters: {letters}')



s = 'Boat Rudder Mast Boat Hull'
lower = 0
upper = 0

for i in s:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1

print(f'upper: {upper} | lower: {lower}')





