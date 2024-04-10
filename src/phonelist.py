# Phone List
# https://open.kattis.com/problems/phonelist
# TAGS: string
# CP4: 6.2e, String Comparison
# NOTES:
"""
In lexicographic order any prefix will appear just before any string that it is a prefix of, so just need to check all pairs in a sorted list
"""
T = int(input())

for _ in range(T):
    n = int(input())
    
    xs = []
    for _ in range(n):
        xs.append(input())
    
    xs = sorted(xs)

    res = any(snd.startswith(fst) for fst, snd in zip(xs, xs[1:]))

    if res:
        print("NO")
    else:
        print("YES")