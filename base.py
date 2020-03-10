from itertools import zip_longest


def get_input(filepath):
    text = ''
    with open(filepath) as file:
        for line in file:
            for letter in line.split():
                text += letter + ' '
    return text


def change_text(text, substitute):
    for change in substitute:
        pos = text.find(change)
        while pos != -1:
            text = text[0:pos] + substitute[change] + text[pos + 2:len(text)]
            print(len(text))
            pos = text.find(change)

    return text


def count_frequency(text):
    frequency = {}
    bigrams = {}
    trigrams = {}

    text_list = []

    for letter in text.split():
        text_list.append(letter)

    for i in range(len(text_list)):
        if text_list[i] in frequency:
            frequency[text_list[i]] += 1
        else:
            frequency[text_list[i]] = 1

        frequency_list = list(frequency.items())
        frequency_list.sort(key=lambda i: i[1])

        bigram = text_list[i - 1] + text_list[i]
        if bigram in bigrams:
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1

        trigram = text_list[i - 2] + text_list[i - 1] + text_list[i]
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





