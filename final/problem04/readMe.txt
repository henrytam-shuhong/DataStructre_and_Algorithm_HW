## How to run the code:
```teminal
python3 problem04.py <ski_input1.txt


```

## description
- Create a matrix file for the input
- Build up a memorization matrix
- Iterate all cells and pick the biggest number whose longest path is smaller than the current value among the 8 adjacent cells.
- Recurrsively conduct it if the cell's longest path is currently unknown
- The base value is that when the current cell is the smallest cell among all adjacent cells.
- Record the already-known longest path value in the memorization matrix for reuse.
- use a pointer to point to the value longest path and return it in the end
