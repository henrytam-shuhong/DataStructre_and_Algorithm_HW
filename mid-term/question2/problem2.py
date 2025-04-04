
# Write an algorithm to calculate if the infection will stop spreading and there are any healthy counties left in the state.
# There are healthy counties left
# There are no healthy counties left

# 5
# 0 2
# 0 4
# 1 1
# 1 4
# 2 2
# 3 0
# 3 3
# 4 2

import sys
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.value = []

# flatten the matrix
def FlatMatrix(matrix):
    flatedMatrix = []
    for i in matrix:
        for j in i:
            flatedMatrix.append(int(j))
    return flatedMatrix

def infectNeigbors(flatedMatrix):
    # examine if the numbers of 0 changes
    zeroCounter = 0

    for i, value in enumerate(flatedMatrix):
        # print(i)
        if flatedMatrix[i] == 1:  # infected
            # check the existence of the companies:
            if i + 6 < len(flatedMatrix) and flatedMatrix[i + 6] == 1:
                # infect the neighbors
                flatedMatrix[i + 1] = 1
                flatedMatrix[i + 5] = 1
            if i - 6 >= 0 and flatedMatrix[i - 6] == 1:
                flatedMatrix[i - 1] = 1
                flatedMatrix[i - 5] = 1
            if i + 4 < len(flatedMatrix) and  (i % 5 != 0) and flatedMatrix[i + 4] == 1:
                flatedMatrix[i - 1] = 1
                flatedMatrix[i + 5] = 1
            if i - 4 >= 0 and ((i + 1) % 5 != 0) and flatedMatrix[i - 4] == 1:
                flatedMatrix[i + 1] = 1
                flatedMatrix[i - 5] = 1
         # examine if the numbers of 0 changes
        else:
            zeroCounter +=1
    print("infected", flatedMatrix)
    return [flatedMatrix, zeroCounter]




def main():
    # create the matrix
    matrix = Matrix(5,5)

    # input 0 in the matrix
    for i in range(5):
        temp = []
        for j in range(5):
            temp.append(0)
        matrix.value.append(temp)
    # print(matrix.value)


    # input coordinates to the matrix
    # Read all input from standard input
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    # print(lines)

    for i in lines[1:]:
        temp = i.strip().split(' ')
        matrix.value[int(temp[0])][int(temp[1])] = 1
    # print(matrix.value)

    # flatten the matrix
    flatedMatrix = FlatMatrix(matrix.value)
    print("original", flatedMatrix)


    # infect the neighbors:
    # traverse the flatedMatrix
    infectedFlatedMatrixArray = infectNeigbors(flatedMatrix)[0]
    # print(infectedFlatedMatrix)
    zeroCounter = infectedFlatedMatrixArray[1]
    # check if the last two zero-counters isn't the same, then repeat the infectedFlatedMatrix,
    # if they are the same, then means there are now more infections needed
    while zeroCounter != 0:
        tempCounter = infectNeigbors(flatedMatrix)[1]
        if tempCounter == zeroCounter:
            if zeroCounter == 0:
                print("There are no healthy counties left")
                return
            else:
                print("There are no healthy counties left")
                return

        else:
            zeroCounter = tempCounter

    if zeroCounter == 0:
        print("There are healthy counties left")
        return

    # # check if there are 0 in the final infectedFlatedMatrix array
    # for i in infectedFlatedMatrixArray[0]:
    #     # contains 0, which means there are healthy contries
    #     if i == 0:
    #         print("There are healthy counties left")
    #         return
    #
    # # all nubmers are 1, which means all countries are infected
    # print("There are no healthy counties left")
    # return


main()
