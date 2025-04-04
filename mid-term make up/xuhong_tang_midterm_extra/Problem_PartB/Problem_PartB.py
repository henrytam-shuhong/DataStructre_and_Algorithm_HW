'''
You will be given a file where the first line will contain the dimension of the matrix the number of rows followed by a space then
the number of columns
The next line will contain a set of symbols or values space separated which you must use to create a matrix with the same
properties as Part A:

e.g. every diagonal from top left to bottom right has the same symbol or value
E.G
5 4
! @ # $ % ^ & *
'''

'''
- read the file
- initiate a matrix container
- fill the first row and first column of the matrix, using the given symbols
- fill all other blank spaces of the matrix by assigning matrix[i][j] the value of matrix[i-1][j-1] when i>0 and j>0 
'''

import sys

def main():
    content = sys.stdin.read().strip().split('\n')
    numbers_of_matrix = content.pop(0).split(' ')
    row =  int(numbers_of_matrix[0])
    column = int(numbers_of_matrix[1])
    # print(row, column)
    content = content[0].split(' ')
    # print(content)
    matrix = []

    for i in range(row):
        matrix.append([])
        for j in range(column):
            if i == 0:
                matrix[0].append(content[j])
            elif j == 0:
                matrix[i].append(content[column+i-1])
            else:
                matrix[i].append(matrix[i - 1][j - 1])
    print(matrix)
    for i in matrix:
        print(" ".join(i))
main()