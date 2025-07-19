# Mathemagicians
# https://open.kattis.com/problems/mathemagicians
# TAGS: logic, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/mathemagicians.md
"""
n = int(input())
beginning = input()
end = input()

boundaries_b = sum(c1 != c2 for c1, c2 in zip(beginning, beginning[1:] + beginning[0]))
boundaries_e = sum(c1 != c2 for c1, c2 in zip(end, end[1:] + end[0]))

if boundaries_e < boundaries_b:
    print("yes")
elif boundaries_e == boundaries_b:
    # need to check that you have "space to move around" see notes
    if 0 < boundaries_b < n:
        print("yes")
    else:
        print("no")
else:
    # boundaries e > boundaries_b is always impossible
    print("no")