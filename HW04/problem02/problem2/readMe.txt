
## How to run the code:
```terminal
 python3 problem2.py <fewest_1.txt

```

## description
compare the original string and the reverse string to check whether they are equal.

- read the input file
- sorting the input array in order to find the greatest number and the second biggest number, and so on.
- because if the number of elements whose sum is larger than the target is the smallest, we need to pick the biggest element each time.
- pick the largest element in the rest of the array and add it to the sum
- compare the new sum to the target to determine if this is the final answer.