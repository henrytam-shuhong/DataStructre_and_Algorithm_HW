
'''
Your implementation must take a file from standard input with the following format:
The first line will contain the dimension of the matrix the number of rows followed by a space then the number of columns
The remainder of lines will be the row and column values of the matrix space separated.

E.G
5 4
! @ # $
% ! @ #
^ % ! @
& ^ % !
* & ^ %
'''

'''
- read the file
- build up a matrix data structure based on the input file
- traverse the matrix and determine whether matrix[i][j] == matrix[i-1][j-1] is held for all  1<=i< #row; 1<= j< #column
- if all diagonals meet the requirements, then the entire matrix meet the requirement. 
'''

import sys

def isEqual(a,b):
    if a == b:
        return True
    else:
        return False

def main():
    content = sys.stdin.read().strip().split('\n')
    numbers_of_matrix = content.pop(0)
    row = int(numbers_of_matrix.split(' ')[0])
    column = int(numbers_of_matrix.split(' ')[1])
    # print(row,column)
    matrix = list(map(lambda x: x.split(' '), content))
    # print(matrix,end='')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i >= 1 and j >= 1:
                if isEqual(matrix[i][j],matrix[i-1][j-1]) != True:
                    print("this matrix doesn't conform to the requirements")
                    return
    print("this matrix conforms to the requirements")


main()