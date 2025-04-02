
## How to run the code:
```teminal
python3 problem01.py
```

## description
- create a Node class with three attributes: value, left, and right
- define a binary search tree class with methods of adding, deleting, finding nodes, and finding the minimum value notes
- for method: add_node:
    - compare the new value to add with the current node's value,
    - if the new one is smaller than move to the left, otherwise move to the left of the current node.
    - if there is no child node of the current node, create a new node and add the new value to it.
    - Otherwise, move to the child node and recursively compare the values.
    - The termination condition is when there is no child node of the current node and it's possible to add one to it.
- for method: find_node:
    - start from the root, compare the targeted value with the current node's value
    - if two value matches, then return the found node
    - if the targeted value is less than the current node's value, move to the left and compare the left child node with the target value
    - if the targeted value is bigger than the current node's value, move to the right and compare the right child node with the target value
    - if the child node doesn't exist, return none/
- for method: delete_node:
    - Searching for the Node:
        - If the tree is empty (current is None), return None
        - If the value to delete is less than the current node's value, recursively search in the left subtree
        - If the value to delete is greater than the current node's value, recursively search in the right subtree
        - If the value matches the current node's value, proceed to deletion
    - delete node:
        - There are three main cases when deleting a node:
            a) Node with No Children (Leaf Node):
                Simply return None, effectively removing the node
            b) Node with Only One Child:
                If no left child, return the right child
                If no right child, return the left child
                This effectively replaces the node with its only child
            c) Node with Two Children:
                Find the minimum value node in the right subtree (using _min_value_node)
                Replace the current node's value with this minimum value
                Recursively delete the minimum value node from the right subtree





