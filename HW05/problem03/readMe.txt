
## How to run the code:
```teminal
python3 problem03.py <input3-1.txt

```

## description
- create a TreeNode class consisting of four attributes:
     - value,
     - index in the original array,
     - tags: demonstrate which original array it belongs to
     - children: the chidren nodes of the current node
- create a Tree ADT compraising four methods
    - add_node
    - find_node
    - find_longest_path
    - traverse
- traverse the array A, and for each element, build up a tree using the element as a root and conform to the requirements.
    - every path from the root to leaf represents a possible required sequence.
- traverse the established tree to find the longest path.
    - this path is the longest sequence starting from this specific element of this specific array
- after traverse the array A, find out the longest possible sequence, which is build up starting from an element in array A
- implement the same algorithm to array B, find out the longest possible sequence, which is build up starting from an element in array B
- pick the longer sequence among outcomes from array A and array B as the ultimate result.

