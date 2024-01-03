# I've Been Everywhere, Man
# https://open.kattis.com/problems/everywhere
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
T = int(input())

for _ in range(T):
    N = int(input())
    s = set()
    for _ in range(N):
        curr = input()
        s.add(curr)
    print(len(s))