import sys

class ArrayStack:
    def __init__(self, value):
        self.stack = value[:]
# convert input string to array
def stringToArray(str):
    return [int(item.strip()) for item in str.split(',')]

# reverse the arrayStack
def reverseArrayStack(stk):
    if len(stk) == 0:
        return
    temp = stk.pop()
    reverseArrayStack(stk)
    insertItem(stk, temp)

# insert a new item
def insertItem(stk, item):
    if len(stk) == 0:
        stk.append(item)
        return
    temp = stk.pop()
    insertItem(stk,item)
    stk.append(temp)
    # print(stk, temp)

def main():
    # receive the input
    for line in sys.stdin:
        # print(line, end='')
        inputArray = stringToArray(line)
        # print(inputArray)

    # reverse the arrayStack
    stk = ArrayStack(inputArray).stack
    reverseArrayStack(stk)
    print(stk)

main()