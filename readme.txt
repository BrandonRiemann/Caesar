How it works:

We first create a dataset with the following features:
* # Letters
* # Words
* Longest word length
* Smallest word length
* Average word length

Targets:
* Number of A's, B's, ..., Z's (26 columns)
* Number of double letter permutations (650 columns)
* Letter distribution (how many times one letter appears a distance from another letter) - e.g., maybe A is adjacent to(distance of 1 from) A 0 times, A is a distance of 2 from A 3 times, ..., counting up to the length of the word for each word in the text or up to maximum distance of 5. Do the same for all pairs of letters. (325*5=1625 columns)

Then, we can perform:
num_a = model.predict(X, y_num_a)

and so on.

We then compare our cipher's statistics against the predictions, performing such comparison for all 26 possible shifts.

The shift that minimizes the sum of squares of differences in the statistics is chosen.