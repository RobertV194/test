def count_words_in_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)
count_words = count_words_in_file('file.txt')

print(f'Suma of words in file are [{count_words}]')



