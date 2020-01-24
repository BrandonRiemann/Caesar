"""
This module generates a dictionary containing various statistics gathered from either a string
or text file.

In particular, the single and double letter frequencies are recorded, as well as a few other
descriptors.

Alternatively, you can run this code directly to save the dictionary to a csv file.

Brandon Sachtleben
"""

import pandas as pd
import sys
from collections import Counter

def generate_dict(str, file = False):
    # single_letter_dist - key: letter (a-z), value: percentage of letters in text using letter
    single_letter_dist = {}

    # double_letter_counts - key: aa, ab, ..., zz; value: number of times the sequence appears
    double_letter_counts = {}

    # first_letter_counts - key: a_1, b_1, ..., z_1; value: frequency of first letter of word
    first_letter_counts = {}

    if file:
        input_file = open(str, 'r')
        input = input_file.read().lower()
        input_file.close()
    else:
        input = str.lower()

    counter = Counter(input)

    # Number of letters in the text
    letter_count = len(input) - input.count('\n')

    words = input.split()

    # Number of words in the text
    word_count = len(words)

    # Length of the longest word in the text
    longest_word_len = max(map(len, words))

    # Length of the shortest word in the text
    shortest_word_len = min(map(len, words))

    # Average word length
    avg_word_len = sum(map(len, words)) / len(words)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for c in alphabet:
        single_letter_dist[c] = counter[c] / letter_count
        first_letter_counts[c + '_1'] = 0

    double_count = 0
    first_count = 0

    for word in words:
        first_letter_counts[word[0] + '_1'] += 1
        first_count += 1

        for i in range(0, len(word)-1):
            double_count += 1

    for c in alphabet:
        for d in alphabet:
            try:
                double_letter_counts[c + d]
            except:
                double_letter_counts[c + d] = 0

            for word in words:
                for i in range(0, len(word)-1):
                    if word[i] + word[i+1] == c + d:
                        double_letter_counts[c + d] += 1

    # double_letter_dist - key: aa, ab, ..., zz; value: percentage with this sequence
    double_letter_dist = {}
    for key, val in double_letter_counts.items():
        double_letter_dist[key] = val / double_count

    first_letter_dist = {}
    for key, val in first_letter_counts.items():
        first_letter_dist[key] = val / first_count

    dict = {'letter_count': letter_count,
            'word_count': word_count,
            'longest_word_len': longest_word_len,
            'shortest_word_len': shortest_word_len,
            'avg_word_len': avg_word_len,
            **single_letter_dist,
            **double_letter_dist,
            **first_letter_dist
            }

    return dict

if __name__ == "__main__":
    df = pd.DataFrame(generate_dict(sys.argv[1], file=True), index=[0])
    df.to_csv('data.csv', mode='a', header=False)
