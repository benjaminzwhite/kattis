# Dual Divisibility
# https://open.kattis.com/problems/dualdivisibility
# TAGS: brute force
# CP4: 0, Not In List Yet
# NOTES:
"""
Not sure if this is a troll question (since the difficulty is 4+) - but if you read the question carefully:

"Given two positive integers and ****with the same number of digits****** compute the number of divisors of a that have b as a divisor."

So the only possibilities are 1,2,3...10* that value of b (otherwise they would not have the same number of digits)
"""
a, b = map(int, input().split())

res = 0
for k in range(1, 11):
    if a % (k * b) == 0:
        res += 1
        
print(res)