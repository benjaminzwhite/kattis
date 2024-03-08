# Un-bear-able Zoo
# https://open.kattis.com/problems/zoo
# TAGS: dict
# CP4: 2.3h, Balanced BST (map)
# NOTES:
from collections import defaultdict

case_number = 0
while (n:= int(input())):
    d = defaultdict(int)

    for _ in range(n):
        animal = input().split()[-1].lower()
        d[animal] += 1

    case_number += 1
    print(f"List {case_number}:")
    for k, v in sorted(d.items()):
        print(k, '|', v)