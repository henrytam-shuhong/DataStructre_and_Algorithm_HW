## How to run the code:
```teminal
python3 problem01.py <marriage_mtest.txt

```

## description
- take the input file and store it in a dictionary as a preference
- divide the participants into two equal groups, group 1 and group 2 based on the order in the input
- initially, all participants in group1 were unmatched
- current_matches track the current pairings and next_proposal track the index of the next person each participant will propose to (all 0 at first)
- while there are unmatched participants in group1, then:
	- an unmatch participant proposes to the preferred participant in the Next_proposal map
	- if the current preferred participant is free, then match the pair and record it to the  current match map; the index in the next_match map increases 1
	- if the curent preferred participant is not free, compare the participants and decide who is more preferred. the loser will be put back to the queue.
	- repeat the steps until the queue is empty. 
- out put the result
