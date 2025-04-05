## How to run the code:
```teminal
python3 problem02.py <input01.txt

```

## description
- read the input file
- count the frequency of each character in the input file
- create a frequency table for each character in the input file
    - print out the frequency map
- create nodes for all char and put them into the priority heap with frequency as indicators
- create a binary tree or huffman tree where:
    - each leaf node represents a character
    - internal nodes represent combined frequencies and nodes
    - print out the tree
- generate the specific binary code by traversing the tree
    - every time passing the left node add 0
    - every time passing the right node add 1
- record the binary code for each character
- use the binary codes to encode the input text
    - write out the output code to a file