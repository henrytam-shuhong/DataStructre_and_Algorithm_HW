import sys
from array import array


# 5
# 1 2 3 4 5

def examineArr(arr, start, end):
    if start == 0 & (arr[end] > arr[len(arr) - 1] / 2):
            print("solution:YES")
            return

    if end == len(arr):
        print("solution: NO")
        return
    if (arr[end] - arr[start-1]) > arr[len(arr)-1] / 2:
        print("solution:YES")
        return
    examineArr(arr, start+1, end+1 )


def main():
    arr = []
    # Read all input from standard input
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    for i in lines[1].strip().split(' '):
        arr.append(int(i))
    print(f"input:{arr}")
    examineArr(arr, 0, 2)


main()