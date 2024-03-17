# Fridge
# https://open.kattis.com/problems/fridge
# TAGS: sorting, logic, improve
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
TODO: IMPROVE - find a logic/proof solution ?
"""
d = {n:0 for n in map(str, range(10))}

s = input()
for c in s:
    d[c] += 1

# get the least frequently occuring char that is NOT '0' to compare its frequency to that of '0'
# sort by ascending count, t[1], and tiebreak on ascending digit value e.g. ('3',1000) < ('6',1000) if both appear 1000 times
to_compare = min(((k, v) for k, v in d.items() if k != '0'), key=lambda t:(t[1], t[0]))
least_nonzero_char, least_nonzero_freq = to_compare
zero_freq = d['0']

# case 1: if 0 occurs least of all, then can make e.g. 10000 where number of zeroes is 1 greater than current number of zeroes
if zero_freq < least_nonzero_freq:
    print('1' + (zero_freq + 1) * '0')
# if not, i.e. nonzero char occurs least of all, print one more repetition of it
# (note this would always be the answer if 000....0 were allowed, but it isn't hence the first condition above)
else:
    print(least_nonzero_char * (least_nonzero_freq + 1))