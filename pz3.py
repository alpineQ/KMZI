with open('result.txt') as file:
    text = file.read()

freq_by_length = {}

for length in range(3, 7):
    freq_by_length[length] = {}
    for index in range(len(text)):
        word = ''
        for delta in range(length, 0, -1):
            word += text[index - delta]
        if word in freq_by_length[length]:
            freq_by_length[length][word] += 1
        else:
            freq_by_length[length][word] = 1

for length in freq_by_length:
    frequency_list = list(freq_by_length[length].items())
    frequency_list.sort(key=lambda i: i[1])
    print(f'---------------------------------------------\nLength: {length}')
    for stat in frequency_list:
        if stat[1] >= 3:
            print(f'{stat[0]}: {stat[1]}')
