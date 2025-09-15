# Forests
# https://open.kattis.com/problems/forests
# TAGS: dict, logic
# CP4: 2.4b, Union-Find
# NOTES:
"""
Reading comprehension/unclear: I guess (from getting WA on first submit) the fact that P can actually lead to "unused people"/people with no opinions:
basically if person 134 doesn't appear in the input, then their opinion is [] or None or whatever.

---

I was searching for exercises tagged Union Find on CP4 book, to practice, but this can be solved easily without it O_o
"""
P, T = map(int, input().split())

# As mentioned in notes, not very clear from exercise statement:
# Here I assume that, by default, every person has [] as their "observation"
d = {str(k) : [] for k in range(1, P + 1)}

while True:
    try:
        person, tree = input().split()
        d[person].append(tree)
    except:
        break

# TODO: IMPROVE: can problably do more efficiently with bitwise
# i.e. assign a bitmask to opinion whether i-th tree is seen i.e. 11001110 is an opinion etc
res = set(map(tuple, map(sorted, d.values())))

print(len(res))