# Minimum Scalar Product
# https://open.kattis.com/problems/minimumscalar
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
T = int(input())

for case_number in range(1, T + 1):
    n = int(input())
    
    a = map(int, input().split())
    b = map(int, input().split())
    a = sorted(a)
    b = sorted(b)
    
    res = 0
    for x, y in zip(a, b[::-1]):
        res += x * y
    
    print(f"Case #{case_number}: {res}")