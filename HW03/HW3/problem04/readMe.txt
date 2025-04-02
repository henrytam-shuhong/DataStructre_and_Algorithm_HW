// For each problem submit your commented code, a readme.txt describing your solution, the heart of your algorithm and directions to run your submission.

## How to run the code:
```teminal
python3 ghostbuster.py < inputFile.txt

```

## description
- Use production knowledge to determine whether two segments intersect
	- To determine whether two line segments intersect, you can determine whether the two endpoints of the two line segments are on their respective sides. Correspondingly, you need to use the positive and negative values ​​​​of the two-dimensional vector cross-product results to represent the characteristics of the vector rotation direction.
- transfer inputFile into a two dimension array (matrix)
- use two indexes to compare two items in the array recursively
	- as long as one pair of segments intersect, the ghosts are not eliminated