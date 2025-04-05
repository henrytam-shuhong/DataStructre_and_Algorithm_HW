'''
Downhill Skier
You are a downhill skier looking for an adventure. You will be dropped by helicopter as a
location of your choosing on a mountain. The mountain is represented as an m x n matric
of altitude values. Design an algorithm that determines the longest path you can follow
down the mountain such that each successive cell in your path has an altitude lower than
the previous cell.
Note: Each Cell has up to eight neighbors, directly adjacent horizontally, vertically or
diagonally.
You should submit a readme.txt file with an explanation of your code and algorithms. You
must provide exact instructions on how to run your code and you must submit screen
shots of your running code and printing your result to the console.


Sample input:
4
5
4 8 7 9 8
6 5 10 12 11
3 6 15 11 12
1 4 9 13 10
Ans: input1 = 9

'''

'''
- flatten the Matrix and sort all values into a descending priority queue, including their original coordinates in the Matrix
- calculated the longest path for each item in the priority queue.
     - the longest path of a specific cell is 1 plusing the maxium of longest path of all adjacent cells whose values are less then the current cell. 
- record the calculatd result in a new Matrix
- use a pointer to record the biggest value during the calculation and return it as a result in the end. 
'''
import sys

def longest_descending_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    memo = [[-1 for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(x, y):
        if memo[x][y] != -1:
            return memo[x][y]

        max_path = 0  # Path length is counted in steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] < matrix[x][y]:
                max_path = max(max_path, 1 + dfs(nx, ny))

        memo[x][y] = max_path
        return memo[x][y]

    longest_path = 0
    for i in range(rows):
        for j in range(cols):
            longest_path = max(longest_path, dfs(i, j))

    return longest_path


# Example Input
# matrix = [
#     [4, 8, 7, 9, 8],
#     [6, 5, 10, 12, 11],
#     [3, 6, 15, 11, 12],
#     [1, 4, 9, 13, 10]
# ]

read = sys.stdin.read().splitlines()
matrix = []
for i in range(2,len(read)):
    temp = read[i].split(' ')
    result = list(map(int, temp))
    matrix.append(result)

# print(matrix)
print("Longest Descending Path (in steps):", longest_descending_path(matrix))
