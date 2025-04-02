
'''
implement a binary search tree
Create an ADT for a Node
Create an ADT for a BST with the following functions:
• Add Node(Value)
• Delete Node(Value)
• FindNode(Value)
• PrintTree()

Demonstrate you code by randomly generating an input set of size 5 to 50 for numbers between 1 and 1000
You must print out your input set, your initial tree and then exercise your methods add and delete printing your tree after every
method invocation. You must also exercise your findNode method by randomly generating a number between 1 and 1000 and
printing whether or not you found the node, you must have both positive and negative cases.
'''


# from binarytree import build
import random

# def print_tree_from_array(arr):
#     tree = build(arr)
#     print(tree)

# Define the Node ADT
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Define the Binary Search Tree ADT
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Add Node
    def add_node(self, value):
        def _add_recursive(current, value):
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    _add_recursive(current.left, value)
            else:
                if current.right is None:
                    current.right = Node(value)
                else:
                    _add_recursive(current.right, value)

        if self.root is None:
            self.root = Node(value)
        else:
            _add_recursive(self.root, value)

    # Delete Node
    def delete_node(self, value):
            def _delete_recursive(current, value):
                if not current:
                    return current
                if value < current.value:
                    current.left = _delete_recursive(current.left, value)
                elif value > current.value:
                    current.right = _delete_recursive(current.right, value)
                else:
                    if not current.left:
                        return current.right
                    elif not current.right:
                        return current.left
                    temp = self._min_value_node(current.right)
                    current.value = temp.value
                    current.right = _delete_recursive(current.right, temp.value)
                return current

            self.root = _delete_recursive(self.root, value)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Find Node
    def find_node(self, value):
            if self.root is None:
                return None
            node = self.root
            while node is not None:
                if value == node.value:
                    return node
                elif value < node.value:
                    node = node.left
                else:
                    node = node.right
            return None

    # Print Tree
    def print_tree(self):
        if not self.root:
            print("Tree is empty.")
            return

        def display(root, val="value", left="left", right="right"):
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)



# Demonstrate the Code
if __name__ == "__main__":
    # Randomly generate input set
    input_set = random.sample(range(1, 1001), random.randint(5, 50))
    print("Input Set:", input_set)
    # print("Level-order Traversal")
    # print_tree_from_array(input_set)
    # Create BST and populate it
    bst = BinarySearchTree()
    for value in input_set:
        bst.add_node(value)

    print("\nInitial binary search Tree :")
    bst.print_tree()

    # Test Add Node
    print("\n--- Adding Nodes ---")
    add_values = random.sample(range(1, 1001), 5)
    for val in add_values:
        print(f"Adding {val}")
        bst.add_node(val)
        print("Tree:")
        bst.print_tree()

    # Test Delete Node
    print("\n--- Deleting Nodes ---")
    delete_values = random.sample(input_set, min(3, len(input_set)))  # Choose 3 random values from input_set
    for val in delete_values:
        print(f"Deleting {val}")
        bst.delete_node(val)
        print("Tree:")
        bst.print_tree()

    # Test Find Node
    print("\n--- Finding Nodes ---")
    print("Tree:")
    bst.print_tree()
    find_values = random.sample(range(1, 1001), 5)
    for val in find_values:
        result = bst.find_node(val)
        print(f"Find {val}: {'Found' if result else 'Not Found'}")

    find_values = random.sample(range(0, len(input_set)), 3)

    for i in find_values:
        # print(i, find_values)
        result = bst.find_node(input_set[i])
        print(f"Find {input_set[i]}: {'Found' if result else 'Not Found'}")
