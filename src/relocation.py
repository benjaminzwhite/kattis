# Relocation
# https://open.kattis.com/problems/relocation
# TAGS: basic
# CP4: 2.3c, DAT, Others
# NOTES:
"""
CARE! 1-based indexing
"""
N, Q = map(int, input().split())
locations = list(map(int, input().split()))
for _ in range(Q):
    command, f, s = map(int, input().split())
    if command == 1:
        locations[f-1] = s # 1-based indexing
    elif command == 2:
        print(abs(locations[f-1] - locations[s-1]))