# nums = {5, 1, 2, 6, 9, 3}
# nums.discard(min(nums))
# nums.discard(max(nums))
# suma = sum(nums)
# print(suma)


# nums = [5, 1, 1, 3, 4, 10, 10, 1, 2, 7, 7]
# min_number = min(nums)
# max_number = max(nums)
# print(sum(set(nums))-max(nums)-min(nums))


# lst = ['qwq', 'hello', 'bye', 'abba', 'ewe']
# for i in lst:
#     if i == i[::-1]:
#         print(i)


# numbers = [111, 141, 223, 755, 919, 333]
# for i in numbers:
#     if str(i) == str(i)[::-1]:
#         print(i)

# word = 'accdeebb'
# new_word = []
# for i in word:
#     if word.count(i) > 1:
#         if i not in new_word:
#             new_word.append(i)
# print(' '.join(new_word))


# a = 'hello world world hi bye hello'
# splited_a = a.split()
# new_a = []
#
# for i in splited_a:
#     if a.count(i) > 1:
#         new_a.append(i)
# print(' '.join(new_a))


a = 'qwertyavnbqon'
vowels = 'aeiou'
first = ''
last = ''

for i in a:
    if i in vowels:
        if not first:
            first = i
        last = i

print(f'First vowel is: {first}')
print(f'Last vowel is: {last}')