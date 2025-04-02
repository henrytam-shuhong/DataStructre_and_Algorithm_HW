import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.value

    def isEmpty(self):
        return self.top is None

def stringToArray(str):
    return [int(item.strip()) for item in str.split(',')]

def reverseLinkedListArray(stk):
    if stk.isEmpty():
        return
    temp = stk.pop()
    reverseLinkedListArray(stk)
    insertNode(stk,temp)

def insertNode(stk, item):
    if stk.isEmpty():
        stk.push(item)
        return
    temp =  stk.pop()
    insertNode(stk, item)
    stk.push(temp)

def main():
    # receive the input
    for line in sys.stdin:
        inputArray = stringToArray(line)
    # create a stack
    stk = LinkedListStack()

    for i in inputArray:
        stk.push(i)

    # print the original stack
    print("original stack", end=" ")
    pointer = stk.top
    while pointer:
        print(pointer.value, end=" ")
        pointer = pointer.next
    print()
        # stack: top ->10 -> 9 ->8 ... -> 1

    # reverse the stack
    reverseLinkedListArray(stk)

    # print the reversed stack
    print("reversed stack", end=" ")
    current = stk.top
    while current:
        print(current.value, end=" ")
        current = current.next


main()
