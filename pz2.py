""" Афинная замена """
from sys import argv
# pylint: disable=invalid-name

input_filepath = 'test_inputs/input_pz2.txt' if len(argv) < 2 else argv[1]

with open('test_inputs/input_pz2.txt') as file:
    text = file.read()

possible_alpha = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
possible_beta = list(range(26))
popular_letter_combinations = ['ment', 'the', 'and']

for alpha in possible_alpha:
    for beta in possible_beta:
        text_attempt = ''
        for letter in text:
            new_letter = (alpha * (ord(letter) - 96) + beta) % 26
            if new_letter == 0:
                new_letter = 26
            text_attempt += chr(new_letter + 96)
        for popular_combination in popular_letter_combinations:
            if popular_combination in text_attempt:
                print(f'Alpha: {alpha}, Beta: {beta}: {text_attempt}')
                break
