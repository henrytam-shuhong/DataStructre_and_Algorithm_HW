import sys

def isPalinedrome(s):
    s = s.strip()
    return s == s[::-1]

def main():
    totalPalindromeCount = 0
    # read input
    for line in sys.stdin:
            # print each line read from the input file
       # print(line, end='')

    # check each line for palindrome
       if isPalinedrome(line):
           print('true')
           totalPalindromeCount += 1
       else:
           print('false')
    # print the total number of palindrome
    print(totalPalindromeCount)

# If this file is run directly
# if __name__ == '__main__':

main()