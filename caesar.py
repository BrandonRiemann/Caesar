import pandas as pd
import sys
from sklearn.metrics import mean_absolute_error
import numpy as np
from analyzeText import generate_dict

# Shift each letter in given string by a fixed integer amount (e.g., shift of 2 takes a->c)
def shift_by(str, shift):
    shifted = ""
    for word in str.split():
        for i in word:
            if i.isalpha():
                start = ord('a') if i.islower() else ord('A')
                shifted += chr((ord(i)+shift-start) % 26 + start)
            else:
                shifted += i
        shifted += " "

    shifted = shifted[:-1] # Remove the trailing space
    return shifted

alphabet = 'abcdefghijklmnopqrstuvwxyz'
features = ['letter_count', 'word_count', 'longest_word_len', 'shortest_word_len', 'avg_word_len']
targets = [c for c in alphabet]
targets.extend([c + d for c in alphabet for d in alphabet])
targets.extend([c+'_1' for c in alphabet])

df = pd.read_csv('data.csv')

X = df[features].fillna(0)
y = df[targets].fillna(0)

# Select one row from the dataframe (0 = data from https://en.wikipedia.org/wiki/Letter_frequency)
y = y.iloc[0]

input_file = open(sys.argv[1], 'r')
input = input_file.read()

print("Ciphertext: " + input)

dict = generate_dict(input)
errors = []

for i in range(0, 26):
    shifted = shift_by(input, -i)

    dict = generate_dict(shifted)
    error = mean_absolute_error([y], [list(dict.values())[5:]])
    errors.append(error)
    # print("MAE for shift of %d: %.4f" % (i, error))

print("Best guess: Shift of %d" % np.argmin(errors))
print("Plaintext: " + shift_by(input, -np.argmin(errors)))
