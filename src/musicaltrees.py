# Musical Trees
# https://open.kattis.com/problems/musicaltrees
# TAGS: array, sorting, nice
# CP4: 2.2e, Sorting, Easier
# NOTES:
"""
Nice little exercise, especially for implementation:

Focus on the TREES AND WHAT THEY "CATCH" RATHER THAN PEOPLE AND WHERE THEY GO, nice change of perspective leads to clean solution

-> Each tree catches a person if that person is closer to that tree than any other
-> Tie break is that lower of 2 trees attracts midvalue
(e.g. 12 18 then tree 12 will attract a person 15 (where 12+18/2 = 15 midpoint tiebreaker illustration here))

---

Implementation note:

You can simplify the solution below, removing the assignments dict{}, but I left as-is because it's clearer
"""
P, T = map(int, input().split())
people = sorted(map(int, input().split()))
trees = sorted(map(int, input().split()))

ip = 0
assignments = {}
for left_tree, right_tree in zip(trees, trees[1:]):
    # iterate over pairs of trees, assuming that previous left tree has caught all its corresponding people:
    # therefore, at any step: current left_tree catches all people remaining in up to catch_r inclusve, where catch_r = (left_tree+right_tree)//2
    # " Note that if a person has more than one closest tree to them, they will always go for the one with the smallest t_i"
    # so make right range inclusive e.g. ts [4,6] then t=4 catches 1,2,3,4,5| since 5 has choice of going to 4 or 6 with movement=1 but goes to 4 since it is <6
    catch_r = (left_tree + right_tree) // 2
    tmp = []
    while ip < P and people[ip] <= catch_r:
        tmp.append(people[ip])
        ip += 1
    if tmp:
        assignments[left_tree] = tmp

if ip < P:
    # all the remaining unprocessed people go to rightmost tree
    assignments[trees[-1]] = people[ip:]

# any tree which has n > 1 persons assigned to it -> means that n-1 of those people will not get a tree.
# so go over the assignments found earlier and look at how many people were assigned to each tree.
res = sum(max(0, len(v) - 1) for v in assignments.values())

print(res)