
## How to run the code:
```terminal
python3 problem02.py < pandemic_input2

```

## description

- for any two countries, if their coordinates satisfy certain rules, they will infect certain neighbors to form a Square. 
	- ensure the new infected countries are still in the grid

- if all infected countries form a square together, the infection terminates.
- if the edge length of this final square is less than the edge length of the grid, then there will be healthy countries left
	- if there are healthy countries, there will be  some 0s in the Matrix 

- create a Matrix where if a country is infected, the number in the corresponding array is 1; otherwise, the number of the item in the array is 0


- flatten the matrix and find the rule that 
	- if one country’s index is x,  the index of the country compared with it to create a new infected country and the index of new infected countries are:
		- x + 6 //  x + 1, x+ 5
		- x - 6 // x - 1, x -5
		- x - 4 // x + 1,  x -5
		- x + 4 // x -1,  x + 5
     - however, if the country is in the first column, x-4 is not its company. Also, if the country is in the last column of the matrix, x+ 4 is not its company. 
		- first column: 0, 5, 10, 15, ———> 5n  // not x-4 
 		- last column: 4, 9, 14, 19, ———> 5n-1 // not x+4


- count the number of zero after every infection
	- check if the last two zero-counters isn't the same, then repeat the infectedFlatedMatrix,
	- if they are the same, then means there are now more infections needed

- then check if there are 0 in the flattenedMatrix array 	
	- if all 0 are eliminated, then there are no healthy country