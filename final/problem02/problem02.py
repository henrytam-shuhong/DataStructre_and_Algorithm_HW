'''
Huffman Encoding
Implement the Huffman Encoding Algorithm we went over in class:
Design an algorithm that takes as input a text document or long string. Create the Huffman frequency map, the Huffman tree and
write out the input text to a file.
You must print out your input set, your frequency map, your tree to the terminal window and write out your file. You must
provide screen shots of your code working.
You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how
to run your code and you must submit screen shots of your running code

'''

'''
- read the input file
- count the frequency of each character in the input file
- create a frequency table for each character in the input file
    - print out the frequency map
- create a binary tree or huffman tree where: 
    - each leaf node represents a character
    - internal nodes represent combind frequencies
    - print out the tree
- generate the specific binary code by traversing the tree 
    - every time passing the left node add 0
    - every time passing the right node add 1
- record the binary code for each character
- use the binary codes to encode the input text
    - write out the output code to a file  
'''


import heapq, sys
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1
    return freq_map

def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)


    return heap[0] if heap else None

def generate_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

    return codes

def encode_text(text, codes):
    return "".join(codes[char] for char in text)

def huffman_encoding(text):
    print("Input Text:", text)

    # Step 1: Calculate frequencies
    freq_map = calculate_frequencies(text)
    print("\nFrequency Map:", freq_map)

    # Step 2: Build Huffman Tree
    root = build_huffman_tree(freq_map)

    # Step 3: Generate Huffman Codes
    codes = generate_codes(root)
    print("\nHuffman Codes:", codes)

    # Step 4: Encode text
    encoded_text = encode_text(text, codes)
    print("\nEncoded Text:", encoded_text)

    return encoded_text, root, codes

    # Print Tree
def print_tree(root):
    if not root:
            print("Tree is empty.")
            return

    def display(root, val="freq", left="left", right="right", char="char"):
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                if getattr(root, char) == '\n':
                    line = '%s' % getattr(root, val) + 'return'
                else:
                    line = '%s' % getattr(root, val) + getattr(root, char)
                width = len(line)
                height = 1
                middle = width // 2

                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val) + getattr(root, char)
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

    lines, *_ = display(root)
    for line in lines:
            print(line)

def main():
    # Input from user or file
    read = sys.stdin.read()
    print(read)
    text = read

    # Encode the input text
    encoded_text, root, codes = huffman_encoding(text)

    # Print Tree
    print_tree(root)

    # Write encoded text to a file
    with open("encoded_output.txt", "w") as file:
        file.write(encoded_text)

    print("Encoded text written to encoded_output.txt")

if __name__ == "__main__":
    main()
