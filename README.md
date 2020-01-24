# Caesar
 Automatically detects the Caesar shift in ciphertext using letter frequency.

## Usage
`
python caesar.py ciphertext.txt
`

A [letter frequency distribution](https://en.wikipedia.org/wiki/Letter_frequency) is stored in a CSV file. You can add your own rows to the file if you wish to try other distributions, or you can directly run analyzeText.py to append rows to the file by analyzing a text file: `python analyzeText.py sample_english_text.txt`. This will gather the necessary statistics, and then you can select the row by changing the appropriate line in caesar.py.
