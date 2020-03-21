""" Вспомогательные функции """
from itertools import zip_longest


def get_input(filepath):
    """ Чтение данных из файла """
    text = []
    with open(filepath) as file:
        for line in file:
            for letter in line.split():
                text.append(letter)
    return text


def change_text(text, substitute):
    """ Простая замена """
    for index, elem in enumerate(text):
        if elem in substitute:
            text[index] = substitute[elem]

    return text


def count_frequency(text):
    """ Подсчёт частотности """
    frequency = {}
    bigrams = {}
    trigrams = {}

    for index, elem in enumerate(text):
        if elem in frequency:
            frequency[elem] += 1
        else:
            frequency[elem] = 1

        frequency_list = list(frequency.items())
        frequency_list.sort(key=lambda i: i[1])

        bigram = text[index - 1] + ' ' + text[index]
        if bigram in bigrams:
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1

        trigram = text[index - 2] + ' ' + text[index - 1] + ' ' + text[index]
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
    for freq, bigram, trigram in zip_longest(frequency_list,
                                             bigrams_list,
                                             trigrams_list,
                                             fillvalue=[' ', ' ']):
        output += f'{freq[0]}: {frequency[freq[0]]}\t\t' \
                  f'{bigram[0]}: {bigrams[bigram[0]]}\t\t' \
                  f'{trigram[0]}: {trigrams[trigram[0]]}\n'
    return output


def format_text_string(text_list):
    """ Преобразование из списка в строку """
    str_text = ''
    for letter in text_list:
        str_text += letter + ' '

    return str_text
