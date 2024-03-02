# Mirror Images
# https://open.kattis.com/problems/mirror
# TAGS: basic
# CP4: 1.6n, Output Formatting, E
# NOTES:
T = int(input())

for test_case in range(1, T + 1):
    res = []
    R, C = map(int, input().split())

    for _ in range(R):
        l = input()
        res.append(l[::-1])

    print("Test", test_case)
    print(*res[::-1], sep='\n')