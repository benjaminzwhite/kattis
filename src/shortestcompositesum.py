# Shortest Composite Sum
# https://open.kattis.com/problems/shortestcompositesum
# TAGS: mathematics, number theory, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
Really don't understand what this is about O_o it's ranked 4.2+ - maybe is a troll question.

The smallest composite even number is 4 and smallest composite odd is 9.
If n is even, then n - 4 is even (and thus composite, since divisible by 2)
If n is odd, then n - 9 is even (and thus composite, since divisible by 2)
So you can always express n as a sum of two composite numbers.

Note e.g cant express n=1,2,3,4,5,6,7,9,11 as sum of composites but the description says it will
always be possible, so presumbly tests avoid precicely such numbers.
"""
n = int(input())

if n % 2 == 0:
    print(2)
    print(4, n - 4)
else:
    print(2)
    print(9, n - 9)