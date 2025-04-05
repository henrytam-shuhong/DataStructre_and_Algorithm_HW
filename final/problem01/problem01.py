'''
Perfect Date
Implement the gale shapley algorithm for the following problem:
You are building a dating web service. There are an equal number of men and women. Implement the gale-shapley algorithm to
assign the best dates for the given input. The algorithm mush match the men and women such that no date is unstable.
• Every man ranks the women in order of preference
• Every woman ranks the men in order of preference
• Each man proposes a date to the woman he most prefers
• Each woman either considers the date requests she receives and replies “maybe” to the man she likes best and “no” to all the rest
• As long as there are unmatched men, each man proposes a date to the most preferred woman to whom he has not yet proposed a date too regardless of
whether or not she is already matched
• Each woman reviews the new proposals and either replies “maybe” if she is not yet matched or if she prefers this new man to the one she was previously
matched to she rejects her previous date and accepts the new request
Demonstrate that your code works by running your solution in a terminal window. You must print your input and the calculated
output for each of the supplied input samples.
You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how
to run your code and you must submit screen shots of your running code.


Problem 1 (25 points) Perfect Date
Sample input file:
The first line will be the number of men and women
The following lines will be the person followed by their in-order selections

10
Benjamin Christine Marjorie Florence Katie Cynthia Julia Deborah Stella Karen Roberta
Kenneth Julia Katie Roberta Florence Stella Cynthia Christine Marjorie Karen Deborah
Shane Karen Cynthia Katie Stella Christine Roberta Julia Marjorie Florence Deborah Barry Stella Karen Julia Deborah Christine Cynthia Marjorie Roberta Katie Florence
Robert Florence Marjorie Deborah Roberta Karen Katie Christine Cynthia Stella Julia David Julia Stella Florence Marjorie Cynthia Deborah Roberta Christine Katie Karen
Travis Deborah Roberta Katie Stella Julia Cynthia Florence Christine Marjorie Karen
Eddie Florence Katie Stella Karen Marjorie Deborah Julia Christine Roberta Cynthia James Stella Florence Marjorie Katie Cynthia Julia Roberta Deborah Christine Karen
John Marjorie Deborah Julia Christine Stella Florence Roberta Karen Cynthia Katie Roberta Robert Travis Shane Benjamin David John James Barry Eddie Kenneth
Christine Robert Benjamin Barry Shane Kenneth John James David Travis Eddie
Cynthia John Barry Eddie David Benjamin Robert Kenneth Shane James Travis Julia Kenneth James Barry Travis John Eddie Benjamin David Robert Shane
Stella Benjamin Shane Kenneth James Barry Eddie Travis Robert John David Karen Shane Barry Robert John Kenneth David James Travis Benjamin Eddie
Marjorie Barry John Travis Kenneth David Robert Eddie Benjamin James Shane
Florence John James Benjamin Eddie David Kenneth Travis Shane Barry Rob

'''


# Gale-Shapley Algorithm for Stable Matching

import sys

def gale_shapley(preferences):
    n = len(preferences) // 2  # Number of participants in each group

    # Split participants into two groups
    group1 = list(preferences.keys())[:n]
    group2 = list(preferences.keys())[n:]

    # Initialize all participants as free
    free_group1 = group1[:]
    current_matches = {person: None for person in preferences}
    next_proposal = {person: 0 for person in preferences}  # Track the next proposal for each person

    while free_group1:
        proposer = free_group1.pop(0)  # Pick a free person from group1
        proposer_prefs = preferences[proposer]
        preferred = proposer_prefs[next_proposal[proposer]]  # Next preference to propose to
        next_proposal[proposer] += 1  # Move to the next preference for future proposals

        current_match = current_matches[preferred]  # Check the current match of the preferred person

        if current_match is None:  # Preferred person is free
            current_matches[preferred] = proposer
            current_matches[proposer] = preferred
        else:  # Preferred person is already matched
            preferred_prefs = preferences[preferred]
            if preferred_prefs.index(proposer) < preferred_prefs.index(current_match):  # Prefers the new proposer
                current_matches[preferred] = proposer
                current_matches[proposer] = preferred
                free_group1.append(current_match)  # The previous match becomes free
                current_matches[current_match] = None
            else:  # Prefers their current match
                free_group1.append(proposer)  # The proposer remains free

    # Create the final stable matching output
    stable_matching = {person: match for person, match in current_matches.items() if person in group1}
    return stable_matching


# # Sample Input for Testing
#
# preferences = {
#     'A': ['X', 'Y', 'Z'],
#     'B': ['Y', 'X', 'Z'],
#     'C': ['Y', 'Z', 'X'],
#     'X': ['B', 'A', 'C'],
#     'Y': ['A', 'B', 'C'],
#     'Z': ['A', 'C', 'B']
# }

read = sys.stdin.read().strip().split('\n')
read.pop(0)
# print(read)
if not read or len(read) % 2 != 0:
    print("Error: Invalid input. Ensure the input is non-empty and contains an even number of participants.")
    sys.exit(1)
preferences = {}
for line in read:
    temp = line.split(' ')
    key = temp[0]
    temp.pop(0)
    value = temp
    # print(key, value)
    preferences[key] = value


# Running the algorithm
result = gale_shapley(preferences)

# Display Input and Output
# print("Preferences:")
# for person, prefs in preferences.items():
#     print(f"{person}: {prefs}")

print("\nStable Matching Result:")
for person, match in result.items():
    print(f"{person} :  {match}")

