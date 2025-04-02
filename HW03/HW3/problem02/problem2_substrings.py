
# abcad
def main():
    print("please enter a string")
    # read a string input
    str = input().strip()
    # print(str)
    # create a set to store substrings
    uniqueSubstringsSet = set()
    # slice the string and store the substring
    substring(str, 0, 1, uniqueSubstringsSet)
    # print results
    print(', '.join(uniqueSubstringsSet))
    print(f"-->{len(uniqueSubstringsSet)}" )

def substring(s, start, end, substringSet):

        # termination condition of start:
        if start == len(s):
            return
        # termination condition of end: start...,final,lens(s),end
        if end == len(s)+1:
            substring(s, start + 1, start + 2, substringSet)
        else:
             # add the substring (e.g. a) of ab to the set
            substringSet.add(s[start:end])
            # increment the end and repeat the substring itself
            substring(s, start, end+1, substringSet)


main()