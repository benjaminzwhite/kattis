# DNA
# https://open.kattis.com/problems/dna
# TAGS: dynamic programming
# CP4: 0, Not In List Yet
# NOTES:
"""
dp[A][curr_char], dp[B][curr_char] states are lowest costs to flip all characters up to the current one to A or to B

The goal value is dp[A][length_of_entire_string], which is the lowest cost to flip all chars up to end of string to A

---

Implementation optimization:

You just need previous dp states, so don't need entire dp[][] array, just the previous costs for a and b
"""
n = int(input())
s = input()

prev_a = 0 # dp cost for: conv all previous chars to A
prev_b = 0 # dp cost for: conv all previous chars to B

for c in s:
    if c == 'A':
        a = prev_a # curr is == 'A' so no additional cost to change this once you have conv all previous chars to A in prev_a operations
        b = min(prev_a + 1, prev_b + 1) # curr is == 'A' so to convert all chars including curr to 'B'', 
        # [...] you must either: conv all previous chars to A, then flip entire prefix hence prev_a+1
        #       or: conv all previous chars to B, then flip curr from A to B for +1 move, for a total of prev_b+1
    else:
        a = min(prev_a + 1, prev_b + 1)
        b = prev_b
    prev_a, prev_b = a, b # update previous dp states

print(prev_a) # see optimization discussion - this is dp[A][length_of_entire_string] when you reach this point