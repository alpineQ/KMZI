""" Разделение данных для шифра разнозначной замены """
from sys import argv
# pylint: disable=invalid-name

input_filepath = 'test_inputs/SRZ.txt' if len(argv) < 2 else argv[1]
print(f'Беру данные из {input_filepath}')
with open(input_filepath) as file:
    text = file.read().replace('\n', '')


digit_freq = {letter: text.count(letter) for letter in text}
digit_freq_list = list(digit_freq.items())
digit_freq_list.sort(key=lambda i: i[1], reverse=True)

most_freq_digit = [digit_freq_list[0][0], digit_freq_list[1][0], digit_freq_list[2][0]]

print('Расставляю пробелы, предполагая, что эти цифры наиболее частотные:')
for digit in most_freq_digit:
    print(f'{digit} найдена {digit_freq[digit]} раз')

formatted_text = text
ft_index = 0
index = 0

while index < len(text):
    if text[index] in most_freq_digit:
        formatted_text = formatted_text[0: ft_index + 2] + ' ' + formatted_text[ft_index + 2: -1]
        ft_index += 3
        index += 2
    else:
        formatted_text = formatted_text[0: ft_index + 1] + ' ' + formatted_text[ft_index + 1: -1]
        ft_index += 2
        index += 1

output_filepath = 'result.txt' if len(argv) < 3 else argv[2]
with open(output_filepath, "w") as file:
    file.write(formatted_text.rstrip())

print(f'\nЗаписано в {output_filepath}')
