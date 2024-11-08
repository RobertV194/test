def count_names_in_file(file_name):
    count_name = {}
    with open(file_name, encoding='utf-8') as file:
        names = file.read().split()
        for i in names:
            if i in count_name:
                count_name[i] += 1
            else:
                count_name[i] = 1
    return count_name

count_name = count_names_in_file('file_names.txt')



def the_most_common_name(count_name):
    the_commonest_name = max(count_name)
    return the_commonest_name, count_name[the_commonest_name]

the_commonest_name, count = the_most_common_name(count_name)



print(f'The most common name is: [{the_commonest_name}] it meets [{count}] times')

