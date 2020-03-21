from itertools import zip_longest


def get_input(filepath):
    text = []
    with open(filepath) as file:
        for line in file:
            for letter in line.split():
                text.append(letter)
    return text


def change_text(text, substitute):
    for index, elem in enumerate(text):
        if elem in substitute:
            text[index] = substitute[elem]

    return text


def count_frequency(text):
    frequency = {}
    bigrams = {}
    trigrams = {}

    for i in range(len(text)):
        if text[i] in frequency:
            frequency[text[i]] += 1
        else:
            frequency[text[i]] = 1

        frequency_list = list(frequency.items())
        frequency_list.sort(key=lambda i: i[1])

        bigram = text[i - 1] + ' ' + text[i]
        if bigram in bigrams:
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1

        trigram = text[i - 2] + ' ' + text[i - 1] + ' ' + text[i]
        if trigram in trigrams:
            trigrams[trigram] += 1
        else:
            trigrams[trigram] = 1

    frequency_list = list(frequency.items())
    frequency_list.sort(key=lambda i: i[1], reverse=True)

    bigrams_list = list(bigrams.items())
    bigrams_list.sort(key=lambda i: i[1], reverse=True)

    trigrams_list = list(trigrams.items())
    trigrams_list.sort(key=lambda i: i[1], reverse=True)

    frequency.update({' ': ' '})
    bigrams.update({' ': ' '})
    trigrams.update({' ': ' '})
    output = 'Frequncy\t\tBigrams\t\tTrigrams\n'
    for freq, bigram, trigram in zip_longest(frequency_list, bigrams_list, trigrams_list, fillvalue=[' ', ' ']):
        output += f'{freq[0]}: {frequency[freq[0]]}\t\t{bigram[0]}: {bigrams[bigram[0]]}\t\t{trigram[0]}: {trigrams[trigram[0]]}\n'
    return output


def format_text_string(text_list):
    str_text = ''
    for letter in text_list:
        str_text += letter + ' '

    return str_text
