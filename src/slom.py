# Slom
# https://open.kattis.com/problems/slom
# TAGS: cipher, brute force
# CP4: 0, Not In List Yet
# NOTES:
"""
I just implemented the given procedure and looked at output: I figured that first char never moves, but then noticed that
the strings always repeat after a given period [seems to depend on even/odd and how chars repeat or not etc]

If you just implement the algorithm for a few iterations, you generate all possible strings that are obtainable, and the order
in which they cyclically appear.

Then, just compute the num_iterations % period, where here the period will be the length of the seen dict i.e. how many distinct strings are obtained

Then just need to lookup the right string that occurs at the right number of offset-iterations relative to the target string

e.g. if num_iterations = 123 and period is 5, you just look at the string that is 123%5 = 3 positions BEFORE the target string etc.
"""
num_iterations = int(input())
target = input()

s = target
seen = {}
position = 0
while s not in seen:
    seen[s] = position
    position += 1
    tmp  = [None] * len(s)
    for i in range((len(s) + 1) // 2):
        tmp[2 * i] = s[i]
    for j in range(1, len(s) // 2 + 1):
        tmp[2 * j - 1] = s[len(s) - j]
    s = ''.join(tmp)

period = len(seen)
initial_v = (seen[target] - num_iterations % period) % period # take % period to get +ve value

for k, v in seen.items():
    if v == initial_v:
        print(k)