import sys

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.value = []

class FlatMatrix(Matrix):
    def __init__(self, rows, cols):
        self.value = []


# read file from standard input and convert it to a matrix
def readFile():
    matrixArr = []
    linesArr= sys.stdin.read().strip().split('\n')
    # print(linesArr)
    for i in linesArr:
        temp = []
        arr = i.strip().split(',')
        # print(arr)
        for val in arr:
            int(val)
            temp.append(int(val))
        matrixArr.append(temp)
    # print(matrixArr)
    return matrixArr

def FlatMatrix(matrix):
    flatedMatrix = []
    for i in matrix:
        for j in i:
            flatedMatrix.append(j)
    return flatedMatrix

def main():
    # convert inputFile to a matrix
    matrixArr = readFile()
    # manipulate matrixArr
    # print(matrixArr[2][0])

    # Flat an Matrix
    flatedMatrix = FlatMatrix(matrixArr)
    print(flatedMatrix)
    # manipulate flatedMatrix
    print(flatedMatrix[2*len(matrixArr[0]) + 0])

main()