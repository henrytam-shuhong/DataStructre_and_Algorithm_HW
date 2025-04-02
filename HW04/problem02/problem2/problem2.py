# You are given an array with n elements and a number T (target). You can assume that the sum of all of the elements in the array
# is larger than T. Create an algorithm to compute the smallest number of elements from the array whose sum is greater than the
# target T.
# Example: given the array [8,3,9,2,7,1,5] with a target T of 18 then the answer is 3.
# You will be given an input file with the number of elements in the array on line 1, line 2 will contained a comma separated list of
# values for the array and line 3 will contain the target T.
# e.g.
# 7
# 8,3,9,2,7,1,5
# 18
# Your solution should print the given array to the console followed by the target and the answer to the console:
# Python3 smallestNumber.py < smallest_input.txt
# Input: 8,3,9,2,7,1,5 Target: 18 Answer: 3

# read the input file

# sorting the input array in order to find the greatest number and the second biggest number, and so on.
# because if the number of elements whose sum is larger than the target is smallest, we need to pick the biggest element each time.

# pick the largest element in the rest of array and add it to the sum
# compare the new sum to the target to determine if this is the final answer.

import sys
# read the input file
input = sys.stdin.read().strip()
inp_arr = input.split('\n')
orig_arr = list(map(int,inp_arr[2].split(' ')))
target = int(inp_arr[1])
# print(orig_arr, target)

# sort the input array in ascending order using heap sort

# heapify the input array into a max heap
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# heapSort the array
def heapSort(arr):
    n = len(arr)
    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements from heap one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def main():
    sorted_arr = heapSort(orig_arr.copy())
    # print(sorted_arr)

    # pick the largest element in the rest of array and add it to the sum
    Sum = 0
    count = 0
    for i in range(len(sorted_arr)-1,-1,-1 ):
        Sum += sorted_arr[i]
        count += 1
        if Sum > target:
            break

    print(f" Input: {orig_arr} Target:{target} Answer:{count}")


if __name__ == '__main__':
    main()