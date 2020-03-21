""" Разделение данных для шифра разнозначной замены """

# pylint: disable=invalid-name
text = ''
with open('SRZ.txt') as file:
    for line in file:
        text += line[0:-1]

bigram_freq = {}
for index, elem in enumerate(text):
    bigram = text[index - 1] + text[index]
    if bigram not in bigram_freq:
        bigram_freq[bigram] = 1
    else:
        bigram_freq[bigram] += 1

digit_freq = {}

for bigram in bigram_freq:
    first_digit = str(bigram)[0]
    if first_digit not in digit_freq:
        digit_freq[first_digit] = bigram_freq[bigram]
    else:
        digit_freq[first_digit] += bigram_freq[bigram]

digit_freq_list = list(digit_freq.items())
digit_freq_list.sort(key=lambda i: i[1])

most_freq_digit = [digit_freq_list[-1][0], digit_freq_list[-2][0], digit_freq_list[-3][0]]

print('Reformatting, assuming these are most frequent digits:')
for digit in most_freq_digit:
    print(f'{digit} found {digit_freq[digit]} times')

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

with open("formatted_text.txt", "w") as file:
    file.write(formatted_text)

print('Check formatted_text.txt')
