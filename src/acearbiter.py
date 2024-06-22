# Ace Arbiter
# https://open.kattis.com/problems/acearbiter
# TAGS: logic, interpreter
# CP4: 0, Not In List Yet
# NOTES:
"""
Took me a while to understand input format:
The lines are NOT DIFFERENT ROUNDS hence why you have 1-0 1-0 1-0 repeatedly.
The Eve referee can decide to take scores MULTIPLE TIMES FOR SAME ROUND so above
example would be 3 snapshots of the same round.

So you are just checking that:
a) the players take turns correctly and that their scores are NON-DECREASING
b) a few edge/final conditions: what happens when one player reaches 11 etc

See notes in code below:
"""
n = int(input())

prev_a, prev_b = 0, 0

# NOTES: alice starts and score is 0-0, then bob serves when score has +1 and +2, then alice when score has +3,+4 etc.
# so alice is serving when SUM OF SCORES % 4 == 0 or == 3, and bob when SUM OF SCORES % 4 == 1 or 2
for i in range(1, n + 1):
    # assume alice serving, so say left number is alice and right is bob
    a, b = map(int, input().split('-'))
    if (a + b) % 4 in (1, 2):
        # in this case, actually bob is serving since sum of scores is 1 or 2 % 4 so swap a,b to b,a
        a, b = b, a
    # failures/errors:
    # 1) if either score is < prev score
    # 2) if someone reaches 11 but there are more rounds AFTER i.e. if i < n 
    # -> CARE! noticed after failing first submit:
    #    The records ARE NOT ROUNDS - THEY ARE "SNAPSHOTS" SO YOU CAN HAVE MULTIPLE LINES FROM THE SAME "ROUND"
    #    e.g. 11-0, 11-0, 11-0 is valid. So you can't just do step 2) with "i<n check".
    #    Instead check that if a==11 then b==prev_b etc. In other words that b DID NOT PLAY after a reached 11 and vice versa
    # 3) if a score ever exceeds 11
    # 4) if both scores are 11 same turn (can handle in case 2) but listing separately here)
    if (a < prev_a or b < prev_b) or (a == prev_a == 11 and b != prev_b) or (b == prev_b == 11 and a != prev_a) or (a > 11 or b > 11) or (a == b == 11):
        print("error", i)
        break
    prev_a, prev_b = a, b
    if i == n: # made it to the end ok O_o
        print("ok")