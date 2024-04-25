# Detailed solution for Kattis - Joyless Game

[Problem statement on Kattis](https://open.kattis.com/problems/joylessgame)

A good exercise to practice combinatorial game analysis with parity considerations.

## Tags

game, logic, proof

## Solution

- In any **final state**, no more characters can be deleted and conversely if no more characters can be deleted you are in a final state
- A character cannot be deleted iif it is 1) at start or end or 2) if deleting it would cause a doublet to form: **we will call this a "wall character"**
- So by the above 2 points, moving left to right through the final string we have:

```
 1 start char
 2 (maybe) a wall char, that cannot be deleted because doing so will cause 1-3 to form a doublet ==> therefore 3 must be SAME CHAR AS 1
 3 same char as 1
 4 (maybe) a wall char, that cannot be deleted because doing so will cause 3-5 to form a doublet ==> therefore 5 must be SAME CHAR AS 3
 5 same char as 3
 6 ...
 7 ...
 8 or 9 end char <-- so the solution reduces to studying what position the end char can be:
```

- If the end char is the same as the start char, then the end char must end up in position 3,5,7...i.e an odd position (to satisfy the above pattern), therefore the final string must be of length 3,5,7... i.e. **odd length**. In this case if the initial string is ODD length then there are an even number of moves to reach final string, so by parity argument since the final losing string is of EVEN parity then the starting player (who sees an odd string on his turns) is the loser, and vice versa for EVEN initial string.

- If the end char is not the same as the start char, then the end char must end up in position 2,4,6... i.e. an even position (to satisfy the above pattern; recall it cannot be in an odd position since they are all == position 1 == start char which is != end char by hypothesis). In this case if the initial string is ODD length then there are an odd number of moves to reach the final string, so by parity argument since the final losing string is of EVEN parity then the starting player (who sees ODD strings on his turns) is the winner, and vice versa for EVEN initial string.


## AC code

```python
T = int(input())

for _ in range(T):
    s = input()
    
    L = len(s)
    start_char = s[0]
    end_char = s[-1]
    
    if start_char == end_char:
        if L % 2 == 1:
            # start player - Chikapu - loses
            print("Bash")
        else:
            print("Chikapu")
    elif start_char != end_char: # NB: handles the edge case where s is of length 2 -> must have 2 distinct chars, so expect start player to lose -> OK
        if L % 2 == 1:
            # start player - Chikapu - wins
            print("Chikapu")
        else:
            print("Bash")
```