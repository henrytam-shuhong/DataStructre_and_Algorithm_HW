'''
You are given two sequences of integers: A = {a1, a2, …. ai} and B = {b1, b2, …. bj}.
Define an algorithm using dynamic programming that returns the longest sequence
of alternating increasing values from A and B where the sequence X = {x1, x2, …. xn}
is as follows:
• The elements of X are increasing e.g. xi < xi+1 for all 1 <= I < n
• The odd-indexed elements of X are a subsequence of one of the sequences either A or B and the even-
indexed elements of X are a subsequence of the other sequence.
• Note a subsequence need not be consecutive elements of the original sequence but must maintain the
relative order of the original sequence
For example A = {1,7,2} and B = {4,8,3,9} then the answer is X = {4,7,9} which has a
length of 3.
'''


import sys

def longest_alternating_subsequence(A, B):
    from functools import lru_cache

    n, m = len(A), len(B)

    @lru_cache(None)
    def dp(currSeq, prevIdx):
        # currSeq: 0 for A, 1 for B
        if currSeq == 0:  # Picking from A
            sequence = A
            otherSequence = B
        else:  # Picking from B
            sequence = B
            otherSequence = A

        max_length = 0
        # Start from the next index in the current sequence
        for i in range(prevIdx + 1, len(sequence)):
            if prevIdx == -1 or sequence[i] > otherSequence[prevIdx]:
                max_length = max(max_length, 1 + dp(1 - currSeq, i))

        return max_length

    # Start from either sequence with no prior element (-1)
    return max(dp(0, -1), dp(1, -1))


# Example usage:
# A = [1, 7, 2]
# B = [4, 8, 3, 9]

read = sys.stdin.read().strip().split('\n')
arrA = list(map(int, read[2].split(' ')))
arrB = list(map(int, read[3].split(' ')))
print(longest_alternating_subsequence(arrA, arrB))  # Output: 3

