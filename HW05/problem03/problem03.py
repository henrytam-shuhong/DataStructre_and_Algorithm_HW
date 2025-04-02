'''
You are given two sequences of integers: A = {a1, a2, …. ai} and B = {b1, b2, …. bj}.
Define an algorithm that returns the longest sequence of alternating increasing
values from A and B where the sequence X = {x1, x2, …. xn} is as follows:
• The elements of X are increasing e.g. xi < xi+1 for all 1 <= I < n
• The odd-indexed elements of X are a subsequence of one of the sequences either A or B and the even-
indexed elements of X are a subsequence of the other sequence.
• Note a subsequence need not be consecutive elements of the original sequence but must maintain the
relative order of the original sequence
For example A = {1,7,2} and B = {4,8,3,9} then the answer is X = {4,7,9} which has a
length of 3.

5
6
8 2 9 1 4
4 1 5 3 2 6
'''

import sys

class TreeNode:
    def __init__(self, value, index, tag):
        """
        Initialize a tree node with a value, index, and tag.
        :param value: The value of the node.
        :param index: The index of the node (e.g., its position in the source list).
        :param tag: The tag of the node (either 1 or 0), meaning whether it belongs to arrA or arrB
        """
        self.value = value
        self.index = index
        self.tag = tag
        self.children = []

    def add_child(self, child_node):
        """Adds a child node to the current node."""
        self.children.append(child_node)

    def remove_child(self, child_node):
        """Removes a specific child node."""
        self.children = [child for child in self.children if child != child_node]

    def traverse(self, depth=0):
        """Traverses and prints the tree structure."""
        print("  " * depth + f"({self.value}, {self.index}, {self.tag})")  # Indentation represents depth
        for child in self.children:
            child.traverse(depth + 1)


class Tree:
    def __init__(self, root_value, root_index, root_tag):
        """Initialize the tree with a root node that has a value, index, and tag."""
        self.root = TreeNode(root_value, root_index, root_tag)

    def add_node(self, parent_value, parent_index, parent_tag, child_value, child_index, child_tag):
        """
        Adds a node with the specified value, index, and tag under the parent node with parent_value, parent_index, and parent_tag.
        """
        parent_node = self._find_node(self.root, parent_value, parent_index, parent_tag)
        if parent_node:
            parent_node.add_child(TreeNode(child_value, child_index, child_tag))
        else:
            print(f"Parent node with value '{parent_value}', index '{parent_index}', and tag '{parent_tag}' not found.")

    def _find_node(self, current_node, value, index, tag):
        """
        Helper method to find a node with the specified value, index, and tag.
        """
        if current_node.value == value and current_node.index == index and current_node.tag == tag:
            return current_node

        for child in current_node.children:
            result = self._find_node(child, value, index, tag)
            if result:
                return result
        return None

    """Finds the longest path from the root to any leaf node and its length."""
    def find_longest_path(self):


        def longest_path_from_node(node):
            if not node.children:
                return [node.value], 1  # Leaf node: path is itself, length is 1

            max_path = []
            max_length = 0
            for child in node.children:
                path, length = longest_path_from_node(child)
                if length > max_length:
                    max_path = path
                    max_length = length

            return [node.value] + max_path, max_length + 1

        if self.root:
            return longest_path_from_node(self.root)
        else:
            return [], 0

    def traverse(self):
        """Traverses the entire tree starting from the root."""
        if self.root:
            self.root.traverse()
        else:
            print("The tree is empty.")


def main(a, b):
    def _resursive(tree, current, arrA, arrB):
        if current is None:
            return
        if current.tag == 1:  # belongs to arrA, and search for children in arrB
            for i in range(current.index + 1, len(arrB)):
                if current.value < arrB[i]:
                    tree.add_node(current.value, current.index, current.tag, arrB[i], i, 0)

        elif current.tag == 0:  # belongs to arrB, and search for children in arrA
            for i in range(current.index + 1, len(arrA)):
                if current.value < arrA[i]:
                    tree.add_node(current.value, current.index, current.tag, arrA[i], i, 1)
        # 1 [8, 3, 9]
        for val in current.children:  # [8,3,9]
            _resursive(tree, val, arrA, arrB)

    # apply the recursive function to build up trees for arrA
    longest_length = 0
    _longest_path = []
    for i in range(0,len(a)):
        tree = Tree(a[i],i,1)
        _resursive(tree,tree.root, a, b)
        # tree.traverse()
    # 1, [8, 3, 9]
        # Find the longest path

        longest_path, length = tree.find_longest_path()
        # print(longest_path)
        # print("longest Length:", length)
        if length > longest_length:
            longest_length = length
            _longest_path = longest_path

    # print("long",_longest_path)
    return [longest_length, _longest_path]



# Example Usage
if __name__ == "__main__":

    read = sys.stdin.read().strip().split('\n')
    arrA = list(map(int, read[2].split(' ')))
    arrB = list(map(int, read[3].split(' ')))

    print(f"arrA:{arrA}\narrB:{arrB}")
    # arrA  = [1, 7, 2]
    # arrB = [4, 8, 3, 9]
    print("Length of longest alternating sequence for tree starting from arrA:", main(arrA, arrB)[0],f",which is {main(arrA, arrB)[1]}")
    print("Length of longest alternating sequence for tree starting from arrB:", main(arrB, arrA)[0],f",which is {main(arrB, arrA)[1]}")

    print("the overall max length:",max(main(arrA, arrB)[0], main(arrB, arrA)[0]))

