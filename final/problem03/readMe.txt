## How to run the code:
```teminal
problem03 % python3 problem03.py < input3-1.txt

```

## description
- Read the input file
- Define the recursive function dp(currSeq, prevIdx) with memoization using @lru_cache.
- Determine the current and alternate sequences based on currSeq (0 for A, 1 for B).
- Iterate over the current sequence starting from prevIdx + 1.
- Check if the current element is greater than the last picked element from the alternate sequence or if prevIdx == -1.
- Calculate the maximum length by picking the current element and calling dp for the alternate sequence.
- Return the maximum length after exploring all valid options.
- Call dp(0, -1) and dp(1, -1) to start from both sequences with no prior element.
- Return the maximum result of the two calls.